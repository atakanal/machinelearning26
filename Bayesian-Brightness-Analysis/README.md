## Uzak Bir Galaksinin Parlaklık Analizi

## 1. Problem Tanımı
Bu çalışmada Bayesyen çıkarım kullanılarak gürültülü gözlem verilerinden bir gök cisminin gerçek parlaklığı ve ölçüm belirsizliği tahmin edilmiştir. Amaç, sentetik olarak üretilmiş gözlem verisi üzerinden iki temel parametrenin posterior dağılımını bulmaktır:

- **μ (mu):** Gerçek parlaklık / ortalama değer
- **σ (sigma):** Ölçüm belirsizliği / standart sapma

Bu amaçla Markov Chain Monte Carlo (MCMC) temelli **emcee** kütüphanesi kullanılmıştır. Sonuçlar sayısal olarak özetlenmiş ve **corner plot** ile görselleştirilmiştir.

## 2. Veri
Ödev kapsamında sentetik veri üretilmiştir. Kullanılan gerçek parametreler aşağıdaki gibidir:

- `true_mu = 150.0`
- `true_sigma = 10.0`
- `n_obs = 50`

Veri üretimi için:

```python
np.random.seed(42)
data = true_mu + true_sigma * np.random.randn(n_obs)
```

Bu yapı, gerçek parlaklığı 150 olan ve standart sapması 10 olan bir gözlem sürecini temsil etmektedir.

## 3. Yöntem
Bayesyen model üç ana bileşenden oluşmaktadır:

### 3.1 Log-Likelihood
Verinin verilen parametreler altında gözlenme olasılığı normal dağılım varsayımıyla modellenmiştir.

### 3.2 Log-Prior
Parametreler için geniş ancak fiziksel açıdan anlamlı sınırlar belirlenmiştir:

- `0 < mu < 300`
- `0 < sigma < 50`

### 3.3 Log-Posterior
Posterior olasılık, prior ile likelihood toplamı üzerinden hesaplanmıştır.

MCMC için aşağıdaki ayarlar kullanılmıştır:

- Başlangıç değeri: `[140, 5]`
- Walker sayısı: `32`
- Toplam adım sayısı: `2000`
- Burn-in: `500`
- Thin: `15`

## 4. Sonuçlar
Aşağıdaki sonuçlar, çalıştırılan MCMC simülasyonu sonucunda elde edilen posterior özetini göstermektedir.

| Değişken | Gerçek Değer | Tahmin Edilen (Median) | Alt Sınır (%16) | Üst Sınır (%84) | Mutlak Hata |
|---|---:|---:|---:|---:|---:|
| μ (Parlaklık) | 150.0 | 147.79 | 146.43 | 149.08 | 2.21 |
| σ (Hata Payı) | 10.0 | 9.49 | 8.55 | 10.53 | 0.51 |

## 5. Sonuçların Yorumu
### 5.1 Merkezi Eğilim ve Doğruluk
Model, gürültülü gözlemlere rağmen gerçek parlaklık değerine oldukça yakın bir tahmin üretmiştir. μ için bulunan 147.79 değeri, gerçek 150.0 değerine 2.21 birim uzaklıktadır. Bu fark, sentetik verinin sonlu örneklem etkisi ve rastgele gürültü nedeniyle oluşmuştur. Buna rağmen modelin genel olarak başarılı olduğu söylenebilir.

### 5.2 Hassasiyet Karşılaştırması
μ parametresi, σ parametresine göre daha dar bir güven aralığına sahiptir. Bunun temel nedeni, ortalamanın tüm gözlemlerden doğrudan ve güçlü biçimde tahmin edilmesidir. Standart sapma ise gözlem saçılımına bağlı olduğu için örneklem dalgalanmalarından daha fazla etkilenir. Bu nedenle σ tahmini genellikle daha belirsiz olur.

### 5.3 Korelasyon Analizi
Corner plot üzerinde μ ve σ parametrelerinin ortak dağılımı büyük ölçüde dik ve simetriğe yakın bir yapı göstermektedir. Bu durum, iki parametre arasında güçlü bir korelasyon bulunmadığını, en fazla çok zayıf düzeyde bir ilişki olabileceğini göstermektedir. Başka bir ifadeyle parlaklık tahmini ile hata tahmini birbirini güçlü biçimde sürüklememektedir.

## 6. Ek Analizler
### 6.1 Prior Etkisi
Eğer μ için çok dar ve yanlış bir prior seçilseydi (örneğin `100 < mu < 110`), posterior dağılım veri tarafından tamamen düzeltilmeyebilir ve sonuçlar gerçek değerden uzaklaşabilirdi. Bu durum Bayesyen yöntemlerde prior seçiminin önemini göstermektedir.

### 6.2 Veri Miktarı Etkisi
Gözlem sayısı `n_obs = 50` yerine `n_obs = 5` yapıldığında posterior dağılım belirgin biçimde genişler. Bu da belirsizliğin arttığını ve modelin parametreler hakkında daha az emin olduğunu gösterir.

## 7. Kullanılan Dosyalar
- `bayesian_code.py`: Python kodu
- `README.md`: Kısa proje özeti
- `RAPOR.md`: Ayrıntılı rapor
- Grafikler: `corner_plot.png`, `trace_plot.png`

## 8. Genel Sonuç
Bu çalışmada Bayesyen çıkarım ve MCMC yaklaşımıyla bir gök cisminin parlaklığı ve ölçüm belirsizliği başarılı şekilde tahmin edilmiştir. Sonuçlar, Bayesyen yöntemin özellikle belirsizliklerin modellenmesinde güçlü bir araç olduğunu göstermektedir.