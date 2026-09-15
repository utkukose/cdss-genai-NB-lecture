"""
cdss_kit.py
Atölyede hazır verilen tek modül. Yaptığı iş tek şeydir: Defter boyunca yapıştırdığınız
kod hücrelerini toplar ve bir sonraki deftere taşıyabileceğiniz tek bir blok hâlinde verir.
Klinik karar destek mantığı içermez; onu siz yazarsınız.

The only module supplied in the workshop. It does one thing: it collects the code cells you
pasted through the notebook and returns them as a single block you can carry to the next
notebook. It contains no clinical decision support logic.
"""

from __future__ import annotations

import inspect
import io
import re
from collections import OrderedDict

LANG = "tr"
ISARET = "#@cdss"

MESAJ = {
    "baslik": {"tr": "BU DEFTERDE YAZILAN KOD", "en": "CODE WRITTEN IN THIS NOTEBOOK"},
    "bos": {"tr": "İşaretli hiçbir hücre çalıştırılmamış. Yapıştırma hücrelerinin ilk "
                  "satırındaki {} işaretini silmeyiniz.",
            "en": "No marked cell has been run. Do not delete the {} marker on the first "
                  "line of the paste cells."},
    "sayi": {"tr": "{} adım, {} satır kod.", "en": "{} steps, {} lines of code."},
    "kopyala": {"tr": "Aşağıdaki bloğun tamamını kopyalayıp bir sonraki defterin ilk "
                      "hücresine yapıştırınız.",
                "en": "Copy the whole block below and paste it into the first cell of the "
                      "next notebook."},
    "kaydedildi": {"tr": "Dosya olarak da kaydedildi: {}", "en": "Also saved to file: {}"},
}


def _m(anahtar, *args):
    return MESAJ[anahtar][LANG].format(*args)


def _gecmis():
    """Çalıştırılmış hücrelerin kaynak metinleri."""
    try:
        return list(get_ipython().user_ns.get("In", []))  # noqa: F821
    except NameError:
        pass
    kare = inspect.currentframe()
    while kare is not None:
        if "In" in kare.f_globals:
            return list(kare.f_globals["In"])
        kare = kare.f_back
    return []


def adimlar():
    """İşaretli hücreler, adım adına göre, her adımın en son sürümü."""
    bulunan = OrderedDict()
    desen = re.compile(rf"^\s*{re.escape(ISARET)}\s*(.*)$")
    for kaynak in _gecmis():
        if not isinstance(kaynak, str) or ISARET not in kaynak:
            continue
        ad, govde = None, []
        for satir in kaynak.split("\n"):
            eslesme = desen.match(satir)
            if eslesme and ad is None:
                ad = eslesme.group(1).strip() or f"adim_{len(bulunan) + 1}"
                continue
            govde.append(satir)
        if ad is None:
            continue
        kod = "\n".join(govde).strip("\n")
        if kod.strip():
            bulunan[ad] = kod          # düzeltilen adım kendi sırasında kalır
    return bulunan


def topla(dosya=None):
    """İşaretli bütün hücreleri tek blok hâlinde yazdırır."""
    toplanan = adimlar()
    baslik = _m("baslik")
    print(baslik)
    print("-" * max(46, len(baslik)))

    if not toplanan:
        print(_m("bos", ISARET))
        return ""

    tampon = io.StringIO()
    for ad, kod in toplanan.items():
        tampon.write(f"{ISARET} {ad}\n{kod}\n\n")
    metin = tampon.getvalue().rstrip() + "\n"

    print(_m("sayi", len(toplanan), metin.count("\n")))
    print(_m("kopyala"))
    print()
    print(metin)

    if dosya:
        with open(dosya, "w", encoding="utf-8") as tutamac:
            tutamac.write(metin)
        print(_m("kaydedildi", dosya))
    return metin


# İngilizce defterlerde aynı işlevler bu adlarla çağrılır.
steps = adimlar
export = topla
