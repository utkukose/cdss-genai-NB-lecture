# Prompt Library · İstem Kütüphanesi

Seven prompts build a clinical decision support prototype. Every prompt is given in Turkish
and in English. Both versions are used during the session, and the difference between them
is itself part of the material.

Yedi istem ile bir klinik karar destek prototipi kurulmaktadır. Her istem Türkçe ve
İngilizce olarak verilmiştir. Oturumda her iki sürüm de kullanılmakta, aradaki fark ise
materyalin bir parçası olarak ele alınmaktadır.

---

## Two conventions · İki kural

`{{CANVAS}}` is replaced by the answers from `templates/cdss-canvas.md`, pasted in full
into every prompt rather than summarised. Repetition keeps the generated code anchored to
the actual clinical problem instead of drifting toward whatever is statistically typical.

`{{CANVAS}}` yerine `templates/cdss-canvas.md` dosyasındaki cevaplar konulmaktadır. Kart
her isteme tam olarak yapıştırılır, özetlenmez. Tekrar bilinçlidir: Her istem klinik
bağlamın tamamını gördüğü için üretilen kod gerçek probleme bağlı kalmaktadır.

**Prompt 0 is run after every single step and is not optional.** Generated clinical code
fails in ways that look correct.

**Sıfırıncı istem her adımdan sonra çalıştırılır ve seçimlik değildir.** Üretilen klinik
kod, doğru görünen biçimlerde hatalıdır.

---

## Language as a literacy question · Bir okuryazarlık konusu olarak dil

Aynı isteme Türkçe ve İngilizce sorulduğunda farklı çıktılar alınmaktadır. Bunun üç pratik
sebebi bulunmaktadır. Teknik kütüphane belgelerinin büyük çoğunluğu İngilizce olduğundan
kod üretimi İngilizce istemlerde genellikle daha tutarlıdır. Buna karşılık klinik bağlam,
hekimin kendi dilinde çok daha doğru ifade edilmektedir; Türkçe yazılmış bir vaka tanımı
İngilizceye çevrilirken incelik kaybedebilmektedir. Üçüncü olarak, Türkçe klinik terimler
zaman zaman yanlış eşlenmekte ve model, kastedilmeyen bir tanı ya da ölçüm için kod
üretebilmektedir.

**Önerilen kullanım:** Kart Türkçe doldurulur, teknik istem gövdesi İngilizce verilir.
Atölyede her iki saf sürüm de denenmekte ve sonuçlar karşılaştırılmaktadır.

### Built-in comparison exercise · Yerleşik karşılaştırma egzersizi

Üçüncü istemden sonra aşağıdaki adım uygulanmaktadır. Bu adım atölyenin okuryazarlık
omurgasıdır ve atlanmamalıdır.

1. Aynı kart ile üçüncü istemi önce Türkçe, sonra ayrı bir konuşmada İngilizce çalıştırınız.
2. İki çıktıyı şu dört başlıkta karşılaştırınız: Seçilen model, ön işleme adımları,
   uydurulmuş sayıların varlığı, klinik terimlerin doğru eşlenip eşlenmediği.
3. Farkları not ediniz. Hangi dilin hangi kısımda daha güvenilir olduğu, probleminize göre
   değişecektir.
4. Bulgunuzu kayda geçiriniz. Bu not, atölyeden çıkardığınız en taşınabilir çıktıdır.

Run prompt 3 twice, once in Turkish and once in English, in separate conversations. Compare
the model chosen, the preprocessing steps, the presence of invented numbers, and whether
clinical terms were mapped correctly. Record the finding. It is the most portable result of
the session.

---

# Prompt 0 — The challenge prompt · Sorgulama istemi

Her adımdan sonra, aynı konuşma içinde çalıştırınız.

### Türkçe

```
Bunu çalıştırmadan önce kendi çıktını aşağıdaki başlıklara göre denetle. Her maddeyi
genel ifadelerle değil, açıkça cevapla:

1. Bu kodda hangi sayıları sen uydurdun? Verdiğim veriden türetilmeyen her eşik,
   kesme değeri, normal aralık, sınıf ağırlığı ve hiperparametreyi listele ve her
   birinin nereden geldiğini yaz. Klinik bir değerin kaynağı yoksa bunu açıkça söyle
   ve kod içinde KAYNAKSIZ olarak işaretle.
2. Test kümesinden ya da sonuç değişkeninin kendisinden modele eğitim sırasında bilgi
   sızabileceği bir yol var mı? Yolu adım adım izle.
3. Bu özniteliklerden hangileri ancak sonuç gerçekleştikten ya da klinisyen tarafından
   zaten şüphelenildikten sonra kaydedilebilir?
4. Bu kod, verim hakkında sana söylemediğim hangi varsayımları yapıyor?
5. Herhangi bir makale, kılavuz ya da standarda atıf yaptıysan DOI ya da resmî belge
   numarasını ver. Veremiyorsan atfı kaldır.
6. Bu sistem, verinin geldiği hastane dışında bir hastanede en büyük olasılıkla hangi
   nedenle başarısız olur?
```

### English

```
Before I run this, audit your own output against the following, and answer each point
explicitly rather than in general terms:

1. Which numbers in this code did you invent? List every threshold, cut-off, normal
   range, class weight and hyperparameter that is not derived from the data I gave you,
   and state where each one came from. If a clinical value has no source, say so
   plainly and mark it in the code as UNSOURCED.
2. Is there any path by which information from the test set, or from the outcome
   itself, reaches the model during training? Trace it explicitly.
3. Which of the features could only be recorded after the outcome has already occurred
   or already been suspected by a clinician?
4. What does this code assume about my data that I did not tell you?
5. If you cited any paper, guideline or standard, give the DOI or the official
   document number. If you cannot, remove the citation.
6. What is the single most likely reason this system would fail in a hospital that is
   not the one the data came from?
```

Birinci madde uydurulmuş klinik eşikleri, ikinci madde sızıntıyı, beşinci madde
halüsinasyon kaynakları yakalamaktadır. Bu üçü derste anlatılan üç riskin doğrudan
karşılığıdır.

---

# Prompt 1 — Frame the system · Sistemi çerçevele

Kod üretmez. Yedi cevabı, kalan altı istemin kullanabileceği bir belirtime dönüştürür.

### Türkçe

```
Bir klinik karar destek sistemi tasarlamama yardım ediyorsun. Klinik bağlamım şu:

{{CANVAS}}

Yalnızca aşağıdaki bölümlerden oluşan bir belirtim belgesi üret, başka hiçbir şey yazma:

- Karar anı: Sistemin çıktı ürettiği tam an ve o anda kullanıcının ne yapmakta olduğu.
- Tahmin hedefi: Sonucun kesin tanımı, zaman penceresi ve rutin kayıtlarda nasıl
  tespit edileceği.
- Girdiler: Karar anında gerçekten erişilebilir olan değişkenler ile ancak sonradan
  erişilebilecek değişkenler ayrı ayrı. Bu ayrımda katı ol.
- Çalışma noktası: Belirttiğim prevalans ve kaçırma ile yanlış alarm arasındaki maliyet
  farkı göz önüne alındığında duyarlılık mı yoksa özgüllük mü öncelenmeli? Tek
  paragrafta gerekçelendir.
- Başarısızlık biçimleri: Bu sistemin bir hastaya zarar verebileceği üç somut yol.
- Kapsam dışı: Bu sistemin açıkça yapmadığı şeyler.

Cevaplarımın eksik ya da kendi içinde tutarsız olduğu yerlerde boşluğu kendin
doldurma; bunu söyle. Açık kalan soruları en sonda listele.
```

### English

```
You are helping design a clinical decision support system. Here is my clinical context:

{{CANVAS}}

Produce a specification document with these sections, and nothing else:

- Decision point: the exact moment in the clinical workflow at which the system
  produces output, and what the user is doing at that moment.
- Prediction target: a precise definition of the outcome, including the time window
  and how it would be identified in routine records.
- Inputs: the variables that would realistically be available at the decision point,
  separated from variables that would only be available afterwards. Be strict about
  this separation.
- Operating point: given the prevalence I stated and the relative cost of a miss
  versus a false alarm that I stated, state which of sensitivity or specificity should
  be favoured and why, in one paragraph.
- Failure modes: three specific ways this system could harm a patient.
- Out of scope: what this system explicitly does not do.

Where my answers are incomplete or internally inconsistent, say so instead of filling
the gap yourself. List the open questions at the end.
```

Son talimat göründüğünden önemlidir. Belirtim üretmesi istenen bir asistan, girdi yetersiz
olsa da bir belirtim üretecektir. Boşlukları görünür kılma zorunluluğu, sessiz bir icadı
açık bir soruya dönüştürmektedir.

---

# Prompt 2 — Data · Veri

Kartın üçüncü cevabına uyan sürümü seçiniz. Ortak senaryoda MIMIC-IV demo veri kümesi
doğrudan ağ üzerinden çekilmektedir ve bu adım `notebooks/NB2_Data_MIMIC_Web.ipynb`
içinde hazırdır. Aşağıdaki 2a sürümü, kendi problemine geçen ve elinde veri bulunmayan
katılımcılar içindir.

## 2a. Routine hospital data · Rutin hastane verisi

### Türkçe

```
Yukarıdaki belirtimi kullanarak, bu problem için sentetik bir hasta kohortu üreten tek
bir Colab hücresi yaz.

Gereksinimler:
- Değişkenler, birimler ve makul aralıklar genel bir klinik veri kümesine değil,
  belirtime uymalı.
- Sonuç prevalansı belirtimde yazan değer olmalı.
- Gerçekçi eksik veri içermeli. Hangi eksiklik mekanizmasını uyguladığını ve neden
  seçtiğini yaz.
- Bir yordayıcı ile sonuç arasındaki ilişkinin gerçekten farklılaştığı en az bir
  demografik alt grup içersin; böylece ilerideki alt grup analizinin bulacağı bir şey
  olsun. Hangi alt grup ve hangi yordayıcı olduğunu söyle ki analizin bunu geri bulup
  bulmadığını kontrol edebileyim.
- Sonuç gerçekleştikten sonra kaydedilebilecek hiçbir değişken bulunmasın.
- Boyutu, sonuç oranını ve beş satırlık örneği yazdır.

Hücrenin başına, bu verinin eğitim amacıyla üretilmiş sentetik veri olduğunu ve klinik
olarak yorumlanmaması gerektiğini belirten tek cümlelik bir yorum bloğu ekle.
```

### English

```
Using the specification above, write a single Colab cell that generates a synthetic
patient cohort for this problem.

Requirements:
- The variables, units and plausible ranges must match the specification, not a generic
  clinical dataset.
- The outcome prevalence must be the value stated in the specification.
- Include realistic missingness. State the missingness mechanism you implemented and
  why you chose it.
- Include at least one demographic subgroup in which the relationship between a
  predictor and the outcome genuinely differs, so that a subgroup analysis later has
  something to find. Tell me which subgroup and which predictor.
- Do not include any variable that would only be recorded after the outcome.
- Print the shape, the outcome rate, and a five row sample.

Add a comment block at the top stating in one sentence that this is synthetic data
generated for teaching and must not be interpreted clinically.
```

## 2b. Medical imaging · Tıbbi görüntü

### Türkçe

```
Yukarıdaki belirtimi kullanarak, bu probleme uygun bir MedMNIST alt kümesini yükleyen;
uygun bir MedMNIST koleksiyonu yoksa kontrol edilebilir sinyal içeren sentetik bir
görüntü kümesi üreten tek bir Colab hücresi yaz.

Gereksinimler:
- Sınıf dengesini raporla ve belirtimdeki prevalansa yeniden ağırlıklandırma ile değil
  alt örnekleme ile ayarla; bu seçimin sonucunu açıkla.
- Herhangi bir ön işleme adımı öğrenilmeden önce test kümesini ayır.
- Dört çarpı dörtlük örnek ızgarasını etiketleriyle göster.
- Bu veri gerçek bir tarayıcıdan gelen klinik görüntü olsaydı hangi ön işleme adımları
  değişirdi ve atlanırlarsa ne yanlış giderdi, açıkça yaz.
```

### English

```
Using the specification above, write a single Colab cell that loads an appropriate
subset of MedMNIST for this problem, or, if no MedMNIST collection fits, generates a
synthetic image set with a controllable signal.

Requirements:
- Report the class balance and set it to the prevalence in my specification by
  subsampling rather than by reweighting, and explain the consequence of that choice.
- Hold out a test split before any preprocessing step is fitted.
- Display a four by four grid of examples with their labels.
- State explicitly which preprocessing steps would differ if this were real clinical
  imaging from a scanner, and what could go wrong if they were skipped.
```

## 2c. Physiological time series · Fizyolojik zaman serisi

### Türkçe

```
Yukarıdaki belirtimi kullanarak, bu problem için fizyolojik zaman serisi verisi
hazırlayan tek bir Colab hücresi yaz. Uygunsa MIMIC-IV-ECG demo kümesini kullan, değilse
sentetik sinyal üret.

Gereksinimler:
- Örnekleme hızını ve pencere uzunluğunu yaz, ikisini de belirtimdeki klinik karar anına
  göre gerekçelendir.
- Eğitim ve test ayrımını pencere düzeyinde değil, her zaman hasta düzeyinde yap.
  Pencere düzeyinde ayrımın başarımı neden şişireceğini yorum satırında açıkla.
- Birden fazla sınıf varsa her sınıftan birer tane olmak üzere üç örnek segment çiz.
```

### English

```
Using the specification above, write a single Colab cell that prepares a physiological
time series dataset for this problem, using the MIMIC-IV-ECG demo if it fits, otherwise
generating synthetic signals.

Requirements:
- State the sampling rate and window length and justify both against the clinical
  decision point in the specification.
- Segment by patient, never by window, when splitting into train and test. Explain in
  a comment why window level splitting would inflate performance.
- Plot three example segments, one from each class if there is more than one.
```

## 2d. Clinical text · Klinik metin

### Türkçe

```
Yukarıdaki belirtimi kullanarak, bu problem için sentetik bir klinik metin derlemi
üreten tek bir Colab hücresi yaz.

Gereksinimler:
- Notlar belirtimde yazan dilde ve üslupta olsun.
- Gerçek klinik metni zorlaştıran kayıt özelliklerini içersin: Kısaltmalar, olumsuzlama,
  belirsizlik ifadeleri, şablon metin ve önceki nottan kopyalama.
- Etiket tek bir anahtar kelimeden çıkarılabilir olmasın. Hangi yüzeysel ipuçlarını
  bilerek elediğini söyle.
- Üç tam örnek notu etiketleriyle yazdır.
```

### English

```
Using the specification above, write a single Colab cell that generates a synthetic
clinical text corpus for this problem.

Requirements:
- Notes must be in the language and register stated in my specification.
- Include the documentation artefacts that make real clinical text hard: abbreviations,
  negation, uncertainty, templated boilerplate, and copy forward from previous notes.
- The label must not be trivially recoverable from a single keyword. Tell me which
  surface cues you deliberately avoided.
- Print three full example notes with their labels.
```

---

# Prompt 3 — Baseline · Temel model

Bu istem iki dilde ayrı ayrı çalıştırılır ve çıktılar karşılaştırılır.

### Türkçe

```
Yukarıdaki veri kümesini ve belirtimi kullanarak temel bir model eğiten tek bir Colab
hücresi yaz.

Gereksinimler:
- Bu veri türü için işe yarayabilecek en basit modelle başla ve burada neden uygun
  temel model olduğunu söyle.
- Veriyi, ölçekleyici, kodlayıcı ve tamamlayıcı dâhil hiçbir şey öğrenilmeden önce ayır.
  Ön işleme zincirinin tamamını bir pipeline içine koy ki bu sessizce bozulamasın.
- Henüz hiperparametre ayarı yapma. Temel model iyi olmak için değil, aşılmak için vardır.
- Eğitim ve test skorlarını yan yana yazdır ve aradaki farkın neyi gösterdiğini tek
  cümleyle söyle.

Başlık sayı olarak doğruluğu raporlama. Belirtimdeki prevalansta doğruluğun neden
yanıltıcı olduğunu tek cümleyle açıkla.
```

### English

```
Using the dataset above and the specification, write a single Colab cell that trains a
baseline model.

Requirements:
- Start with the simplest model that could work for this data type, and say why it is
  the appropriate baseline here.
- Split the data before any fitting, including any scaler, encoder or imputer. Put the
  whole preprocessing chain inside a pipeline so this cannot go wrong silently.
- Do not tune hyperparameters yet. A baseline exists to be beaten, not to be good.
- Print the training and test scores side by side and, in one sentence, tell me what
  the gap between them indicates.

Do not report accuracy as the headline number. Explain in one sentence why accuracy is
misleading at the prevalence stated in my specification.
```

Son paragraf dersin tamamının bir talimata sıkıştırılmış hâlidir. Yüzde yedi prevalansta
her zaman olumsuz sınıfı söyleyen bir model yüzde 93 doğruluk vermektedir ve bu
gösterilmemiş bir katılımcı o sayıyı kabul edecektir.

**→ Burada dil karşılaştırma egzersizini uygulayınız.**

---

# Prompt 4 — Honest evaluation · Dürüst değerlendirme

Atölyenin dönüm noktası olan istemdir.

### Türkçe

```
Şimdi modeli düzgün biçimde değerlendir. Aşağıdakilerin tamamını kapsayan ve her birinin
altına kısa bir sade dil yorumu yazdıran tek bir Colab hücresi üret:

1. Ayrım gücü: Güven aralığıyla birlikte ROC AUC ve kesinlik-duyarlılık eğrisi altındaki
   alan. Benim prevalansımda hangisinin daha bilgilendirici olduğunu ve nedenini yaz.
2. Kalibrasyon: Kalibrasyon eğrisi ve kalibrasyon eğimi. Modelin aşırı mı yoksa yetersiz
   mi güvenli olduğunu ve bunun eşik belirleyen bir klinisyen için ne anlama geldiğini yaz.
3. Çalışma noktası: Belirtimdeki maliyet asimetrisine uygun bir eşik seç; o eşikte
   duyarlılık, özgüllük, pozitif kestirim değeri ve negatif kestirim değerini raporla.
   Eşik seçimini gerekçelendir.
4. Klinik karşılık: O eşikte sistem her yüz hastada kaç uyarı üretir ve bunların kaçı
   doğrudur? Belirtimdeki gerçek prevalansı kullan.
5. Alt grup dökümü: Ölçütleri her demografik alt grup için ayrı ayrı tekrarla ve
   başarımın belirgin biçimde düştüğü alt grupları işaretle.
6. Boş karşılaştırma: Her zaman çoğunluk sınıfını söyleyen bir model bu ölçütlerin her
   birinde ne elde ederdi?

Sonunda DEVREYE ALIR MIYDIM başlıklı bir paragraf yaz. Bunu modelin yazarı olarak değil,
şüpheci bir hakem olarak yaz.
```

### English

```
Now evaluate the model properly. Write a single Colab cell that produces an evaluation
report covering all of the following, with a short plain language interpretation
printed under each:

1. Discrimination: ROC AUC with a confidence interval, and precision-recall AUC.
   State which of the two is more informative at my prevalence and why.
2. Calibration: a calibration curve and a calibration slope. State whether the model is
   over-confident or under-confident and what that means for a clinician setting a
   threshold.
3. The operating point: choose a threshold consistent with the cost asymmetry in my
   specification, and report sensitivity, specificity, positive predictive value and
   negative predictive value at that threshold. Justify the threshold choice.
4. Clinical translation: at that threshold, state how many alerts the system would fire
   per hundred patients and how many of those would be true. Use the actual prevalence
   from my specification.
5. Subgroup breakdown: repeat the metrics separately for each demographic subgroup and
   flag any subgroup where performance is materially worse.
6. A null comparison: what would a model that always predicts the majority class
   achieve on each of these metrics?

End with a paragraph headed WOULD I DEPLOY THIS, written as a sceptical reviewer rather
than as the author of the model.
```

Dördüncü madde sayıları kliniğe bağlamakta, altıncı madde ise hiçbir şey öğrenmemiş bir
modelden etkilenmeyi engellemektedir. Kapanış paragrafı bilinçli olarak hakem konumundan
yazdırılmaktadır; kendi işini değerlendirmesi istenen bir asistan, kendisine karşıt bir rol
verildiğinde özet istenmesine kıyasla belirgin biçimde daha eleştireldir.

---

# Divergence point · Ayrışma noktası

Buraya kadar her şey ortak senaryo üzerinde çalıştı. Bu noktadan sonra her katılımcı
`{{CANVAS}}` yerine kendi cevaplarını koymakta ve birinci istemden dördüncü isteme kadar
olan zinciri yeni bir konuşmada yeniden çalıştırmaktadır. Zincir değişmez, problem değişir.

Everything above ran on the shared scenario. From here, each participant replaces
`{{CANVAS}}` with their own answers and runs prompts 1 to 4 again in a fresh conversation.
The chain does not change. The problem does.

---

# Prompt 5 — Explainability · Açıklanabilirlik

### Türkçe

```
Bu modeli iki düzeyde açıklayan tek bir Colab hücresi yaz.

Küresel: Model tipine uygun bir yöntemle, modeli genel olarak hangi özniteliklerin
sürüklediğini göster ve çiz.

Yerel: Bir doğru pozitif, bir yanlış pozitif ve bir yanlış negatif örnek seç; her biri
için açıklamayı göster. Katkıların yanına gerçek öznitelik değerlerini de yazdır.

Ardından AÇIKLAMA ELEŞTİRİSİ başlıklı ayrı bir bölümde, modelin eleştirmeni gibi şu
soruları cevapla:
- Yüksek katkılı özniteliklerden herhangi biri sızıntıya, sonucun bir vekiline ya da
  verinin kaydediliş biçiminden kaynaklanan bir artefakta mı benziyor?
- Yanlış pozitif açıklamasını okuyan bir klinisyen, tahminin makul olduğuna ikna olur
  muydu? Olursa, bunun neden bir başarı değil bir sorun olduğunu açıkla.
- Bu katkılardan hangileri nedensellik iddiası sanılabilir ve bir klinisyen bunlara
  nedensel bir iddia gibi davranırsa ne yanlış gider?
```

### English

```
Write a single Colab cell that explains this model at two levels.

Global: which features drive the model overall, using a method appropriate to the model
type. Plot it.

Local: pick one true positive, one false positive and one false negative, and show the
explanation for each. Print the actual feature values alongside the attributions.

Then, in a separate printed section headed EXPLANATION CRITIQUE, answer these as the
model's critic:
- Does any high-attribution feature look like leakage, a proxy for the outcome, or an
  artefact of how the data was recorded rather than a clinical signal?
- Would a clinician reading the false positive explanation be persuaded that the
  prediction was reasonable? If so, explain why that is a problem rather than a success.
- Which of these attributions could be mistaken for a causal claim, and what would go
  wrong if a clinician acted on it as one?
```

Önemli olan yanlış pozitif örneğidir. Yanlış bir tahmini makul gösteren bir açıklama,
açıklanabilirliğin hatayı aklama mekanizmasıdır ve bunu bir kez görmek, kavramın tanımını
öğrenmekten daha değerlidir.

---

# Prompt 6 — Safety guardrails · Güvenlik bariyerleri

### Türkçe

```
Bu sisteme üç güvenlik davranışı ekleyen tek bir Colab hücresi yaz.

1. Çekimserlik: Tahmin edilen olasılık, karar eşiğinin etrafındaki bir bantta kaldığında
   sistem tahmin yerine "yeterli güven yok, klinisyen değerlendirmesi gerekli" döndürsün.
   Bandı rastgele değil kalibrasyon sonuçlarından seç ve artık vakaların yüzde kaçında
   çekimser kalındığını raporla.
2. Dağılım dışı tespiti: Eğitim popülasyonuna benzemeyen girdileri işaretle. Açıkça
   dağılım dışı bir vaka kurarak çalıştığını göster.
3. Girdi doğrulama: Fizyolojik olarak imkânsız değerleri sessizce tahmine sokmak yerine
   açıklayıcı bir mesajla reddet.

Ardından KIRMIZI TAKIM başlıklı bir bölümde, bu sistemi kötü davranmaya itecek beş somut
girdi ve sistemin her birinde ne yaptığını yazdır. En az biri bariz bozuk değil, klinik
olarak makul bir vaka olsun.
```

### English

```
Write a single Colab cell that adds three safety behaviours to this system.

1. Abstention. When the predicted probability falls in a band around the decision
   threshold, the system returns "insufficient confidence, clinician review required"
   instead of a prediction. Choose the band from the calibration results, not
   arbitrarily, and report what fraction of cases now abstain.
2. Out of distribution detection. Flag inputs that do not resemble the training
   population. Show it working by constructing one clearly out of distribution case.
3. Input validation. Reject physiologically impossible values with an informative
   message rather than silently predicting on them.

Then print a section headed RED TEAM containing five specific inputs that would make
this system behave badly, and what it does with each. Include at least one case that is
clinically plausible rather than obviously broken.
```

---

# Prompt 7 — Governance artefacts · Yönetişim belgeleri

### Türkçe

```
Bu sistem için iki belge üret. Çıktıyı kod olarak değil, markdown olarak ver.

BİRİNCİ BELGE, bir model kartı. İçeriği: Amaçlanan kullanım ve kullanıcılar; açıkça
kapsam dışı kullanımlar; eğitim verisi ve sınırlılıkları; alt grup dökümü dâhil
değerlendirme sonuçları; çalışma eşiği ve bu eşiği kimin seçtiği; bilinen başarısızlık
biçimleri; çekimserlik ve devretme davranışı; devreye alma sonrası gerekecek izleme.

İKİNCİ BELGE, bir düzenleyici triyaj notu. Şu soruları cevapla:
- AB Tıbbi Cihaz Tüzüğü 2017/745 Kural 11 kapsamında bu yazılım büyük olasılıkla tıbbi
  cihaz sayılır mı, hangi gerekçeyle?
- Cihaz sayılıyorsa AB Yapay Zekâ Yasası'nın hangi eki uygulanır ve geçerli uyum tarihi
  nedir? Temmuz 2026'da yürürlüğe giren AB 2026/1744 sayılı Dijital Omnibus
  düzenlemesinin bu tarihleri değiştirdiğini dikkate al.
- Amerika Birleşik Devletleri'nde FD&C Act 520(o)(1)(E) maddesindeki klinik karar destek
  muafiyetinin dört ölçütünü karşılar mı? Özellikle bağımsız gözden geçirme ölçütünü ele al.
- Türk hukukunda, sağlık verisinin özel nitelikli kişisel veri olması nedeniyle 6698
  sayılı Kanun'dan hangi yükümlülükler doğar?

Dört maddenin her birinde kendi güven düzeyini ve bir hukukçunun neyi kontrol etmesi
gerektiğini belirt. Bunların hiçbirini hukuki görüş olarak sunma.
```

### English

```
Produce two documents for this system. Output them as markdown, not as code.

DOCUMENT 1, a model card, containing: intended use and intended users; explicitly
out-of-scope uses; training data and its limitations; evaluation results including the
subgroup breakdown; the operating threshold and who chose it; known failure modes; the
abstention and escalation behaviour; and what monitoring would be required after
deployment.

DOCUMENT 2, a regulatory triage note answering:
- Under EU Medical Device Regulation 2017/745 Rule 11, would this software likely
  qualify as a medical device, and on what reasoning?
- If it is a device, which EU AI Act annex applies and what is the operative compliance
  date? Note that the Digital Omnibus, Regulation (EU) 2026/1744, changed these dates
  in July 2026.
- Would this software meet the four criteria of FD&C Act Section 520(o)(1)(E) for the
  United States clinical decision support exclusion? Address the independent review
  criterion specifically.
- Under Turkish law, which obligations arise from Law No. 6698 given that health data
  is a special category of personal data?

For each of the four points, state your confidence and what a lawyer would need to check.
Do not present any of this as legal advice.
```

İkinci belgeye sorgulama istemini özellikle dikkatli uygulayınız. Düzenleyici sorular
kendinden emin icadı davet etmektedir ve bu alandaki uyum tarihleri Temmuz 2026'da
değişmiştir; bu, pek çok asistanın hâlâ eski takvimi döndürecek kadar yeni bir tarihtir.

---

## What to keep · Neyi saklamalı

Oturumun sonunda üç şey saklanmaya değerdir: Doldurulmuş kart, konuşma dökümü ve dördüncü
istemden çıkan değerlendirme raporu. Kod en az değerli çıktıdır, çünkü karttan dakikalar
içinde yeniden üretilebilmektedir. Bu sistemin neden var olması ya da olmaması gerektiğine
dair akıl yürütme ise yeniden üretilemez.
