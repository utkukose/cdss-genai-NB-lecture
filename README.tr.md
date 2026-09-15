<div align="center">

# Üretken Yapay Zekâ ile Klinik Karar Destek Sistemleri

### Ders ve Atölye Materyali

*Sağlık Bilimlerinde Teknoloji ve Yapay Zekâ Okuryazarlığı Eğitimi*
*Akdeniz Üniversitesi, Antalya · 16 ve 18 Eylül 2026*

[![Lisans](https://img.shields.io/badge/Lisans-CC%20BY--NC--SA%204.0-0E7C7B.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.tr)
[![Colab](https://img.shields.io/badge/NB1'i%20Colab'da%20a%C3%A7-C2185B.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/NB1_CDSS_Canvas.ipynb)
[![English](https://img.shields.io/badge/Full%20material-English-6B7590.svg)](README.md)

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

> **Dil hakkında:** Materyal, birbirinden bağımsız iki tam takım hâlinde hazırlanmıştır.
> Bu sayfa Türkçe takıma yönlendirir; İngilizce takım için [README.md](README.md)
> dosyasına bakınız. İki takım birbirine atıf yapmaz ve katılımcı birini baştan sona
> takip eder.

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

## Birinci oturum — Ders, 16 Eylül 2026

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

## İkinci oturum — Atölye, 18 Eylül 2026

**Üretken Yapay Zekâ Araçları ile Klinik Karar Destek Sistemleri Geliştirilmesi**

Atölye, yedi istemde bir karar destek sistemi kurma mantığı üzerine tasarlanmıştır.
Katılımcılar ortak bir senaryo ile başlamakta, yaklaşık bir saat sonra aynı istem zincirini
kendi klinik problemlerine geçirmektedir. Verisi olmayan katılımcılar problemlerine uygun
bir sentetik kohort üretmekte, gerçek veri ile çalışmak isteyenler ise kimlik doğrulaması
gerektirmeyen açık veri kümelerini kullanmaktadır.

| Defter | Ne yapılıyor |
|---|---|
| NB1 | Yedi soru cevaplanıyor ve yazılı bir belirtime dönüştürülüyor |
| NB2 | Açık veriden kohort kuruluyor, veri türüne göre dallanıyor |
| NB3 | Temel model ve asıl önemlisi dürüst bir değerlendirme raporu |
| **Ayrışma** | Her katılımcı kendi kartını aynı zincire yerleştiriyor |
| NB4 | Model açıklanıyor, ardından açıklamanın kendisi eleştiriliyor |
| NB5 | Çekimserlik ve bariyerler, sonra model kartı ile düzenleyici triyaj |
| NB6 | Web üzerinden çalışan arayüz ve kapanış tartışması |

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

`templates/tr/cdss-canvas.md` dosyasındaki yedi soruyu, önemsediğiniz bir klinik problem için
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

## Ders materyali

| | Belge | Dil |
|---|---|---|
| [PDF](lecture/KKDS-ders-notlari-TR.pdf) | Ders notlari, gorsellerle birlikte tam kaynak metin | Turkce |
| [PDF](lecture/CDSS-lecture-notes-EN.pdf) | Lecture notes, ayni metnin Ingilizce surumu | Ingilizce |
| [PDF](slides/KKDS-ders-sunumu-TR.pdf) | Sunum dosyasi | Turkce |
| [PDF](slides/CDSS-lecture-slides-EN.pdf) | Presentation deck | Ingilizce |

Ders notlari duz metin olarak yazilmistir; NotebookLM ya da benzeri bir araca dogrudan
kaynak dosya olarak verilebilir. `slides/` klasorundeki sunumlar bu metinlerden uretilmekte
ve oturumdan sonra eklenmektedir. Metindeki her sayi, tarih ve atif
[lecture/verified-sources.md](lecture/verified-sources.md) dosyasinda birincil kaynagina
kadar izlenmektedir.

---

## Defterler

Materyal birbirinden bağımsız iki tam takım hâlindedir. Bu sayfa Türkçe takıma yönlendirir;
İngilizce takım için [README.md](README.md) dosyasına bakınız.

| | Defter | Eklenen katman |
|---|---|---|
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB1_Veriye_Ulasmak.ipynb) | **NB1** Veriye ulaşmak | Hazırlık, veriyi getirme, ilk bakış |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB2_Veriyi_Hazirlamak.ipynb) | **NB2** Veriyi hazırlamak | Temizleme, hasta düzeyinde ayrım, modele uygun biçime çevirme |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB3_Model_Kurmak_ve_Olcmek.ipynb) | **NB3** Model kurmak ve ölçmek | Model, tahmin ve dokuz değerli dürüst ölçüm |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB4_Karari_Gerekcelendirmek.ipynb) | **NB4** Kararı gerekçelendirmek | Genel ve hasta düzeyinde gerekçe, gerekçenin eleştirisi |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB5_Guvenlik_ve_Uyumluluk.ipynb) | **NB5** Güvenlik ve uyumluluk | Üç bariyer, kırmızı takım, ekrana basılan uyumluluk raporu |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/tr/NB6_Web_Arayuzu.ipynb) | **NB6** Web arayüzü | Tarayıcıdan çalışan arayüz ve programın tamamı |

### Defterler nasıl çalışıyor

**Python bilmeniz gerekmez ve kodu siz yazmazsınız.** Her adımda sade bir klinik dille
yazılmış bir istem verilir. İstemi bir üretken yapay zekâ aracına aktarır, aracın verdiği
kodu istemin altındaki boş hücreye yapıştırıp çalıştırırsınız.

Her istemin sonunda BEKLENEN SONUÇ başlıklı bir bölüm bulunur; kodun ne üretmesi gerektiğini
yazar. Ardından gelen kontrol hücresi tam olarak bunu sınar ve eksik varsa bildirir. Bildirimi
yapay zekâ aracına geri verir, kodu yeniden ürettirirsiniz. İlk denemede tutmaması olağandır.

Kodu anlamanız beklenir ve her adımdan sonra kısa bir Python notu gelir. Notlar hiçbir ön
bilgi varsaymaz; az önce gördüğünüz yapıyı açıklar: Kütüphane nedir, tablo nedir, fonksiyon
ve açıklama metni nedir, ekrana yazmak ile geri vermek arasındaki fark, sözlük, döngü,
nesne ve yöntem, erken dönüş, geri çağrı.

### Kod defterden deftere taşınır

Her yapıştırma hücresinin ilk satırında `#@cdss adim_adi` yazar. Defterin sonunda
`kit.export()` işaretli bütün hücreleri tek bir blok hâlinde toplar. O bloğu bir sonraki
defterin ilk hücresine yapıştırırsınız; böylece yazdığınız program birikerek ilerler. Bir
adımı düzeltip yeniden çalıştırdığınızda eski sürümün yerini yenisi alır.

NB6'nın sonunda biriken kod, web arayüzü arkasında çalışan eksiksiz bir klinik karar destek
sistemidir ve `cdss_sistem.py` adıyla kaydedilir.

### Size verilen tek şey

`workshop/cdss_kit.py` modülü. Kodu taşır ve kontrolleri çalıştırır. İçinde klinik karar
destek mantığı yoktur; onu siz yazarsınız.

**Bir koşul.** Defterler bu modülü `raw.githubusercontent.com` üzerinden çeker, dolayısıyla
deponun herkese açık olması gerekir. Özel bir depoda çağrı 404 döner ve modülün Colab
oturumuna elle yüklenmesi gerekir.

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

Bu oturumlar, TÜBİTAK destekli Sağlık Bilimlerinde Teknoloji ve Yapay Zekâ Okuryazarlığı Eğitimi projesi
kapsamında Akdeniz Üniversitesi ev sahipliğinde gerçekleştirilmiştir. Davet ve organizasyon
için proje yürütücülerine ve düzenleme kuruluna, atölyenin ayrışma aşamasını biçimlendiren
klinik sorularıyla katılımcılara teşekkür edilmektedir.

---

<div align="center">

**Prof. Dr. Utku Köse**

Süleyman Demirel Üniversitesi, Bilgisayar Mühendisliği Bölümü<br>
Yapay Zekâ Uygulama ve Araştırma Merkezi (YAZEM) Müdürü<br>
Isparta, Türkiye

[utkukose@sdu.edu.tr](mailto:utkukose@sdu.edu.tr) · [www.utkukose.com](https://www.utkukose.com) · [ORCID 0000-0002-9652-6415](https://orcid.org/0000-0002-9652-6415) · [github.com/utkukose](https://github.com/utkukose)

</div>
