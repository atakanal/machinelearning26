# MLE ile Akıllı Şehir Planlaması (YZM212)

Bu proje, YZM212 Makine Öğrenmesi dersi 2. Laboratuvar değerlendirmesi kapsamında geliştirilmiştir. Temel amacı, bir şehrin ana caddesindeki trafik yoğunluğunu Poisson Dağılımı ve Maximum Likelihood Estimation (MLE) yöntemi kullanarak istatistiksel olarak modellemektir.

## 📌 Problem Tanımı
Belediyenin ulaşım planlamasına destek olmak amacıyla, bir dakikada geçen araç sayılarından yola çıkarak caddenin trafik karakteristiği çıkarılmalıdır. Amaç, veri setini en yüksek olasılıkla (Likelihood) üretebilecek olan Poisson dağılımı parametresini (lambda) hem analitik türetme hem de sayısal optimizasyon yöntemleriyle bulmaktır.

## 📊 Veri
Projede şehrin en yoğun ana caddesinden 1 dakika aralıklarla toplanmış 14 adet örneklem (araç sayısı) kullanılmıştır. Gözlem seti: `[12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15]`. Analizin son bölümünde (Outlier Analizi), sisteme hatalı kaydedilmiş "200" araçlık bir değer de senaryoya dahil edilerek veri hassasiyeti test edilmiştir.

## ⚙️ Yöntem
1. **Analitik Çözüm (Teorik Türetme):** Poisson dağılımı formülü üzerinden Log-Likelihood fonksiyonu türetilmiş ve birinci türevi sıfıra eşitlenerek en iyi parametre tahmininin (MLE), verilerin aritmetik ortalaması olduğu matematiksel olarak ispatlanmıştır.
2. **Sayısal Çözüm (Python):** `scipy.optimize` kütüphanesi kullanılarak Negatif Log-Olabilirlik (Negative Log-Likelihood) fonksiyonunu minimize eden optimum lambda değeri algoritmik olarak bulunmuştur.
3. **Görselleştirme:** Elde edilen model, gerçek veri histogramı ile birlikte `matplotlib` kullanılarak Olasılık Kütle Fonksiyonu (PMF) olarak çizdirilmiştir.

## 🚀 Sonuçlar
* Analitik ve sayısal yöntemlerin her ikisi de caddedeki optimum trafik yoğunluğunu **lambda = 12.14** olarak başarıyla hesaplamıştır. 
* Çizdirilen grafikler, gerçek veri dağılımının (11-15 araç bandındaki yoğunlaşma) Poisson eğrisiyle yüksek oranda örtüştüğünü ve modelin verilere çok iyi "fit" (uyum) sağladığını göstermiştir. (Detaylar rapor dosyasındadır.)

## 🧠 Yorum ve Tartışma
Veri setine eklenen "200" gibi tek bir hatalı (outlier) değer, MLE yönteminin doğrudan aritmetik ortalamaya dayanması sebebiyle modeli dramatik şekilde bozmuştur. Lambda değeri bir anda 24.6'ya sıçramıştır. Bu durum, MLE'nin aykırı değerlere karşı son derece dirençsiz (non-robust) olduğunu gösterir. Gerçek hayat senaryolarında bu tarz kör hesaplamalar, belediyelerin gereksiz yol genişletme kararları almasına ve milyonlarca liralık bütçe israfına yol açabilir. Modellemeden önce verilerin kesinlikle ön işlemden (pre-processing) geçirilmesi gerekmektedir.