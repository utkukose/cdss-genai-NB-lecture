"""
checks.py
Acceptance tests for code produced with a generative AI tool.

Each prompt in the workshop ends with a contract that names the variables and columns the
generated code must produce. The functions here test that contract, step by step, and
report what is missing.

When a task is delegated to a language model, the person delegating defines the interface.
A prompt without a contract produces code that cannot be checked.

Set LANG to 'tr' or 'en' before calling anything. The Turkish and English notebook sets
each set it once, at the top.
"""

from __future__ import annotations

import pandas as pd

LANG = "tr"

OK, WARN, FAIL = "  [+] ", "  [!] ", "  [x] "

# Column names that usually indicate a value recorded after the outcome.
LEAK_HINTS = [
    "los", "outtime", "dischtime", "deathtime", "discharge", "expire",
    "last_careunit", "cikis", "taburcu", "olum", "sure",
]

T = {
    "h_tables": {"tr": "TABLO KONTROLÜ", "en": "TABLE CHECK"},
    "h_target": {"tr": "HEDEF DEĞİŞKEN KONTROLÜ", "en": "TARGET CHECK"},
    "h_columns": {"tr": "SÜTUN KONTROLÜ", "en": "COLUMN CHECK"},
    "h_rows": {"tr": "SATIR SAYISI KONTROLÜ", "en": "ROW COUNT CHECK"},
    "h_cohort": {"tr": "KOHORT KONTROLÜ", "en": "COHORT CHECK"},
    "h_report": {"tr": "VERİ RAPORU", "en": "DATA REPORT"},
    "h_verdict": {"tr": "SONUÇ", "en": "VERDICT"},

    "no_var": {"tr": "'{}' adında bir değişken bulunmuyor. İstemdeki kabul ölçütlerini inceleyiniz.",
               "en": "No variable named '{}'. Review the contract in the prompt."},
    "not_frame": {"tr": "'{}' bir DataFrame değildir; gelen tür {}.",
                  "en": "'{}' is not a DataFrame; the type received is {}."},
    "empty": {"tr": "'{}' boştur.", "en": "'{}' is empty."},
    "table_ok": {"tr": "{}: {} satır, {} sütun.", "en": "{}: {} rows, {} columns."},

    "col_missing": {"tr": "'{}' sütunu bulunmuyor.", "en": "Column '{}' is missing."},
    "col_present": {"tr": "İstenen {} sütunun tamamı yerinde.",
                    "en": "All {} required columns are present."},
    "col_forbidden": {"tr": "'{}' sütunu tablodan çıkarılmamış. Bu değer karar anında "
                            "mevcut değildir ve modele girmemelidir.",
                      "en": "Column '{}' has not been removed. This value is not available "
                            "at the decision point and must not reach the model."},
    "col_clean": {"tr": "Çıkarılması istenen sütunların hiçbiri tabloda değil.",
                  "en": "None of the columns that had to be removed are present."},

    "target_not_binary": {"tr": "Hedef değişken '{}' ikili değildir. Bulunan değerler: {}",
                          "en": "Target '{}' is not binary. Values found: {}"},
    "target_ok": {"tr": "Hedef değişken '{}' ikilidir. Olay oranı: {:.1%} ({} / {})",
                  "en": "Target '{}' is binary. Event rate: {:.1%} ({} / {})"},
    "prevalence_low": {"tr": "Olay oranı düşüktür ({:.1%}). Bu sayıda pozitif vaka ile "
                             "ölçülen hiçbir başarım değeri güvenilir olmaz.",
                       "en": "The event rate is low ({:.1%}). No performance figure "
                             "measured on this few positives will be reliable."},

    "id_ok": {"tr": "Hasta kimliği '{}' yerinde. {} satır, {} ayrı hasta.",
              "en": "Patient id '{}' present. {} rows across {} distinct patients."},
    "id_repeat": {"tr": "Bir hastaya ait birden fazla satır bulunmaktadır. Veri eğitim ve "
                        "test olarak ayrılırken ayrım hasta düzeyinde yapılmalıdır.",
                  "en": "Some patients have more than one row. The train and test split "
                        "must therefore be made at patient level."},

    "rows_same": {"tr": "Satır sayısı korunmuş: {} satır.",
                  "en": "Row count preserved: {} rows."},
    "rows_grown": {"tr": "Satır sayısı {} değerinden {} değerine çıkmış. Birleştirme "
                         "sırasında satırlar çoğalmıştır; birleştirme anahtarını "
                         "denetleyiniz.",
                   "en": "Row count rose from {} to {}. The merge has duplicated rows; "
                         "check the join key."},
    "rows_dropped": {"tr": "Satır sayısı {} değerinden {} değerine inmiş. Düşüş bilinçli "
                           "ise sorun yoktur; değilse birleştirme türünü denetleyiniz.",
                     "en": "Row count fell from {} to {}. If the drop was intended this is "
                           "fine; otherwise check the join type."},
    "rows_few": {"tr": "Tabloda yalnızca {} satır bulunmaktadır. Model kurulabilir, ancak "
                       "elde edilen sayılar başarım kanıtı sayılamaz.",
                 "en": "The table has only {} rows. A model can be built, but the figures "
                       "obtained cannot count as evidence of performance."},

    "leak_found": {"tr": "Sızıntı şüphesi: '{}'. Bu değer sonuç belli olduktan sonra mı "
                         "kaydedilmektedir? Öyleyse tablodan çıkarınız.",
                   "en": "Possible leak: '{}'. Is this value recorded after the outcome is "
                         "known? If so, remove it."},
    "leak_none": {"tr": "Sütun adlarına dayalı sızıntı taramasında şüpheli bir ad "
                        "bulunmadı. Bu tarama yalnızca adlara bakar ve güvence vermez.",
                  "en": "The name based leak scan found nothing suspicious. This scan "
                        "inspects names only and is not a guarantee."},

    "missing_high": {"tr": "Yarıdan fazlası boş olan {} sütun bulunmaktadır. En yüksek üçü:",
                     "en": "{} columns are more than half empty. The highest three:"},

    "pass": {"tr": "Kabul ölçütleri karşılanmıştır. Bir sonraki adıma geçebilirsiniz.",
             "en": "The contract is satisfied. You may move to the next step."},
    "fix": {"tr": "{} madde düzeltilmelidir. Üretilen kodu yapay zekâ aracına geri veriniz, "
                  "yukarıdaki eksikleri aktarınız ve kodu yeniden ürettiriniz.",
            "en": "{} item(s) need correction. Return the generated code to the AI tool, "
                  "state the shortcomings listed above and have it regenerated."},
}


def _t(key: str, *args) -> str:
    return T[key][LANG].format(*args)


def _header(key: str) -> None:
    line = _t(key)
    print(line)
    print("-" * max(46, len(line)))


def _verdict(problems: int) -> bool:
    print()
    print(_t("h_verdict"))
    if problems == 0:
        print(OK + _t("pass"))
        return True
    print(FAIL + _t("fix", problems))
    return False


def _is_frame(obj, name: str) -> int:
    if obj is None:
        print(FAIL + _t("no_var", name))
        return 1
    if not isinstance(obj, pd.DataFrame):
        print(FAIL + _t("not_frame", name, type(obj).__name__))
        return 1
    if len(obj) == 0:
        print(FAIL + _t("empty", name))
        return 1
    return 0


# ------------------------------------------------------------------ step checks


def check_tables(**tables) -> bool:
    """Fetch step: every named table exists, is a DataFrame and is non-empty."""
    _header("h_tables")
    problems = 0
    for name, frame in tables.items():
        failed = _is_frame(frame, name)
        problems += failed
        if not failed:
            print(OK + _t("table_ok", name, len(frame), frame.shape[1]))
    return _verdict(problems)


def check_target(df, target: str, name: str = "df") -> bool:
    """Target step: the outcome column exists and takes exactly two values."""
    _header("h_target")
    problems = _is_frame(df, name)
    if problems:
        return _verdict(problems)

    if target not in df.columns:
        print(FAIL + _t("col_missing", target))
        return _verdict(1)

    values = sorted(pd.Series(df[target]).dropna().unique().tolist())
    if len(values) != 2 or not set(values) <= {0, 1, True, False}:
        print(FAIL + _t("target_not_binary", target, values[:6]))
        return _verdict(1)

    positives = int(pd.Series(df[target]).sum())
    rate = positives / len(df)
    print(OK + _t("target_ok", target, rate, positives, len(df)))
    if rate < 0.05:
        print(WARN + _t("prevalence_low", rate))
    if len(df) < 30:
        print(WARN + _t("rows_few", len(df)))
    return _verdict(0)


def check_columns(df, required=None, forbidden=None, name: str = "df") -> bool:
    """Merge and cleaning steps: required columns present, forbidden ones removed."""
    _header("h_columns")
    problems = _is_frame(df, name)
    if problems:
        return _verdict(problems)

    required = list(required or [])
    forbidden = list(forbidden or [])

    missing = [c for c in required if c not in df.columns]
    for column in missing:
        print(FAIL + _t("col_missing", column))
    problems += len(missing)
    if required and not missing:
        print(OK + _t("col_present", len(required)))

    left = [c for c in forbidden if c in df.columns]
    for column in left:
        print(FAIL + _t("col_forbidden", column))
    problems += len(left)
    if forbidden and not left:
        print(OK + _t("col_clean"))

    return _verdict(problems)


def check_rows(df, before: int, name: str = "df") -> bool:
    """Merge step: the join did not duplicate or silently discard rows."""
    _header("h_rows")
    problems = _is_frame(df, name)
    if problems:
        return _verdict(problems)

    after = len(df)
    if after == before:
        print(OK + _t("rows_same", after))
    elif after > before:
        print(FAIL + _t("rows_grown", before, after))
        problems += 1
    else:
        print(WARN + _t("rows_dropped", before, after))
    return _verdict(problems)


def check_cohort(df, target: str, patient_id: str, min_rows: int = 30) -> bool:
    """Final contract for the cohort: target, patient id and a leak scan together."""
    _header("h_cohort")
    problems = _is_frame(df, "df")
    if problems:
        return _verdict(problems)

    if target not in df.columns:
        print(FAIL + _t("col_missing", target))
        problems += 1
    else:
        values = sorted(pd.Series(df[target]).dropna().unique().tolist())
        if len(values) != 2 or not set(values) <= {0, 1, True, False}:
            print(FAIL + _t("target_not_binary", target, values[:6]))
            problems += 1
        else:
            positives = int(pd.Series(df[target]).sum())
            rate = positives / len(df)
            print(OK + _t("target_ok", target, rate, positives, len(df)))
            if rate < 0.05:
                print(WARN + _t("prevalence_low", rate))

    if patient_id not in df.columns:
        print(FAIL + _t("col_missing", patient_id))
        problems += 1
    else:
        unique = df[patient_id].nunique()
        print(OK + _t("id_ok", patient_id, len(df), unique))
        if unique < len(df):
            print(WARN + _t("id_repeat"))

    if len(df) < min_rows:
        print(WARN + _t("rows_few", len(df)))

    suspicious = [c for c in df.columns
                  if any(h in str(c).lower() for h in LEAK_HINTS) and c != target]
    if suspicious:
        for column in suspicious[:5]:
            print(WARN + _t("leak_found", column))
    else:
        print(OK + _t("leak_none"))

    return _verdict(problems)


# ---------------------------------------------------------------- final report


def data_report(df, target: str, patient_id: str) -> None:
    """The fixed end of notebook report, run on whatever the participant produced."""
    _header("h_report")
    labels = {"tr": ("satır", "sütun", "hasta", "olay"),
              "en": ("rows", "columns", "patients", "events")}[LANG]

    print(f"{labels[0]:<24} {len(df)}")
    print(f"{labels[1]:<24} {df.shape[1]}")
    print(f"{labels[2]:<24} {df[patient_id].nunique()}")
    positives = int(pd.Series(df[target]).sum())
    print(f"{labels[3]:<24} {positives} ({positives / len(df):.1%})")
    print()

    missing = df.isna().mean().sort_values(ascending=False)
    heavy = missing[missing > 0.5]
    if len(heavy):
        print(WARN + _t("missing_high", len(heavy)))
        for column, fraction in heavy.head(3).items():
            print(f"        {column:<30} {fraction:.0%}")
        print()

    if positives < 25:
        if LANG == "tr":
            print("Pozitif vaka sayısı yirmi beşin altındadır. Bundan sonra elde edilecek")
            print("her başarım değeri yöntemin gösterimi niteliğindedir; sonucun kanıtı")
            print("olarak sunulamaz.")
        else:
            print("There are fewer than twenty five positive cases. Every performance")
            print("figure obtained from here on demonstrates the method; none of them can")
            print("be presented as evidence about the result.")


# --------------------------------------------------- later notebook checks

T.update({
    "h_canvas": {"tr": "PROBLEM KARTI KONTROLÜ", "en": "PROBLEM CARD CHECK"},
    "h_split": {"tr": "AYRIM KONTROLÜ", "en": "SPLIT CHECK"},
    "h_model": {"tr": "MODEL KONTROLÜ", "en": "MODEL CHECK"},
    "h_pred": {"tr": "TAHMİN KONTROLÜ", "en": "PREDICTION CHECK"},

    "canvas_blank": {"tr": "'{}' sorusu cevaplanmamış. Boş bırakmak yerine bilmediğinizi "
                           "ve gerekçesini yazınız.",
                     "en": "Question '{}' is unanswered. Rather than leaving it blank, "
                           "state what is unknown and why."},
    "canvas_short": {"tr": "'{}' sorusunun cevabı çok kısa. Tek kelimelik bir cevap "
                           "istemin işine yaramaz.",
                     "en": "The answer to '{}' is very short. A one word answer is of no "
                           "use to the prompt."},
    "canvas_ok": {"tr": "Yedi sorunun tamamı cevaplanmış.",
                  "en": "All seven questions are answered."},

    "split_overlap": {"tr": "{} hasta hem eğitim hem test kümesinde bulunuyor. Ayrım satır "
                            "düzeyinde yapılmış. Modelin o hastaları tanıması nedeniyle "
                            "test başarımı olduğundan yüksek çıkar.",
                      "en": "{} patient(s) appear in both the training and test sets. The "
                            "split was made at row level. Test performance will come out "
                            "higher than it should because the model recognises them."},
    "split_ok": {"tr": "Eğitim {} satır, test {} satır. Ortak hasta yok.",
                 "en": "Training {} rows, test {} rows. No patient appears in both."},
    "split_onesided": {"tr": "{} kümesinde hedef değişken tek değer alıyor. Bu kümeyle "
                             "değerlendirme yapılamaz.",
                       "en": "The target takes only one value in the {} set. No evaluation "
                             "is possible with it."},
    "split_rate": {"tr": "Olay oranı eğitimde {:.1%}, testte {:.1%}.",
                   "en": "Event rate {:.1%} in training, {:.1%} in test."},
    "split_rate_gap": {"tr": "İki kümedeki olay oranı belirgin biçimde farklı. Küçük "
                             "kümelerde tek bir ayrım sonuçları kaydırabilir.",
                       "en": "The two event rates differ noticeably. In small cohorts a "
                             "single split can shift the results."},

    "model_no_proba": {"tr": "Model olasılık üretmiyor. predict_proba yöntemi bulunmuyor; "
                             "eşik belirlenemez.",
                       "en": "The model produces no probabilities. There is no "
                             "predict_proba method, so no threshold can be set."},
    "model_not_pipeline": {"tr": "Model bir Pipeline değil. Ölçekleme ve tamamlama "
                                 "adımlarının ayrımdan önce öğrenilmediğini "
                                 "doğrulayamıyorum; kodu kendiniz okuyunuz.",
                           "en": "The model is not a Pipeline. Whether scaling and "
                                 "imputation were fitted before the split cannot be "
                                 "verified here; read the code yourself."},
    "model_pipeline_ok": {"tr": "Model bir Pipeline. Ön işleme adımları: {}",
                          "en": "The model is a Pipeline. Preprocessing steps: {}"},
    "model_ok": {"tr": "Model eğitilmiş ve olasılık üretiyor.",
                 "en": "The model is fitted and produces probabilities."},

    "pred_length": {"tr": "Tahmin sayısı {}, test kümesi {} satır. İkisi eşit olmalıdır.",
                    "en": "There are {} predictions for {} test rows. The two must match."},
    "pred_range": {"tr": "Tahminler 0 ile 1 arasında değil. Olasılık yerine sınıf etiketi "
                         "üretilmiş olabilir.",
                   "en": "Predictions do not lie between 0 and 1. Class labels may have "
                         "been produced instead of probabilities."},
    "pred_constant": {"tr": "Bütün tahminler aynı değerde. Model hiçbir ayrım yapmıyor.",
                      "en": "Every prediction has the same value. The model separates "
                            "nothing."},
    "pred_ok": {"tr": "{} tahmin üretilmiş, değerler {:.3f} ile {:.3f} arasında.",
                "en": "{} predictions produced, ranging from {:.3f} to {:.3f}."},
})


def check_canvas(card: dict, min_chars: int = 25) -> bool:
    """NB1: every question on the problem card carries a usable answer."""
    _header("h_canvas")
    problems = 0
    for key, value in card.items():
        text = str(value or "").strip()
        if not text:
            print(FAIL + _t("canvas_blank", key))
            problems += 1
        elif len(text) < min_chars:
            print(WARN + _t("canvas_short", key))
    if problems == 0:
        print(OK + _t("canvas_ok"))
    return _verdict(problems)


def check_split(train, test, target: str, patient_id: str) -> bool:
    """NB3: the split holds out whole patients and leaves both sides usable."""
    _header("h_split")
    problems = _is_frame(train, "train") + _is_frame(test, "test")
    if problems:
        return _verdict(problems)

    overlap = set(train[patient_id]) & set(test[patient_id])
    if overlap:
        print(FAIL + _t("split_overlap", len(overlap)))
        problems += 1
    else:
        print(OK + _t("split_ok", len(train), len(test)))

    for name, part in (("train", train), ("test", test)):
        if pd.Series(part[target]).nunique() < 2:
            print(FAIL + _t("split_onesided", name))
            problems += 1

    if problems == 0:
        rate_train = float(pd.Series(train[target]).mean())
        rate_test = float(pd.Series(test[target]).mean())
        print(OK + _t("split_rate", rate_train, rate_test))
        if abs(rate_train - rate_test) > 0.10:
            print(WARN + _t("split_rate_gap"))

    return _verdict(problems)


def check_model(model) -> bool:
    """NB3: the model is fitted, returns probabilities, and keeps preprocessing inside."""
    _header("h_model")
    problems = 0

    if model is None:
        print(FAIL + _t("no_var", "model"))
        return _verdict(1)

    if not hasattr(model, "predict_proba"):
        print(FAIL + _t("model_no_proba"))
        problems += 1
    else:
        print(OK + _t("model_ok"))

    steps = getattr(model, "named_steps", None)
    if steps is None:
        print(WARN + _t("model_not_pipeline"))
    else:
        print(OK + _t("model_pipeline_ok", ", ".join(list(steps)[:-1]) or "-"))

    return _verdict(problems)


def check_predictions(y_prob, n_expected: int) -> bool:
    """NB3: predictions are probabilities, one per test case, and not constant."""
    _header("h_pred")
    problems = 0

    values = pd.Series(list(y_prob)).astype(float)
    if len(values) != n_expected:
        print(FAIL + _t("pred_length", len(values), n_expected))
        problems += 1

    low, high = float(values.min()), float(values.max())
    if low < 0 or high > 1:
        print(FAIL + _t("pred_range"))
        problems += 1
    elif low == high:
        print(FAIL + _t("pred_constant"))
        problems += 1
    else:
        print(OK + _t("pred_ok", len(values), low, high))

    return _verdict(problems)
