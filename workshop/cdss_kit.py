"""
cdss_kit.py
The only module supplied by the instructor. It contains no clinical decision support
logic: the participant writes that, step by step, with a generative AI tool.

Two jobs.

CARRY FORWARD. Every cell the participant pastes code into begins with a marker line,
`#@cdss <step name>`. At the end of a notebook, export() gathers those cells in order and
prints them as one block, which is pasted at the top of the next notebook. Re-running a
corrected cell replaces the earlier version, so the exported block always holds the latest
working code.

VERIFICATION. The check functions test what the pasted code produced against the contract
stated at the end of each prompt. They inspect names, call functions and examine returned
objects. They never do the work themselves.
"""

from __future__ import annotations

import inspect
import io
import re
from collections import OrderedDict

LANG = "tr"
MARKER = "#@cdss"

OK, WARN, FAIL = "  [+] ", "  [!] ", "  [x] "

T = {
    "h_defined": {"tr": "TANIM KONTROLÜ", "en": "DEFINITION CHECK"},
    "h_call": {"tr": "FONKSİYON KONTROLÜ", "en": "FUNCTION CHECK"},
    "h_frame": {"tr": "VERİ KONTROLÜ", "en": "DATA CHECK"},
    "h_export": {"tr": "BU DEFTERDE YAZILAN KOD", "en": "CODE WRITTEN IN THIS NOTEBOOK"},
    "h_verdict": {"tr": "SONUÇ", "en": "VERDICT"},

    "missing": {"tr": "'{}' tanımlı değil. İstemdeki kabul ölçütlerini inceleyiniz.",
                "en": "'{}' is not defined. Review the contract in the prompt."},
    "defined": {"tr": "{} tanımlı ({}).", "en": "{} is defined ({})."},
    "not_callable": {"tr": "'{}' çağrılabilir değil; bir fonksiyon bekleniyordu.",
                     "en": "'{}' is not callable; a function was expected."},
    "call_failed": {"tr": "'{}' çağrıldığında hata verdi: {}: {}",
                    "en": "'{}' raised when called: {}: {}"},
    "call_ok": {"tr": "'{}' çalıştı ve {} döndürdü.", "en": "'{}' ran and returned {}."},
    "no_doc": {"tr": "'{}' için docstring yok. Ne yaptığını bir cümleyle yazınız.",
               "en": "'{}' has no docstring. State what it does in one sentence."},
    "sig": {"tr": "İmza: {}{}", "en": "Signature: {}{}"},

    "wrong_type": {"tr": "'{}' bir {} değil; gelen tür {}.",
                   "en": "'{}' is not a {}; the type received is {}."},
    "empty": {"tr": "'{}' boştur.", "en": "'{}' is empty."},
    "shape": {"tr": "{}: {} satır, {} sütun.", "en": "{}: {} rows, {} columns."},
    "col_missing": {"tr": "'{}' sütunu yok.", "en": "Column '{}' is missing."},
    "col_ok": {"tr": "İstenen {} sütunun tamamı yerinde.",
               "en": "All {} required columns are present."},
    "col_forbidden": {"tr": "'{}' sütunu hâlâ tabloda. Bu değer karar anında mevcut "
                            "değildir ve modele girmemelidir.",
                      "en": "Column '{}' is still present. This value is not available at "
                            "the decision point and must not reach the model."},
    "col_clean": {"tr": "Çıkarılması istenen sütunların hiçbiri tabloda değil.",
                  "en": "None of the columns that had to be removed are present."},
    "rows_few": {"tr": "Yalnızca {} satır var. Model kurulabilir, ancak elde edilen "
                       "sayılar başarım kanıtı sayılamaz.",
                 "en": "Only {} rows. A model can be built, but the figures obtained "
                       "cannot count as evidence of performance."},

    "pass": {"tr": "Kabul ölçütleri karşılanmıştır. Bir sonraki adıma geçebilirsiniz.",
             "en": "The contract is satisfied. You may move to the next step."},
    "fix": {"tr": "{} madde düzeltilmelidir. Üretilen kodu yapay zekâ aracına geri "
                  "veriniz, yukarıdaki eksikleri aktarınız ve kodu yeniden ürettiriniz.",
            "en": "{} item(s) need correction. Return the code to the AI tool, state the "
                  "shortcomings above and have it regenerated."},

    "no_steps": {"tr": "Bu defterde işaretli hiçbir hücre çalıştırılmamış. Yapıştırma "
                       "hücrelerinin ilk satırındaki {} işaretini silmeyiniz.",
                 "en": "No marked cell has been run in this notebook. Do not delete the "
                       "{} marker on the first line of the paste cells."},
    "export_head": {"tr": "Aşağıdaki bloğun tamamını kopyalayınız ve bir sonraki defterin "
                          "ilk yapıştırma hücresine yerleştiriniz.",
                    "en": "Copy the whole block below and paste it into the first paste "
                          "cell of the next notebook."},
    "export_count": {"tr": "{} adım, {} satır kod.", "en": "{} steps, {} lines of code."},
    "saved": {"tr": "Dosya olarak da kaydedildi: {}", "en": "Also saved to file: {}"},
}


def _t(key, *args):
    return T[key][LANG].format(*args)


def _header(key):
    line = _t(key)
    print(line)
    print("-" * max(46, len(line)))


def _verdict(problems):
    print()
    print(_t("h_verdict"))
    if problems == 0:
        print(OK + _t("pass"))
        return True
    print(FAIL + _t("fix", problems))
    return False


def _caller_globals(depth=2):
    frame = inspect.currentframe()
    for _ in range(depth):
        frame = frame.f_back
    return frame.f_globals


# ------------------------------------------------------------------ carry forward


def _history():
    """Executed cell sources, in order, from the IPython session."""
    try:
        return list(get_ipython().user_ns.get("In", []))  # noqa: F821
    except NameError:
        pass
    frame = inspect.currentframe()
    while frame is not None:
        if "In" in frame.f_globals:
            return list(frame.f_globals["In"])
        frame = frame.f_back
    return []


def steps() -> "OrderedDict[str, str]":
    """Marked cells, keyed by step name, latest version of each."""
    found = OrderedDict()
    pattern = re.compile(rf"^\s*{re.escape(MARKER)}\s*(.*)$")
    for source in _history():
        if not isinstance(source, str) or MARKER not in source:
            continue
        lines = source.split("\n")
        name, body = None, []
        for line in lines:
            m = pattern.match(line)
            if m and name is None:
                name = m.group(1).strip() or f"adim_{len(found) + 1}"
                continue
            body.append(line)
        if name is None:
            continue
        code = "\n".join(body).strip("\n")
        if code.strip():
            # Yeniden çalıştırılan adım kendi sırasında kalır, yalnızca içeriği yenilenir.
            found[name] = code
    return found


def export(save_as: str | None = None) -> str:
    """Print every marked cell as one block, ready for the next notebook."""
    collected = steps()
    _header("h_export")
    if not collected:
        print(FAIL + _t("no_steps", MARKER))
        return ""

    buffer = io.StringIO()
    for name, code in collected.items():
        buffer.write(f"{MARKER} {name}\n{code}\n\n")
    text = buffer.getvalue().rstrip() + "\n"

    print(_t("export_count", len(collected), text.count("\n")))
    print(_t("export_head"))
    print()
    print(text)

    if save_as:
        with open(save_as, "w", encoding="utf-8") as handle:
            handle.write(text)
        print(_t("saved", save_as))
    return text


# ----------------------------------------------------------------------- checks


def check_defined(*names) -> bool:
    """Every name exists in the participant's namespace."""
    _header("h_defined")
    scope = _caller_globals()
    problems = 0
    present = []
    for name in names:
        if name not in scope or scope[name] is None:
            print(FAIL + _t("missing", name))
            problems += 1
        else:
            present.append(f"{name}: {type(scope[name]).__name__}")
    for line in present:
        print(OK + _t("defined", line.split(":")[0], line.split(": ")[1]))
    return _verdict(problems)


def check_function(name, call_with=None, expect_type=None, needs_doc=True) -> bool:
    """The named function exists, carries a docstring, runs and returns the right type."""
    _header("h_call")
    scope = _caller_globals()
    problems = 0

    if name not in scope:
        print(FAIL + _t("missing", name))
        return _verdict(1)

    fn = scope[name]
    if not callable(fn):
        print(FAIL + _t("not_callable", name))
        return _verdict(1)

    try:
        print(OK + _t("sig", name, str(inspect.signature(fn))))
    except (TypeError, ValueError):
        pass

    if needs_doc and not (fn.__doc__ or "").strip():
        print(WARN + _t("no_doc", name))

    if call_with is None:
        return _verdict(problems)

    args, kwargs = call_with if isinstance(call_with, tuple) else (call_with, {})
    try:
        result = fn(*args, **kwargs)
    except Exception as exc:  # noqa: BLE001
        print(FAIL + _t("call_failed", name, type(exc).__name__, str(exc)[:140]))
        return _verdict(problems + 1)

    print(OK + _t("call_ok", name, type(result).__name__))
    if expect_type and not isinstance(result, expect_type):
        want = getattr(expect_type, "__name__", str(expect_type))
        print(FAIL + _t("wrong_type", name, want, type(result).__name__))
        problems += 1
    return _verdict(problems)


def check_frame(df, name="df", required=None, forbidden=None, min_rows=1) -> bool:
    """A returned table has the columns the contract asked for and none it forbade."""
    _header("h_frame")
    problems = 0

    if df is None:
        print(FAIL + _t("missing", name))
        return _verdict(1)
    if not hasattr(df, "columns") or not hasattr(df, "shape"):
        print(FAIL + _t("wrong_type", name, "DataFrame", type(df).__name__))
        return _verdict(1)
    if len(df) == 0:
        print(FAIL + _t("empty", name))
        return _verdict(1)

    print(OK + _t("shape", name, len(df), df.shape[1]))

    required = list(required or [])
    missing = [c for c in required if c not in df.columns]
    for column in missing:
        print(FAIL + _t("col_missing", column))
    problems += len(missing)
    if required and not missing:
        print(OK + _t("col_ok", len(required)))

    forbidden = list(forbidden or [])
    left = [c for c in forbidden if c in df.columns]
    for column in left:
        print(FAIL + _t("col_forbidden", column))
    problems += len(left)
    if forbidden and not left:
        print(OK + _t("col_clean"))

    if len(df) < min_rows:
        print(WARN + _t("rows_few", len(df)))

    return _verdict(problems)


# ------------------------------------------------- later notebook checks

T.update({
    "h_split": {"tr": "AYRIM KONTROLÜ", "en": "SPLIT CHECK"},
    "h_model": {"tr": "MODEL KONTROLÜ", "en": "MODEL CHECK"},
    "h_numbers": {"tr": "SAYI KONTROLÜ", "en": "NUMBER CHECK"},
    "h_report": {"tr": "RAPOR KONTROLÜ", "en": "REPORT CHECK"},

    "split_overlap": {"tr": "{} hasta hem eğitim hem sınama grubunda. Ayrım hasta düzeyinde "
                            "yapılmamış; model o hastaları tanıyacağı için sınama sonucu "
                            "olduğundan iyi çıkar.",
                      "en": "{} patient(s) are in both the training and test groups. The "
                            "split was not made at patient level; the model will recognise "
                            "them and the test result will look better than it is."},
    "split_ok": {"tr": "Eğitim {} satır, sınama {} satır. Ortak hasta yok.",
                 "en": "Training {} rows, test {} rows. No patient appears in both."},
    "split_one_class": {"tr": "{} grubunda hedef tek değer alıyor; bu grupla ölçüm yapılamaz.",
                        "en": "The target takes one value only in the {} group; no "
                              "measurement is possible with it."},
    "split_rate": {"tr": "Olay oranı eğitimde {:.1%}, sınamada {:.1%}.",
                   "en": "Event rate {:.1%} in training, {:.1%} in test."},

    "model_no_fit": {"tr": "'{}' bir model gibi davranmıyor; fit veya predict yöntemi yok.",
                     "en": "'{}' does not behave like a model; it has no fit or predict "
                           "method."},
    "model_no_proba": {"tr": "Model olasılık üretmiyor. Eşik belirlenemez, yalnızca hazır "
                             "sınıf etiketi alınabilir.",
                       "en": "The model does not produce probabilities. No threshold can be "
                             "set; only ready-made class labels are available."},
    "model_ok": {"tr": "'{}' eğitilmiş bir model ve olasılık üretiyor ({}).",
                 "en": "'{}' is a fitted model and produces probabilities ({})."},

    "num_count": {"tr": "{} sayı bekleniyordu, {} geldi.", "en": "{} numbers expected, {} received."},
    "num_range": {"tr": "Değerler {} ile {} arasında olmalıydı; gelen aralık {:.3f} - {:.3f}.",
                  "en": "Values should lie between {} and {}; the range received is {:.3f} - {:.3f}."},
    "num_constant": {"tr": "Bütün değerler aynı. Model hiçbir ayrım yapmıyor.",
                     "en": "Every value is identical. The model separates nothing."},
    "num_ok": {"tr": "{} değer, {:.3f} ile {:.3f} arasında.",
               "en": "{} values, ranging from {:.3f} to {:.3f}."},

    "rep_not_text": {"tr": "'{}' bir metin değil; gelen tür {}.",
                     "en": "'{}' is not text; the type received is {}."},
    "rep_missing": {"tr": "Raporda '{}' bölümü geçmiyor.", "en": "The report does not mention '{}'."},
    "rep_ok": {"tr": "Rapor {} satır ve istenen {} başlığın tamamını içeriyor.",
               "en": "The report has {} lines and contains all {} required headings."},
})


def check_split(train, test, target, patient_id) -> bool:
    """The split holds out whole patients and leaves both groups usable."""
    _header("h_split")
    problems = 0
    for frame, label in ((train, "egitim"), (test, "sinama")):
        if frame is None or not hasattr(frame, "columns"):
            print(FAIL + _t("missing", label))
            problems += 1
    if problems:
        return _verdict(problems)

    overlap = set(train[patient_id]) & set(test[patient_id])
    if overlap:
        print(FAIL + _t("split_overlap", len(overlap)))
        problems += 1
    else:
        print(OK + _t("split_ok", len(train), len(test)))

    for frame, label in ((train, "eğitim" if LANG == "tr" else "training"),
                         (test, "sınama" if LANG == "tr" else "test")):
        if frame[target].nunique() < 2:
            print(FAIL + _t("split_one_class", label))
            problems += 1

    if problems == 0:
        print(OK + _t("split_rate", float(train[target].mean()), float(test[target].mean())))
    return _verdict(problems)


def check_model(name, sample=None) -> bool:
    """The named object is a fitted model that can return probabilities."""
    _header("h_model")
    scope = _caller_globals()
    if name not in scope or scope[name] is None:
        print(FAIL + _t("missing", name))
        return _verdict(1)

    model = scope[name]
    if not (hasattr(model, "fit") and hasattr(model, "predict")):
        print(FAIL + _t("model_no_fit", name))
        return _verdict(1)

    if not hasattr(model, "predict_proba"):
        print(WARN + _t("model_no_proba"))
        return _verdict(0)

    if sample is None:
        print(OK + _t("model_ok", name, type(model).__name__))
        return _verdict(0)

    try:
        model.predict_proba(sample)
    except Exception as exc:  # noqa: BLE001
        print(FAIL + _t("call_failed", name, type(exc).__name__, str(exc)[:140]))
        return _verdict(1)

    print(OK + _t("model_ok", name, type(model).__name__))
    return _verdict(0)


def check_numbers(values, name="olasilik", count=None, low=0.0, high=1.0) -> bool:
    """A sequence of numbers has the expected length, range and variation."""
    _header("h_numbers")
    problems = 0
    try:
        series = [float(v) for v in values]
    except Exception:  # noqa: BLE001
        print(FAIL + _t("wrong_type", name, "sayi dizisi" if LANG == "tr" else "number sequence",
                        type(values).__name__))
        return _verdict(1)

    if count is not None and len(series) != count:
        print(FAIL + _t("num_count", count, len(series)))
        problems += 1

    lowest, highest = min(series), max(series)
    if lowest < low or highest > high:
        print(FAIL + _t("num_range", low, high, lowest, highest))
        problems += 1
    elif lowest == highest:
        print(FAIL + _t("num_constant"))
        problems += 1
    else:
        print(OK + _t("num_ok", len(series), lowest, highest))
    return _verdict(problems)


def check_report(text, name="rapor", must_contain=None) -> bool:
    """A produced report is text and mentions every required heading."""
    _header("h_report")
    if not isinstance(text, str):
        print(FAIL + _t("rep_not_text", name, type(text).__name__))
        return _verdict(1)

    required = list(must_contain or [])
    missing = [h for h in required if h.lower() not in text.lower()]
    for heading in missing:
        print(FAIL + _t("rep_missing", heading))
    if not missing:
        print(OK + _t("rep_ok", text.count("\n") + 1, len(required)))
    return _verdict(len(missing))
