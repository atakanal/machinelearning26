import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from scipy.stats import poisson

# BÖLÜM 2: MLE

# Gözlemlenen Trafik Verisi
traffic_data = np.array([12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15]) #

def negative_log_likelihood(lam, data):
    """
    Poisson dağılımı için Negatif Log-Likelihood hesaplar.
    İpucu: log(k!) terimi optimizasyon sırasında sabit olduğu için ihmal edilebilir.
    """
    n = len(data) 
    
    # TODO: Log-likelihood formülünü (negatif olarak) buraya yazın
    # l(lambda) = -n * lambda + ln(lambda) * sum(k)
    # Negatif l(lambda) = n * lambda - ln(lambda) * sum(k)
    
    sum_k = np.sum(data)
    nll = n * lam - np.log(lam) * sum_k
    
    return nll 

# Başlangıç tahmini
initial_guess = 1.0 #

# Optimizasyon: NLL'yi minimize etmek, Likelihood'u maximize etmektir.
result = opt.minimize(negative_log_likelihood, initial_guess, args=(traffic_data,), bounds=[(0.001, None)]) #

print("--- SAYISAL MLE SONUÇLARI ---")
print(f"Sayısal Tahmin (MLE lambda): {result.x[0]:.4f}") #
print(f"Analitik Tahmin (Ortalama): {np.mean(traffic_data):.4f}\n") #

# ----------------------------------------------------
# BÖLÜM 3: Model Karşılaştırma ve Görselleştirme

# Bulduğumuz MLE lambda değeri
lambda_mle = result.x[0]

# Poisson PMF için x değerleri (0'dan verideki max değerin biraz fazlasına kadar)
x_degerleri = np.arange(0, np.max(traffic_data) + 5)
# Hesaplanan lambda ile Poisson olasılıklarını (PMF) buluyoruz
poisson_pmf = poisson.pmf(x_degerleri, lambda_mle)

# Grafiği Çizme
plt.figure(figsize=(10, 6))

# Gerçek veri setinin histogramı (density=True ile olasılığa çeviriyoruz)
plt.hist(traffic_data, bins=np.arange(0, np.max(traffic_data)+2)-0.5, density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Gerçek Veri Histogramı')

# MLE ile bulunan Poisson Dağılımının çizgisi
plt.plot(x_degerleri, poisson_pmf, 'ro-', ms=8, label=f'Poisson PMF Modeli ($\lambda$={lambda_mle:.2f})')

# Grafik Ayarları (Zorunlu tutulan kısımlar)
plt.title('Akıllı Şehir Planlaması: Trafik Yoğunluğu Modeli (MLE)')
plt.xlabel('1 Dakikada Geçen Araç Sayısı')
plt.ylabel('Olasılık')
plt.legend()
plt.grid(axis='y', alpha=0.7)
plt.tight_layout()
plt.savefig("Figure_1.png", bbox_inches='tight', dpi=300)
# Grafiği gösterme
plt.show()