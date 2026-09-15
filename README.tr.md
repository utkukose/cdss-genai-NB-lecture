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

İki oturum tek bir argüman olarak tasarlanmıştır. Ders, böyle bir sistemin kurulduğu on üç
aşamayı ve her aşamanın hangi ölçütle değerlendirildiğini ortaya koyar; atölye aynı
aşamaları defter defter yürür.

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

## Katılımcı olarak nasıl hazırlanılır

Hazırlık gerekmez. Oturuma bir tarayıcı ve bir üretken yapay zekâ aracı hesabıyla
geliniz; kullandığınız araç fark etmez.

Bir hazırlık yapmak isterseniz iki dakikalık bir iş vardır: `notebooks/tr/` klasöründeki
NB1 defterini açıp veri kümesi kataloğuna bakınız ve hangi kümeyle ilerleyeceğinize karar
veriniz. Kendi klinik probleminiz varsa ve kataloğun dışına çıkmak istiyorsanız, o
problemi tek cümleyle yazılı hâlde getiriniz.

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
