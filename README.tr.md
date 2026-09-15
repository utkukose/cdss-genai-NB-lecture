<div align="center">

# Üretken Yapay Zekâ ile Klinik Karar Destek Sistemleri

### Ders ve Atölye Materyali

*Sağlık Bilimlerinde Teknoloji ve Yapay Zekâ Okuryazarlığı Eğitimi*
*Akdeniz Üniversitesi, Antalya · 16 ve 18 Eylül 2026*

[![Lisans](https://img.shields.io/badge/Lisans-CC%20BY--NC--SA%204.0-0E7C7B.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.tr)
[![Colab](https://img.shields.io/badge/NB1'i%20Colab'da%20a%C3%A7-C2185B.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB1_Veriye_Ulasmak.ipynb)
[![Defterler](https://img.shields.io/badge/Defter-12-16213C.svg)](notebooks/)
[![English](https://img.shields.io/badge/Material-English-6B7590.svg)](README.md)

**Prof. Dr. Utku Köse**

Süleyman Demirel Üniversitesi, Bilgisayar Mühendisliği Bölümü, Isparta, Türkiye<br>
Yapay Zekâ Uygulama ve Araştırma Merkezi (YAZEM) Müdürü<br>
University of North Dakota, Grand Forks, ABD<br>
Universidad Panamericana, Meksiko, Meksika<br>
Vel Tech University, Chennai, Hindistan<br>
IEEE Senior Member · ACM Professional Member

[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--9652--6415-A6CE39.svg)](https://orcid.org/0000-0002-9652-6415)
[![Web](https://img.shields.io/badge/Web-utkukose.com-16213C.svg)](https://www.utkukose.com)
[![GitHub](https://img.shields.io/badge/GitHub-utkukose-181717.svg)](https://github.com/utkukose)

</div>

---

## Bu depo nedir

Bu depo, yapay zekâ tabanlı klinik karar destek sistemleri üzerine birbirine bağlı iki
oturumun bütün materyalini içerir. Birincisi, bu sistemlerin ne olduğunu, sahada neden
başarısız olduklarını ve güvenilirliği neyin belirlediğini ele alan kırk beş dakikalık bir
derstir. İkincisi, katılımcıların üretken yapay zekâ araçlarıyla kendi klinik problemleri
için çalışan bir karar destek prototipi geliştirdiği, mümkün olduğunca az doğrudan kod
yazılan iki saatlik bir atölye çalışmasıdır.

İki oturum tek bir argüman olarak tasarlanmıştır. Ders, böyle bir sistemin kurulduğu on üç
aşamayı ve her aşamanın hangi ölçütle değerlendirildiğini ortaya koyar; atölye aynı
aşamaları defter defter yürür. Yalnızca atölyeye katılan biri akışı takip edebilir,
yalnızca derse katılan biri de atölyenin üzerine kurulduğu aşama listesiyle ayrılır.

**Atölye önceden Python bilgisi ve kurulum gerektirmez.** Her şey tarayıcı üzerinden Google
Colab ortamında çalışır.

---

## Depo yapısı

```
cdss-genai-NB-lecture/
├── lecture/
│   ├── KKDS-ders-notlari-TR.pdf        Görsellerle birlikte ders kaynak metni, Türkçe
│   ├── CDSS-lecture-notes-EN.pdf       Aynı metnin İngilizcesi
│   └── verified-sources.md             Her bilginin birincil kaynağı
├── slides/                             Ders notundan üretilen sunumlar, oturum sonrası eklenir
├── workshop/
│   └── cdss_kit.py                     Kodu defterler arasında taşır
├── notebooks/
│   ├── tr/                             Türkçe defterler, NB1 ile NB6 arası
│   └── en/                             İngilizce defterler, NB1 ile NB6 arası
├── prompts/
│   ├── tr/anti-patterns.md             Üretilen klinik kodda sık görülen hatalar
│   └── en/anti-patterns.md             Aynısının İngilizcesi
├── templates/
│   ├── tr/                             Model kartı ve düzenleyici triyaj, NB5 için başvuru
│   └── en/                             Aynı ikisinin İngilizcesi
├── LICENSE                             CC BY-NC-SA 4.0, üçüncü taraf kapsamı belirtilmiş
├── CITATION.cff                        Makine tarafından okunabilir atıf bilgisi
└── docs/images/
```

---

## Ders materyali

| | Belge | Dil |
|---|---|---|
| [PDF](lecture/KKDS-ders-notlari-TR.pdf) | Ders notları, görsellerle birlikte tam kaynak metin | Türkçe |
| [PDF](lecture/CDSS-lecture-notes-EN.pdf) | Aynı metnin İngilizce sürümü | İngilizce |
| [PDF](slides/KKDS-ders-sunumu-TR.pdf) | Sunum dosyası | Türkçe |
| [PDF](slides/CDSS-lecture-slides-EN.pdf) | Presentation deck | İngilizce |

Ders notları düz metin olarak yazılmıştır; NotebookLM ya da benzeri bir araca doğrudan
kaynak dosya olarak verilebilir. `slides/` klasöründeki sunumlar bu metinlerden üretilmekte
ve oturumdan sonra eklenmektedir. O klasördeki `README.md` dosyası, sunum ürettirmek için
kullanılan istemleri iki dilde içerir. Metindeki her şekil, tarih ve atıf
[lecture/verified-sources.md](lecture/verified-sources.md) dosyasında birincil kaynağına
kadar izlenmektedir.

---

## Defterlerin çalıştırılması

Materyal Türkçe ve İngilizce olmak üzere iki ayrı sürüm hâlinde hazırlanmıştır. Bu sayfa
Türkçe sürüme yönlendirir; İngilizce için [README.md](README.md) dosyasına bakınız. İki
sürüm birbirine atıf yapmaz ve katılımcı birini baştan sona takip eder.

| | Defter | Eklenen katman |
|---|---|---|
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB1_Veriye_Ulasmak.ipynb) | **NB1** Veriye ulaşmak | Hazırlık, veriyi getirme, ilk bakış |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB2_Veriyi_Hazirlamak.ipynb) | **NB2** Veriyi hazırlamak | Temizleme, hasta düzeyinde ayrım, modele uygun biçime çevirme |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB3_Model_Egitimi_ve_Degerlendirme.ipynb) | **NB3** Model eğitimi ve değerlendirme | Model, tahmin ve dokuz değerli dürüst ölçüm |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB4_Karari_Aciklamak.ipynb) | **NB4** Kararı açıklamak | Genel ve hasta düzeyinde gerekçe, gerekçenin eleştirisi |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB5_Guvenlik_ve_Uyumluluk.ipynb) | **NB5** Güvenlik ve uyumluluk | Üç bariyer, kırmızı takım denemesi, uyumluluk raporu |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB6_Web_Arayuzu.ipynb) | **NB6** Web arayüzü | Tarayıcıdan çalışan arayüz ve programın tamamı |

### Veri kümeleri

Açık erişimli altı veri kümesi hazırlanmıştır; katılımcı NB1'de birini seçer ve sonraki her
adım bu seçime göre ilerler.

| Kod | Tür | Veri kümesi | Erişim |
|---|---|---|---|
| `mimic-yogun-bakim` | tablo | MIMIC-IV demo, 100 hastanın yoğun bakım kaydı | HTTPS, kimlik doğrulaması yok |
| `wisconsin` | tablo | Breast Cancer Wisconsin, 569 örnek | scikit-learn içinde hazır |
| `pnomoni-mnist` | görüntü | PneumoniaMNIST, 5.856 akciğer grafisi | `pip install medmnist` |
| `meme-mnist` | görüntü | BreastMNIST, 780 ultrason görüntüsü | `pip install medmnist` |
| `mimic-ekg` | zaman serisi | MIMIC-IV-ECG demo, 92 hastadan 659 EKG | HTTPS, kimlik doğrulaması yok |
| `sentetik-not` | metin | Üretilen klinik notlar | Kod üretir |

EKG kümesi klinik demo ile aynı 92 hastayı içerir; o yolda aynı sonuç bu kez sinyalden
tahmin edilir ve iki yaklaşım doğrudan karşılaştırılabilir. MedMNIST kümelerinde hasta
kimliği bulunmaz ve defter bunu gizlemek yerine yazar. Kimlik doğrulaması istemeyen klinik
not kümesi bulunmadığından metin yolunda veri üretilir.

### Defterler nasıl çalışıyor

**Python bilmeniz gerekmez ve kodu siz yazmazsınız.** Her adımda sade bir klinik dille
yazılmış kısa bir istem verilir. İstemi bir üretken yapay zekâ aracına aktarır, aracın
verdiği kodu istemin altındaki boş hücreye yapıştırır ve çalıştırırsınız.

Her adımdan sonra birkaç soru gelir. Kodunuza ve çıktısına bakarak cevaplayınız. Sorular
atölyenin asıl içeriğidir: Üretilen kod ilk bakışta doğru görünür, yanlış olduğu yerler de
öyle görünür. Sorular sızıntıyı, hasta düzeyinde ayrımı, sınıf dengesizliğini ve düzenleyici
tarihleri doğrudan hedefler.

Defterlerde otomatik kod denetimi yoktur. Denetim sorumluluğu size aittir; atölyenin
öğrettiği şey de budur.

### Kod defterden deftere taşınır

Her yapıştırma hücresinin ilk satırında `#@cdss adim_adi` yazar. Defterin sonunda
`kit.export()` işaretli bütün hücreleri tek bir blok hâlinde toplar. O bloğu bir sonraki
defterin ilk hücresine yapıştırırsınız; böylece yazdığınız program birikerek ilerler. Bir
adımı düzeltip yeniden çalıştırdığınızda eski sürümün yerini yenisi alır ve adım kendi
sırasında kalır.

NB6'nın sonunda biriken kod, web arayüzü arkasında çalışan eksiksiz bir klinik karar destek
sistemidir ve `cdss_sistem.py` adıyla kaydedilir.

### Hazır verilen tek şey

Tek bir modül: `workshop/cdss_kit.py`. Yalnızca kodu defterler arasında taşır. İçinde klinik karar destek mantığı yoktur; onu siz yazarsınız.

**Bir koşul.** Defterler bu modülü `raw.githubusercontent.com` üzerinden çeker, bu nedenle
deponun herkese açık olması gerekir. Özel bir depoda bu çağrı 404 döner ve modülün Colab
oturumuna elle yüklenmesi gerekir.

---

## Birinci oturum — Ders, 16 Eylül 2026

**Yapay Zekâ Tabanlı Klinik Karar Destek Sistemleri**

Ders, bağımsız olarak doğrulanmış bir başarısızlık vakası üzerine kurulmuştur. Yüzlerce
hastanede kullanılan Epic Sepsis Model, 38.455 yatış üzerinde dış doğrulamaya tabi tutulmuş
ve üreticinin 0,76 ile 0,83 arasındaki iddiasına karşılık 0,63 eğri altı alan ile yüzde 12
pozitif kestirim değeri vermiştir. Üç yıl sonra 145.885 acil servis başvurusu üzerinde
yapılan ikinci doğrulamada duyarlılık yüzde 14,7 olarak bulunmuştur. Bu iki çalışmadan
atölyeye doğrudan taşınan üç sonuç çıkarılmaktadır: Dış doğrulama seçimlik değildir,
pozitif kestirim değeri yerel prevalans bilinmeden yorumlanamaz ve gereğinden sık
tetiklenen bir sistem kendi başına zarar üretir.

Kalan bölümler kalibrasyon ile ayrım gücü ayrımını, açıklanabilirliğin ne verip ne
vermediğini, bir iddiayı denetlenebilir kılan raporlama standartlarını ve Eylül 2026
itibarıyla Avrupa Birliği, Amerika Birleşik Devletleri ile Türkiye'deki düzenleyici konumu
ele almaktadır.

Ders kaynak metinleri `lecture/` klasöründedir. Düz metin olarak yazıldıkları için
NotebookLM ya da benzeri bir araca doğrudan kaynak dosya olarak verilip sunuma
dönüştürülebilirler. Metinlerdeki her şekil, tarih ve atıf `lecture/verified-sources.md`
dosyasında izlenmektedir.

---

## İkinci oturum — Atölye, 18 Eylül 2026

**Üretken Yapay Zekâ Araçları ile Klinik Karar Destek Sistemleri Geliştirilmesi**

Katılımcı altı defter boyunca çalışan bir klinik karar destek sistemi yazar. Python bilgisi
gerekmez ve kod elle yazılmaz: Her adımda sade bir klinik dille yazılmış bir istem verilir,
katılımcı bunu bir üretken yapay zekâ aracına aktarır, gelen kodu yapıştırır ve çalıştırır.
Ardından gelen kontrol hücresi, sonucu istemin sonundaki beklenen sonuca göre sınar.

| Defter | Eklenen katman |
|---|---|
| NB1 | Veriye ulaşma ve ilk bakış |
| NB2 | Temizleme, hasta düzeyinde ayrım, modele uygun biçime çevirme |
| NB3 | Modelin kurulması, öğretilmesi ve dürüst ölçüm |
| NB4 | Kararı gerekçelendiren katman |
| NB5 | Güvenlik bariyerleri ve uyumluluk raporu |
| NB6 | Web tarayıcısından kullanılan arayüz |

Kod defterden deftere taşınır. Her defterin sonunda o ana kadar yazılan bütün adımlar tek
bir blok hâlinde toplanır ve bir sonraki defterin ilk hücresine yapıştırılır. NB6'nın
sonunda biriken kod, web arayüzü arkasında çalışan eksiksiz bir sistemdir ve
`cdss_sistem.py` adıyla kaydedilir.

Katılımcı NB1'de yukarıdaki altı veri kümesinden birini seçer ve bu seçim sonraki her adımı
yönlendirir. Bir adım veri türüne göre gerçekten değişiyorsa istem kendi içinde dallanır;
diğer her yerde NB1'de tanımlanan sabitleri okur ve değişmeden çalışır. Hiçbir veri önceden
indirilmez ve burada yeniden dağıtılmaz.

**Veri kümeleri dağıtılabilir bir modeli taşıyacak büyüklükte değildir ve değerlendirme
bunu söyler.** Katılımcılar bir sistem kurar, dürüstçe ölçer ve devreye alınmaması
gerektiği sonucuna varır.

---

## Bu materyal nasıl kullanılır

**Katılımcı iseniz.** Hazırlık gerekmez. Oturuma bir tarayıcı ve bir üretken yapay zekâ
aracı hesabıyla geliniz; kullandığınız araç fark etmez. Hazırlanmak isterseniz NB1'i açıp
veri kümesi kataloğuna bakınız ve hangi kümeyle ilerleyeceğinize karar veriniz. Kendi
klinik probleminiz varsa ve kataloğun dışına çıkmak istiyorsanız, o problemi tek cümleyle
yazılı hâlde getiriniz.

**Materyali yeniden kullanan eğitmen iseniz.** Derste zamana bağlı üç başlık bulunur ve
ileride verilecek her oturumdan önce yeniden denetlenmelidir: Avrupa Birliği yapay zekâ
uyum takvimi, Amerika Birleşik Devletleri'ndeki cihaz sayısı ve ulusal mevzuattaki durum.
Üçü de bu nedenle `lecture/verified-sources.md` dosyasında tarihlendirilmiştir.

**Bu materyalin ne olmadığına dair bir not.** Buradaki hiçbir çıktı doğrulanmış bir klinik
araç değildir. Atölyede kurulan sistemler öğretim amaçlı yapıtlardır. Bunlardan herhangi
birinin gerçek hasta verisi üzerinde kullanılması ya da bir bakım ortamına alınması, dersin
anlattığı bütün mekanizmayı gerektirir: Dış doğrulama, kalibrasyon değerlendirmesi, alt
grup analizi, düzenleyici sınıflandırma ve devreye alma sonrası izleme.

---

## Atıf

```bibtex
@misc{kose2026cdssgenai,
  author       = {K{\"o}se, Utku},
  title        = {Clinical Decision Support Systems with Generative AI:
                  Lecture and Workshop Material},
  year         = {2026},
  howpublished = {\url{https://github.com/utkukose/cdss-genai-NB-lecture}},
  note         = {Technology and Artificial Intelligence Literacy Training in Health Sciences,
                  Akdeniz University}
}
```

## Lisans

Materyal, Creative Commons Atıf-GayriTicari-AynıLisanslaPaylaş 4.0 Uluslararası lisansı ile
yayımlanmaktadır. Atıf verilerek öğretim ve araştırma amacıyla paylaşılabilir ve
uyarlanabilir; izin alınmadan ticari olarak kullanılamaz veya satılamaz. Ayrıntı için
`LICENSE` dosyasına bakınız.

---

## Teşekkür

Bu oturumlar, TÜBİTAK destekli Sağlık Bilimlerinde Teknoloji ve Yapay Zekâ Okuryazarlığı
Eğitimi projesi kapsamında Akdeniz Üniversitesi ev sahipliğinde gerçekleştirilmiştir. Davet
ve organizasyon için proje yürütücülerine ve düzenleme kuruluna, klinik sorularıyla
atölyenin biçimlenmesine katkı veren katılımcılara teşekkür edilmektedir.

---

<div align="center">

**Prof. Dr. Utku Köse**

Süleyman Demirel Üniversitesi, Bilgisayar Mühendisliği Bölümü<br>
Yapay Zekâ Uygulama ve Araştırma Merkezi (YAZEM) Müdürü<br>
Isparta, Türkiye

[utkukose@sdu.edu.tr](mailto:utkukose@sdu.edu.tr) · [www.utkukose.com](https://www.utkukose.com) · [ORCID 0000-0002-9652-6415](https://orcid.org/0000-0002-9652-6415) · [github.com/utkukose](https://github.com/utkukose)

</div>
