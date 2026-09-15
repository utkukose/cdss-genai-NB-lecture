<div align="center">

# Üretken Yapay Zekâ ile Klinik Karar Destek Sistemleri

### Ders ve Atölye Materyali

*Teknoloji ve Yapay Zekâ Okuryazarlığı Eğitimi*
*Akdeniz Üniversitesi, Antalya · 16 ve 18 Eylül 2026*

[![Lisans: CC BY-NC-SA 4.0](https://img.shields.io/badge/Lisans-CC%20BY--NC--SA%204.0-0E7C7B.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.tr)
[![Colab'da aç](https://img.shields.io/badge/NB1'i-Colab'da%20aç-C2185B.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/NB1_CDSS_Canvas.ipynb)
[![English](https://img.shields.io/badge/Full%20material-English-6B7590.svg)](README.md)

**Prof. Dr. Utku Köse**

Süleyman Demirel Üniversitesi, Mühendislik ve Doğa Bilimleri Fakültesi, Bilgisayar Mühendisliği Bölümü
Yapay Zekâ Uygulama ve Araştırma Merkezi (YAZEM) Müdürü, Isparta
University of North Dakota · Universidad Panamericana · Vel Tech University
IEEE Senior Member · ACM Professional Member

[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--9652--6415-A6CE39.svg)](https://orcid.org/0000-0002-9652-6415)
[![Web](https://img.shields.io/badge/Web-utkukose.com-16213C.svg)](https://www.utkukose.com)
[![GitHub](https://img.shields.io/badge/GitHub-utkukose-181717.svg)](https://github.com/utkukose)

</div>

---

> **Dil hakkında:** Depodaki not defterleri, istem kütüphanesi ve şablonlar uluslararası
> erişilebilirlik gerekçesiyle İngilizce yayımlanmaktadır. Ders metni her iki dilde de
> mevcuttur ve bu sayfa, atölyeyi Türkçe takip etmek isteyen katılımcılar için gerekli
> bağlamı içermektedir. İngilizce sürüm için [README.md](README.md) dosyasına bakınız.

## Bu depo nedir

Bu depo, yapay zekâ tabanlı klinik karar destek sistemleri üzerine birbirine bağlı iki
oturumun materyalini içermektedir. Birincisi, bu sistemlerin ne olduğunu, sahada neden
başarısız olduklarını ve güvenilirliği neyin belirlediğini ele alan kırk beş dakikalık bir
derstir. İkincisi, katılımcıların üretken yapay zekâ araçlarını kullanarak kendi klinik
problemleri için çalışan bir karar destek prototipi geliştirdiği iki saatlik bir atölye
çalışmasıdır.

İki oturum tek bir argüman olarak tasarlanmıştır. Ders bir değerlendirme ölçütleri kümesi
sunmakta, atölye ise bu ölçütlerin her birini bir isteme (prompt) dönüştürmektedir.

**Atölye önceden Python bilgisi ve kurulum gerektirmemektedir.** Tüm çalışma tarayıcı
üzerinden Google Colab ortamında yürütülmektedir.

---

## Birinci oturum — Ders, 16 Eylül 2026, 16.00-16.45

**Yapay Zekâ Tabanlı Klinik Karar Destek Sistemleri**

Ders, bağımsız olarak doğrulanmış bir başarısızlık vakası üzerine kurulmuştur. Yüzlerce
hastanede kullanılan Epic Sepsis Model, 38.455 yatış üzerinde dış doğrulamaya tabi
tutulmuş ve üreticinin 0,76-0,83 aralığındaki iddiasına karşılık 0,63 eğri altı alan ile
yüzde 12 pozitif kestirim değeri vermiştir. Üç yıl sonra 145.885 acil servis başvurusu
üzerinde yapılan ikinci doğrulamada duyarlılık yüzde 14,7 olarak bulunmuştur. Bu iki
çalışmadan atölyeye doğrudan taşınan üç ders çıkarılmaktadır: Dış doğrulama seçimlik
değildir, pozitif kestirim değeri yerel prevalans bilinmeden yorumlanamaz ve gereğinden sık
tetiklenen bir sistem kendi başına zarar üretir.

Dersin kalan bölümleri kalibrasyon ile ayrım gücü ayrımını, açıklanabilirliğin ne verip ne
vermediğini, bir iddiayı denetlenebilir kılan raporlama standartlarını ve Eylül 2026
itibarıyla Avrupa Birliği, Amerika Birleşik Devletleri ile Türkiye'deki düzenleyici
konumu ele almaktadır.

Ders metinleri `lecture/` klasöründedir. Düz metin olarak yazıldıkları için NotebookLM ya
da benzeri bir araçta doğrudan kaynak dosya olarak kullanılıp sunuma dönüştürülebilirler.
Metinlerdeki her sayı, tarih ve atıf `lecture/verified-sources.md` dosyasında birincil
kaynağına kadar izlenmektedir.

---

## İkinci oturum — Atölye, 18 Eylül 2026, 09.00-11.00

**Üretken Yapay Zekâ Araçları ile Klinik Karar Destek Sistemleri Geliştirilmesi**

Atölye, yedi istemde bir karar destek sistemi kurma mantığı üzerine tasarlanmıştır.
Katılımcılar ortak bir senaryo ile başlamakta, yaklaşık bir saat sonra aynı istem zincirini
kendi klinik problemlerine geçirmektedir. Verisi olmayan katılımcılar problemlerine uygun
bir sentetik kohort üretmekte, gerçek veri ile çalışmak isteyenler ise kimlik doğrulaması
gerektirmeyen açık veri kümelerini kullanmaktadır.

| Saat | Modül | Ne yapılıyor |
|---|---|---|
| 00:00 | Yönlendirme | Colab açılıyor, iki şerit anlatılıyor, ortak senaryo tanıtılıyor |
| 00:10 | Kart | Yedi soru cevaplanıyor ve yazılı bir belirtime dönüştürülüyor |
| 00:25 | Veri | İkinci istem kohortu üretiyor ya da açık veriyi yüklüyor, veri türüne göre dallanıyor |
| 00:45 | Temel model ve değerlendirme | Üçüncü ve dördüncü istemler model ve dürüst bir değerlendirme raporu üretiyor |
| 01:05 | **Ayrışma** | Her katılımcı kendi kartını aynı zincire yerleştiriyor |
| 01:20 | Açıklanabilirlik | Beşinci istem modeli açıklıyor, ardından kendi açıklamasını eleştiriyor |
| 01:35 | Güvenlik ve yönetişim | Altıncı ve yedinci istemler çekimserlik ekliyor, model kartı ve düzenleyici triyaj üretiyor |
| 01:50 | Gösterim ve kapanış | Tek hücrelik arayüz, üç çıktının sunumu, kapanış tartışması |

### Dört veri yolu

İstem kütüphanesi her istemin her veri türü için ayrı bir sürümünü içermektedir. Böylece
farklı problemler üzerinde çalışan katılımcılar aynı sırayı takip edebilmektedir.

| Yol | Tipik problem | Atölyede kullanılan veri |
|---|---|---|
| Rutin hastane verisi | Kötüleşme riski, yeniden yatış, triyaj önceliği | MIMIC-IV demo veri kümesi ya da üretilen kohort |
| Tıbbi görüntü | Lezyon tespiti, tarama triyajı | MedMNIST ya da üretilen görüntü kümesi |
| Fizyolojik zaman serisi | Aritmi tespiti, monitör alarmları | MIMIC-IV-ECG demo ya da üretilen sinyal kümesi |
| Klinik metin | Rapor sınıflandırma, bilgi çıkarımı | Katılımcının belirtimine göre üretilen sentetik notlar |

---

## Katılımcı olarak nasıl hazırlanılır

`templates/cdss-canvas.md` dosyasındaki yedi soruyu, önemsediğiniz bir klinik problem için
oturumdan önce cevaplayınız. Yanınızda yalnızca bu cevapları getirmeniz yeterlidir. Yedi
soru şunlardır:

- Hangi klinik karar hedefleniyor; sistem tam olarak hangi anda devreye girecek?
- Sistemi kim kullanacak; hekim, hemşire, teknisyen ya da doğrudan hasta mı?
- Hangi veri türü kullanılacak; rutin hastane verisi, tıbbi görüntü, fizyolojik zaman serisi ya da klinik metin mi?
- Sonuç değişkeni nedir; nasıl ve hangi zaman penceresinde ölçülüyor?
- Hedeflenen durumun kendi hasta grubunuzdaki prevalansı nedir?
- Hangi hata daha pahalıdır; kaçırma mı yoksa yanlış alarm mı?
- Sistem yanılırsa ne olur; zarar senaryosu ve devretme kuralı nedir?

---

## Defterler

Defterlerin tamamı tarayıcıda Google Colab üzerinde çalışmaktadır. Kurulum gerekmemekte,
hiçbir veri kümesi önceden indirilmemektedir.

| | Defter | İçerik |
|---|---|---|
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/NB1_CDSS_Canvas.ipynb) | **NB1** Kart | Yedi soruyu belirtim istemine çeviren defter, iki dilde |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/NB2_Data_MIMIC_Web.ipynb) | **NB2** Veri | MIMIC-IV demo verisinin PhysioNet'ten çağrılması ve ortak kohortun kurulması |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/NB3_Baseline_and_Evaluation.ipynb) | **NB3** Temel model | Hasta düzeyinde ayrım, sızıntıya kapalı zincir ve dürüst değerlendirme raporu |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/NB4_Explainability.ipynb) | **NB4** Açıklanabilirlik | Küresel önem, kesin yerel katkılar ve açıklamanın eleştirisi |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/NB5_Safety_and_Governance.ipynb) | **NB5** Güvenlik | Çekimserlik, dağılım kayması, girdi doğrulama, kırmızı takım, yönetişim belgeleri |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/NB6_Ship_a_Demo.ipynb) | **NB6** Demo | Tamamlanan prototipin web'den çağrılabilen arayüzü |

NB3 ve sonrası temel modeli tek bir `pipeline.prepare()` çağrısıyla yeniden kurmaktadır;
defterler NB2'den sonra bağımsız olarak ve istenen sırayla çalıştırılabilmektedir.

---

## Önemli uyarı

Bu depodaki hiçbir materyal doğrulanmış bir klinik araç değildir. Atölyede üretilen
prototipler öğretim amaçlı yapıtlardır. Bunlardan herhangi birinin gerçek hasta verisi
üzerinde kullanılması ya da bir bakım ortamına alınması, dersin anlattığı bütün
mekanizmayı gerektirir: Dış doğrulama, kalibrasyon değerlendirmesi, alt grup analizi,
düzenleyici sınıflandırma ve devreye alma sonrası izleme.

---

## Lisans

Materyal, Creative Commons Atıf-GayriTicari-AynıLisanslaPaylaş 4.0 Uluslararası lisansı ile
yayımlanmaktadır. Atıf verilerek öğretim ve araştırma amacıyla paylaşılabilir ve uyarlanabilir;
izin alınmadan ticari olarak kullanılamaz veya satılamaz.

---

## Teşekkür

Bu oturumlar, TÜBİTAK destekli Teknoloji ve Yapay Zekâ Okuryazarlığı Eğitimi projesi
kapsamında Akdeniz Üniversitesi ev sahipliğinde gerçekleştirilmiştir. Davet ve organizasyon
için proje yürütücülerine ve düzenleme kuruluna, atölyenin ayrışma aşamasını biçimlendiren
klinik sorularıyla katılımcılara teşekkür edilmektedir.

---

<div align="center">

**Prof. Dr. Utku Köse**

Süleyman Demirel Üniversitesi, Bilgisayar Mühendisliği Bölümü
Yapay Zekâ Uygulama ve Araştırma Merkezi (YAZEM) Müdürü
Isparta, Türkiye

[utkukose@sdu.edu.tr](mailto:utkukose@sdu.edu.tr) · [www.utkukose.com](https://www.utkukose.com) · [ORCID 0000-0002-9652-6415](https://orcid.org/0000-0002-9652-6415) · [github.com/utkukose](https://github.com/utkukose)

</div>
