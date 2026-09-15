# Model Card · Model Kartı

Yedinci istemin ürettiği belge bu şablonla karşılaştırılmaktadır. Şablonda olup üretilen
belgede bulunmayan her başlık, cevaplanmamış bir sorudur. Boş bırakılan her alan, bir
klinisyenin sorması gereken sorudur.

Bir kural bütün belge boyunca geçerlidir: Ölçülmemiş bir şey bu kartta iyimser biçimde
yazılmaz. "Test edilmedi" geçerli bir cevaptır ve uydurulmuş bir sayıdan üstündür.

---

## 1. Kimlik · Identification

| | |
|---|---|
| Sistem adı | |
| Sürüm | |
| Tarih | |
| Sorumlu kişi ve kurum | |
| İletişim | |

---

## 2. Amaçlanan kullanım · Intended use

**Hangi klinik karar destekleniyor?**

**Kim kullanacak?**

**Hangi anda devreye giriyor?**

**Çıktı ne biçimde sunuluyor?** Olasılık, sıralama, ikili uyarı ya da işaretleme.

---

## 3. Kapsam dışı kullanımlar · Out-of-scope uses

Sistemin açıkça yapmadığı ve yapmak için kullanılmaması gereken şeyler. Bu bölüm boş
bırakılmamalıdır; boş bir kapsam dışı listesi, kapsamın düşünülmediği anlamına gelir.

- Tarama amacıyla kullanılamaz, çünkü
- Şu hasta grubunda geçerli değildir, çünkü
- Tek başına karar gerekçesi olarak kullanılamaz, çünkü

---

## 4. Eğitim verisi ve sınırlılıkları · Training data

| | |
|---|---|
| Kaynak | |
| Merkez sayısı | |
| Hasta sayısı | |
| Kayıt dönemi | |
| Sonuç prevalansı | |
| Eksik veri oranı | |
| Erişim ve lisans | |

**Temsil boşlukları.** Hangi hasta grupları bu veride yetersiz temsil ediliyor? Bu
boşlukların sistemin kullanılacağı popülasyona etkisi nedir?

**Veri kaydına özgü artefaktlar.** Ölçüm sıklığı, kodlama alışkanlığı ya da cihaz
farklılıkları modelin öğrendiği şeyi etkiliyor olabilir mi?

---

## 5. Değerlendirme · Evaluation

### Ayrım gücü

| Ölçüt | Değer | %95 güven aralığı |
|---|---|---|
| ROC AUC | | |
| Ortalama kesinlik | | |
| Boş model karşılaştırması | | |

### Kalibrasyon

| Ölçüt | Değer |
|---|---|
| Kalibrasyon eğimi | |
| Kesişim | |
| Brier skoru | |
| Yorum | |

### Çalışma noktası

| | |
|---|---|
| Eşik | |
| Eşiği kim seçti | |
| Seçim gerekçesi | |
| Duyarlılık | |
| Özgüllük | |
| Pozitif kestirim değeri | |
| Negatif kestirim değeri | |
| Yüz hastada uyarı sayısı | |
| Bunların kaçı doğru | |

### Alt grup dökümü

| Alt grup | n | Pozitif | AUC | Duyarlılık | PKD |
|---|---|---|---|---|---|
| | | | | | |

Örneklem yetersizliği nedeniyle değerlendirilemeyen alt gruplar buraya yazılır. Bu bir
eksiklik değil, bir bulgudur: Hiç test edilmemiş bir grup için sistemin adil olduğu
gösterilemez.

### Dış doğrulama

Yapıldı mı? Yapılmadıysa, bu kartın taşıdığı bütün sayılar tek merkeze aittir ve başka bir
merkezde geçerli değildir.

---

## 6. Bilinen başarısızlık biçimleri · Known failure modes

Her madde için: Ne oluyor, hangi hastada oluyor, sonucu ne.

1.
2.
3.

---

## 7. Çekimserlik ve devretme · Abstention and escalation

| | |
|---|---|
| Çekimserlik bandı | |
| Bant nasıl seçildi | |
| Çekimser kalınan vaka oranı | |
| Bant denetimi sonucu | |
| Dağılım dışı tespiti yöntemi | |
| Eksik veri bariyeri | |
| Devretme kuralı | |

---

## 8. Girdi doğrulama · Input validation

| Öznitelik | Alt sınır | Üst sınır | Kaynak |
|---|---|---|---|
| | | | |

Kaynağı olmayan hiçbir klinik sınır bu tabloya yazılmaz. Veriden türetilen zarf, klinik
sınır değildir ve öyle sunulamaz.

---

## 9. Devreye alma sonrası izleme · Post-deployment monitoring

**Ne izlenecek?** Başarım kayması, girdi dağılımı değişimi, uyarı hacmi, klinisyen kabul
oranı.

**Hangi sıklıkla?**

**Hangi eşikte müdahale edilecek?**

**İzlemeden kim sorumlu?**

Bu bölüm boşsa sistem devreye alınmamalıdır. Başarım kayması ölçülmediği sürece fark
edilmemektedir.

---

## 10. Düzenleyici konum · Regulatory position

Ayrıntı için `regulatory-triage.md` dosyasına bakınız. Bu bölüme yalnızca sonuç yazılır.

| | |
|---|---|
| Tıbbi cihaz mı | |
| Tabi olunan mevzuat | |
| Geçerli uyum tarihi | |
| Kişisel veri değerlendirmesi yapıldı mı | |
| Hukuki görüş alındı mı | |
