## Uzak Bir Galaksinin Parlaklık Analizi

## 1. Giriş
Bu ödevde Bayesyen çıkarım yaklaşımı kullanılarak gürültülü gözlem verileri üzerinden bir gök cisminin gerçek parlaklığı ve ölçüm belirsizliği tahmin edilmiştir. Astronomide doğrudan deney yapmak çoğu zaman mümkün olmadığından, gözlem verilerinden parametre tahmini yapmak için Bayesyen yöntemler büyük önem taşımaktadır. Bu çalışmada sentetik veri oluşturulmuş, ardından MCMC yöntemi ile posterior dağılımlar elde edilmiştir.

## 2. Kullanılan Veri ve Parametreler
Çalışmada sentetik veri kullanılmıştır. Veri üretiminde kullanılan gerçek parametreler şöyledir:

- Gerçek parlaklık: `true_mu = 150.0`
- Gerçek hata payı: `true_sigma = 10.0`
- Gözlem sayısı: `n_obs = 50`

Veri üretimi için aşağıdaki işlem uygulanmıştır:

```python
np.random.seed(42)
data = true_mu + true_sigma * np.random.randn(n_obs)
```

Bu veri, gerçek değeri 150 olan ancak gözlem gürültüsü içeren bir parlaklık ölçüm kümesini temsil etmektedir.

## 3. Yöntem
Bu çalışmada Bayesyen çıkarım için üç temel fonksiyon tanımlanmıştır:

### 3.1 Log-Likelihood
Verilerin normal dağılıma sahip olduğu varsayılmıştır. Bu nedenle likelihood fonksiyonu, normal dağılımın log formu üzerinden tanımlanmıştır.

### 3.2 Log-Prior
Parametreler için geniş aralıklı, informatif olmayan bir prior seçilmiştir:

- `0 < μ < 300`
- `0 < σ < 50`

### 3.3 Log-Posterior
Posterior olasılık, prior ile likelihood toplamı şeklinde tanımlanmıştır.

### 3.4 MCMC Ayarları
Parametre örneklemesi için **emcee** kütüphanesi kullanılmıştır.

- Başlangıç değeri: `[140, 5]`
- Walker sayısı: `32`
- Adım sayısı: `2000`
- Burn-in: `500`
- Thin: `15`

## 4. Elde Edilen Sonuçlar
Posterior örneklerden hesaplanan özet istatistikler aşağıdaki tabloda verilmiştir.

### 4.1 Parametre Karşılaştırma Tablosu

| Değişken | Gerçek Değer (Girdi) | Tahmin Edilen (Median) | Alt Sınır (%16) | Üst Sınır (%84) | Mutlak Hata |
|---|---:|---:|---:|---:|---:|
| μ (Parlaklık) | 150.0 | 147.79 | 146.43 | 149.08 | 2.21 |
| σ (Hata Payı) | 10.0 | 9.49 | 8.55 | 10.53 | 0.51 |

Bu tabloya göre μ parametresi için bulunan median değer 147.79, σ parametresi için bulunan median değer ise 9.49'dur.

## 5. Sonuçların Bilimsel Yorumu
### 5.1 Merkezi Eğilim ve Doğruluk Analizi
Bayesyen çıkarım modeli, veri setindeki gürültüye rağmen gerçek parlaklık değeri olan 150.0'a oldukça yakın bir sonuç üretmiştir. μ için elde edilen 147.79 değeri ile gerçek değer arasındaki mutlak hata 2.21'dir. Bu hata düşük düzeydedir ve modelin genel olarak doğru sonuç verdiğini göstermektedir. Buradaki sapma, modelin başarısız olmasından değil, sentetik olarak üretilen 50 gözlemden oluşan örneklemin ortalamasının 150.0 değerinden biraz düşük gerçekleşmesinden kaynaklanmaktadır. Dolayısıyla posterior dağılımın 147.79 civarında merkezlenmesi istatistiksel olarak beklenen ve tutarlı bir sonuçtur.

### 5.2 Tahmin Hassasiyeti Karşılaştırması
Tablodaki güven aralıkları incelendiğinde, μ parametresinin güven aralığının σ parametresine göre daha dar olduğu görülmektedir. μ için %16-%84 aralığı 146.43 ile 149.08 arasında olup yaklaşık 2.65 birimlik bir genişliğe sahiptir. σ için aynı aralık 8.55 ile 10.53 arasında olup yaklaşık 1.98 birimdir; ancak bu aralık parametrenin kendi ölçeğine göre değerlendirildiğinde görece daha belirsizdir. Bunun temel nedeni, ortalamanın tüm gözlem noktaları üzerinden daha doğrudan tahmin edilmesidir. Standart sapma ise gözlemlerin saçılımına bağlı olduğundan örneklem değişkenliğinden daha fazla etkilenir. Ayrıca gözlem sayısının 50 olması, ortalama tahmininin daha kararlı hale gelmesini sağlamıştır. Veri sayısı arttıkça ortalama tahmini daha hızlı keskinleşirken, varyans ve standart sapma tahmini genellikle daha yavaş kesinleşir.

### 5.3 Olasılıksal Korelasyon Analizi
Corner plot üzerinde μ ve σ parametrelerinin ortak dağılımı incelendiğinde, elips yapısının belirgin şekilde eğik olmadığı görülmektedir. Konturlar büyük ölçüde yuvarlak ve dik eksenlere yakın bir yapı göstermektedir. Bu durum, iki parametre arasında güçlü bir korelasyon olmadığını, varsa da bunun oldukça zayıf olduğunu göstermektedir. Yani parlaklık tahmini ile hata tahmini birbirine güçlü biçimde bağlı değildir. Eğer elips daha belirgin biçimde eğik olsaydı, μ arttıkça σ'nın da sistematik biçimde değiştiği ve parametreler arasında korelasyon bulunduğu söylenebilirdi.

## 6. Ek Analiz Soruları
### 6.1 Prior Etkisi
Eğer parlaklık için çok dar bir prior seçilseydi, örneğin `100 < μ < 110`, posterior dağılım gerçek verinin gösterdiği bölgeden uzaklaşabilirdi. Bu durumda model, veri yerine önceki varsayıma daha fazla bağlı kalmış olurdu. Yani posterior dağılım 147-150 bandı yerine prior tarafından yapay biçimde 100-110 aralığına çekilirdi. Bu durum, Bayesyen çıkarımda prior seçiminin sonuçlar üzerinde doğrudan etkili olduğunu göstermektedir.

### 6.2 Veri Miktarının Etkisi
Gözlem sayısı 50 yerine 5 olarak seçilseydi posterior dağılım çok daha geniş olurdu. Bunun anlamı, modelin parametreler hakkında daha az emin olmasıdır. Özellikle μ için histogram daha yayvan hale gelir, σ için ise belirsizlik daha da büyür. Veri miktarı arttıkça posterior dağılım daralır ve tahminler daha güvenilir hale gelir. Bu nedenle `n_obs = 50`, bu çalışmada parametrelerin makul hassasiyetle tahmin edilebilmesine önemli katkı sağlamıştır.

## 7. Şekillerin Yorumu
### 7.1 Trace Plot Yorumu
Trace plot incelendiğinde, walker'ların başlangıçta kısa bir geçiş süreci yaşadığı, ardından hem μ hem de σ için kararlı bir bölgede dolaşmaya başladığı görülmektedir. Zincirlerin birbirine karışmış olması ve belirgin bir ayrışma göstermemesi, MCMC örneklemesinin yakınsadığını desteklemektedir. İlk adımlarda görülen hareketlilik burn-in sürecine karşılık gelmektedir. Burn-in sonrası zincirlerin dengeli biçimde örnekleme yaptığı söylenebilir.

### 7.2 Corner Plot Yorumu
Corner plot, her iki parametre için de tek tepeli posterior dağılımlar üretildiğini göstermektedir. μ parametresi yaklaşık 147.79 çevresinde, σ parametresi ise yaklaşık 9.49 çevresinde yoğunlaşmıştır. Bu durum, modelin veri içindeki merkezi eğilimi ve saçılımı başarılı şekilde yakaladığını göstermektedir. İki parametrenin ortak yoğunluk grafiğinde güçlü bir eğim görülmemesi, parametreler arası bağımlılığın zayıf olduğuna işaret etmektedir.

## 8. Genel Değerlendirme
Bu çalışmada Bayesyen çıkarım ve MCMC yöntemi ile gürültülü astronomik gözlem verilerinden parametre tahmini yapılmıştır. Elde edilen sonuçlar, modelin hem gerçek parlaklık değerini hem de hata seviyesini makul doğrulukla tahmin edebildiğini göstermektedir. Özellikle belirsizliklerin açık şekilde modellenebilmesi, Bayesyen yöntemin güçlü yönlerinden biridir.

## 9. Sonuç
Sonuç olarak Bayesyen yaklaşım, astronomik gözlemlerde belirsizlik altında parametre tahmini yapmak için oldukça etkili bir yöntemdir. Bu ödevde kullanılan MCMC tabanlı yöntem sayesinde hem parlaklık hem de hata payı için olasılıksal tahminler elde edilmiş ve sonuçlar görsel olarak da desteklenmiştir.