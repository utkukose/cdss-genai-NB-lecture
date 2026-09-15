# Anti-patterns · Üretken yapay zekânın klinik kodda yaptığı hatalar

Bu liste, atölye sırasında üretilen kodu denetlerken kullanılacak referanstır. Her madde
gerçekte karşılaşılan bir hata biçimidir ve hepsinin ortak özelliği şudur: Kod çalışır,
hata vermez ve okunduğunda doğru görünür.

Defterlerdeki kontrol hücreleri ve istemlerin sonundaki kabul ölçütleri bu listedeki
hataları yakalamak için tasarlanmıştır. Liste, kontrollerin neden o noktalara baktığını
açıklamaktadır.

---

## 1. Uydurulmuş klinik eşik

**Ne oluyor.** Model, kaynağı olmayan bir kesme değerini kendinden emin bir dille koda
yazmaktadır. Laktat için 2 mmol/L, kreatinin için 1,2 mg/dL, SOFA için 2 puanlık artış
gibi değerler kimi zaman doğrudur, kimi zaman yakındır ve kimi zaman tamamen uydurmadır.
Üçü de aynı üslupla gelmektedir.

**Neden tehlikeli.** Doğru olanlarla uydurma olanlar biçimsel olarak ayırt edilememektedir.
Kod yorumunda "standart klinik eşik" yazması, o eşiğin var olduğu anlamına gelmemektedir.

**Nasıl yakalanır.** Üretilen koddaki her sayının kaynağı sorulur. Kaynağı olmayan
değerler kodda `KAYNAKSIZ` olarak işaretlenir ve klinik olarak doğrulanana kadar öyle
kalır.

**Örnek.**

```python
# Modelin ürettiği hâli
LACTATE_THRESHOLD = 2.0  # standard clinical cutoff for sepsis

# Denetimden sonraki hâli
LACTATE_THRESHOLD = 2.0  # UNSOURCED: doğrula. Sepsis-3'te laktat >2 mmol/L septik şok
                         # tanımının bir bileşenidir, ancak burada farklı bir amaçla
                         # ve farklı bir popülasyonda kullanılıyor.
```

---

## 2. Sessiz sızıntı: Ayrımdan önce öğrenilen ön işleme

**Ne oluyor.** Ölçekleyici, tamamlayıcı veya kodlayıcı, eğitim ve test ayrımı yapılmadan
önce verinin tamamı üzerinde çalıştırılmaktadır. Test kümesindeki değerlerin ortalaması
ya da ortancası eğitim sürecine taşınmaktadır.

**Neden tehlikeli.** Hiçbir uyarı vermemektedir. Başarımı yükseltmekte ve kod okunduğunda
adım sırası mantıklı görünmektedir.

**Nasıl yakalanır.** Ön işlemenin tamamı bir `Pipeline` içine alınır; böylece hata yapısal
olarak imkânsız hâle gelir. NB3'teki model kontrolü Pipeline kullanılıp kullanılmadığını
denetler.

**Örnek.**

```python
# Sızıntılı
X = SimpleImputer().fit_transform(X)
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Doğru
X_train, X_test, y_train, y_test = train_test_split(X, y)
pipe = Pipeline([("impute", SimpleImputer()), ("scale", StandardScaler()), ("clf", model)])
pipe.fit(X_train, y_train)
```

---

## 3. Hedef sızıntısı: Sonucun bir sonucu öznitelik oluyor

**Ne oluyor.** Tahmin edilmek istenen sonucun ardından kaydedilen bir değişken modele
girdi olarak verilmektedir. Sepsis modeline antibiyotik istemi, yoğun bakım devri
modeline yoğun bakım yatak numarası, mortalite modeline taburculuk tipi girmesi gibi.

**Neden tehlikeli.** Başarım olağanüstü yükselmektedir ve bu yükselme ilk bakışta bir
başarı gibi görünmektedir. Model sahaya alındığında ise o değişken karar anında henüz
mevcut olmadığı için sistem çalışmamaktadır.

**Nasıl yakalanır.** Her öznitelik için tek bir soru sorulur: Karar anında bu değer kayıtta
var mıydı? NB2'deki kabul ölçütleri bunu zorunlu kılar. Atölyenin veri modülünde
altı saatlik zaman penceresi ve `los`, `outtime`, `last_careunit` sütunlarının silinmesi
bu nedenledir.

**Belirti.** Eğri altı alan 0,95 üzerindeyse ve klinik problem gerçekten zorsa, önce
sızıntı aranır. Klinik tahmin problemlerinde bu değer neredeyse her zaman bir hatanın
işaretidir.

---

## 4. Hasta düzeyinde değil satır düzeyinde ayrım

**Ne oluyor.** Aynı hastanın birden fazla kaydı bulunduğunda, `train_test_split`
varsayılan olarak satırları rastgele ayırmakta ve aynı hastanın bir kaydı eğitime,
diğeri teste düşmektedir.

**Neden tehlikeli.** Model hastayı tanımaktadır. Test başarımı yükselmekte ve bu yükselme
yeni bir hastada tekrarlanmamaktadır.

**Nasıl yakalanır.** Hasta kimliği ayrım grubu olarak verilir: `GroupShuffleSplit` ya da
`StratifiedGroupKFold`. Model bunu kendiliğinden yapmamaktadır; açıkça istenmelidir.

Aynı hata zaman serisinde pencere düzeyinde, görüntüde ise aynı hastanın farklı kesitleri
düzeyinde ortaya çıkmaktadır.

---

## 5. Halüsinasyon kaynak

**Ne oluyor.** Var olmayan bir makaleye, kılavuza veya standarda atıf yapılmaktadır. Yazar
adları gerçek, dergi gerçek, yıl makul ve biçim kusursuzdur.

**Neden tehlikeli.** Biçimsel doğruluk, içerik doğruluğu izlenimi vermektedir. Bir model
kartına ya da makaleye geçtiğinde düzeltilmesi zordur.

**Nasıl yakalanır.** Her atıf için DOI ya da resmî belge numarası istenir. DOI verilemiyorsa atıf kaldırılmaktadır. Verilen DOI ise
açılarak kontrol edilmektedir; doi.org üzerinden çözülmeyen bir numara yoktur.

---

## 6. Doğruluğun başlık sayı olarak sunulması

**Ne oluyor.** Dengesiz bir klinik problemde doğruluk raporlanmaktadır.

**Neden tehlikeli.** Yüzde 7 prevalansta her zaman olumsuz sınıfı söyleyen bir kural yüzde
93 doğruluk vermektedir. Doğruluk bu durumda modelin ne yaptığını değil, hastalığın ne
kadar nadir olduğunu ölçmektedir.

**Nasıl yakalanır.** Boş karşılaştırma her raporda bulunmalıdır. Değerlendirme modülündeki
`null_comparison` bunu yapmaktadır.

---

## 7. Kalibrasyonun hiç raporlanmaması

**Ne oluyor.** Eğri altı alan raporlanmakta, kalibrasyon atlanmaktadır.

**Neden tehlikeli.** Klinik kararda bir eşik belirleniyorsa, modelin verdiği olasılığın
gerçekliğe karşılık gelmesi gerekmektedir. Aşırı güvenli bir model, klinisyenin seçtiği
eşiği sandığından farklı bir yere oturtmaktadır.

**Nasıl yakalanır.** Kalibrasyon eğrisi ve eğimi istenmektedir. Eğim birin belirgin
altındaysa model aşırı güvenlidir.

---

## 8. Alt grup dökümünün atlanması ya da uydurulması

**Ne oluyor.** İki hata biçimi bulunmaktadır. Birincisi alt grup analizinin hiç
yapılmamasıdır. İkincisi, sekiz hastalık bir alt grup için üç haneli hassasiyetle bir
duyarlılık değeri raporlanmasıdır.

**Neden tehlikeli.** İkinci hata birincisinden daha tehlikelidir, çünkü denetlenmişlik
görüntüsü vermektedir. Bir slaytta ya da model kartında sekiz hastadan çıkan sayı ile
sekiz yüz hastadan çıkan sayı aynı otoriteyi taşımaktadır.

**Nasıl yakalanır.** Örneklem eşiği önceden belirlenir ve altında kalan gruplar için sayı
yerine "yetersiz örneklem" yazılır. Değerlendirme modülü bunu yapmaktadır. Bu ifade bir
eksiklik değil, bir bulgudur: Hiç test edilmemiş bir grup için sistemin adil olduğu
gösterilemez.

---

## 9. Nokta tahminin güven aralığı olmadan sunulması

**Ne oluyor.** Eğri altı alan 0,78 olarak raporlanmakta, aralık verilmemektedir.

**Neden tehlikeli.** Küçük kohortlarda aralık 0,5 değerini içerebilmektedir. Bu durumda
model şanstan ayırt edilememektedir ve nokta tahmin bu gerçeği gizlemektedir.

**Nasıl yakalanır.** Her başarım değeri aralığıyla birlikte istenir. Değerlendirme
modülündeki `bootstrap_auc` bunu üretmektedir.

---

## 10. Düzenleyici sorularda kendinden emin icat

**Ne oluyor.** Bir yazılımın tıbbi cihaz sayılıp sayılmadığı ya da hangi uyum tarihine
tabi olduğu sorulduğunda, kesin ve eski bilgi verilmektedir.

**Neden tehlikeli.** Bu alandaki tarihler Temmuz 2026'da değişmiştir. AB 2026/1744 sayılı
Dijital Omnibus düzenlemesi, Ek I kapsamındaki gömülü sistemler için uyum tarihini
2 Ağustos 2028'e ertelemiştir. Pek çok asistan hâlâ eski takvimi döndürecek kadar yeni bir
değişikliktir.

**Nasıl yakalanır.** NB5'te üretilen düzenleyici triyaj notu ayrıca denetlenir. Her
düzenleyici iddia için güven düzeyi ve bir hukukçunun kontrol etmesi gereken nokta
istenir.

---

## Denetim sırası

Üretilen her kod parçası için aşağıdaki sıra izlenmektedir.

1. Üretilen koddaki bütün sabit sayıları listeletiniz.
2. Listeyi okuyunuz ve kaynağı olmayanları işaretleyiniz.
3. Ayrımın nerede yapıldığını kendi gözünüzle bulunuz.
4. Öznitelik listesini karar anına göre süzünüz.
5. Varsa atıfları doi.org üzerinden açınız.
6. Ancak bundan sonra sonuçlara bakınız.

Sonuçlar en sona bırakılır. İyi görünen bir sayı görüldükten sonra, arkasındaki hatayı
aramak belirgin biçimde zorlaşır.
