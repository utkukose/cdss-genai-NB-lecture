# CDSS Canvas · Karar Destek Kartı

Bu kartı atölyeden önce kendi klinik probleminiz için doldurunuz. Cevaplar, atölyede
yazılacak her istemin girdisidir. Doldurulmuş kartın tamamı her isteme `{{CANVAS}}`
yerine yapıştırılır, özetlenmez.

Complete this card for your own clinical problem before the workshop. The answers are the
input to every prompt in the session. The whole completed card is pasted in place of
`{{CANVAS}}`, never summarised.

---

## Nasıl doldurulur · How to complete it

Yedi sorunun tamamı cevaplanmalıdır. Bir soruyu cevaplayamıyorsanız bu, sistemin
tasarlanamayacağı anlamına gelmez; o sorunun atölyede birlikte çalışılacak nokta olduğu
anlamına gelir. Boş bırakmak yerine "bilmiyorum, şu sebeple" yazınız.

Üç uyarı. Beşinci soruya tahmini bir sayı yazmak, hiç yazmamaktan iyidir; ama tahmin
olduğunu belirtiniz. Altıncı soruda iki hatayı da eşit derecede pahalı bulduğunuzu
düşünüyorsanız, muhtemelen kararın klinik sonucunu henüz yeterince düşünmemişsinizdir.
Yedinci soru en sık atlanan ve en çok önem taşıyan sorudur.

---

## Kart · The card

### 1. Hangi klinik karar? · Which clinical decision?

Sistemin hedeflediği karar ve tam olarak hangi anda devreye gireceği.

> *Cevabınız:*

---

### 2. Kim kullanacak? · Who will use it?

Hekim, hemşire, teknisyen ya da doğrudan hasta. Kullanıcının o anda ne yapmakta olduğu.

> *Cevabınız:*

---

### 3. Hangi veri türü? · Which type of data?

Rutin hastane verisi, tıbbi görüntü, fizyolojik zaman serisi ya da klinik metin. Birden
fazla ise hangisinin ana kaynak olduğu. Bu cevap, atölyede hangi veri yolunu izleyeceğinizi
belirlemektedir.

> *Cevabınız:*

---

### 4. Sonuç değişkeni nedir? · What is the outcome?

Tahmin edilecek sonucun kesin tanımı, zaman penceresi ve rutin kayıtlarda nasıl tespit
edileceği. "Kötüleşme" bir sonuç değişkeni değildir; "kabulden sonraki 48 saat içinde
yoğun bakıma devir" bir sonuç değişkenidir.

> *Cevabınız:*

---

### 5. Prevalans ne? · What is the prevalence?

Hedeflenen durumun kendi hasta grubunuzdaki sıklığı. Kesin bilmiyorsanız tahmininizi ve
neye dayandığını yazınız. Bu sayı olmadan pozitif kestirim değeri yorumlanamamaktadır.

> *Cevabınız:*

---

### 6. Hangi hata daha pahalı? · Which error is more costly?

Kaçırma mı, yanlış alarm mı? Cevabı klinik sonucuyla birlikte yazınız. Bu cevap, atölyede
eşiğin hangi yönde seçileceğini belirlemektedir.

> *Cevabınız:*

---

### 7. Sistem yanılırsa ne olur? · What happens when it is wrong?

Somut bir zarar senaryosu ve devretme kuralı. Hangi durumda karar insana geçer?

> *Cevabınız:*

---

## Worked example · Örnek doldurulmuş kart

Atölyenin ortak senaryosu bu kart doldurularak kurulmuştur. Kendi cevaplarınızın bu
ayrıntı düzeyinde olması yeterlidir.

**1. Hangi klinik karar?**
Yoğun bakıma kabul edilen bir hastanın uzun süre kalıp kalmayacağının erken öngörülmesi.
Sistem, kabulden altı saat sonra devreye girmekte ve yatak kapasitesi planlaması ile
erken yükseltme kararına girdi sağlamaktadır.

**2. Kim kullanacak?**
Yoğun bakım sorumlu hekimi ve yatak yönetiminden sorumlu hemşire. Sabah viziti sırasında,
hasta listesi gözden geçirilirken.

**3. Hangi veri türü?**
Rutin hastane verisi. Demografik bilgi, yatış bağlamı ve ilk altı saatin vital bulguları
ile laboratuvar sonuçları.

**4. Sonuç değişkeni nedir?**
Yoğun bakım yatış süresinin üç günü aşması. Yatış ve çıkış zamanlarından hesaplanmakta,
rutin kayıtlarda doğrudan mevcuttur.

**5. Prevalans ne?**
Bu kohortta yaklaşık üçte bir. Kendi biriminizde farklı olacaktır; kendi rakamınızı
kullanınız.

**6. Hangi hata daha pahalı?**
Kaçırma. Uzun kalacak bir hastanın öngörülmemesi, kapasitenin plansız dolmasına ve başka
bir hastanın kabulünün gecikmesine yol açmaktadır. Yanlış alarmın maliyeti ise gereksiz
bir planlama toplantısıdır. Eşik bu nedenle duyarlılıktan seçilmektedir.

**7. Sistem yanılırsa ne olur?**
Yanlış negatif durumunda kapasite planı yetersiz kalmakta ve devir kararı gecikmektedir.
Devretme kuralı şudur: Sistem çekimser kaldığında ya da hasta eğitim popülasyonuna
benzemediğinde karar sorumlu hekime geçmekte, sistem çıktısı gösterilmemektedir.

---

## Kartın ilk kullanımı · First use of the card

Doldurulmuş kartı, istem kütüphanesindeki birinci istemin içine yapıştırınız. O istem
kart üzerinden bir belirtim üretmekte ve kalan altı istem o belirtimi kullanmaktadır.

Birinci istem, cevaplarınızın eksik ya da kendi içinde tutarsız olduğu yerleri size
bildirecek biçimde yazılmıştır. O listeyi okuyunuz. Kartınızın zayıf noktaları,
kuracağınız sistemin zayıf noktalarıdır.
