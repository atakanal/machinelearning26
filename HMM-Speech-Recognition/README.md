# HMM ile İzole Kelime Tanıma Sistemi Tasarımı

Bu proje, YZM212 Makine Öğrenmesi dersi I. Laboratuvar değerlendirmesi kapsamında geliştirilmiştir. Temel amacı, Saklı Markov Modelleri (HMM - Hidden Markov Model) kullanılarak istatistiksel tabanlı bir izole kelime tanıma (speech recognition) sistemi simüle etmektir.

## 📌 Problem Tanımı
Konuşma tanıma sistemlerinde kelimeler, "fonem" adı verilen temel ses birimlerinden oluşur. Bu projede fonemler HMM içerisindeki "Gizli Durumlar" (Hidden States) olarak modellenmiş olup, dışarıdan alınan ses spektrumu frekansları (High/Low) ise "Gözlemler" (Observations) olarak ele alınmıştır. Amaç, belirli olasılık matrislerine dayanarak, verilen bir ses dizisini en yüksek olasılıkla (Log-Likelihood) üretebilecek kelimeyi (EV veya OKUL) tespit etmektir.

## 📊 Veri
Projede iki tür veri kullanılmıştır:
- **Teorik Veri (1. Bölüm):** Durum uzayı $S=\{e,v\}$ ve gözlem uzayı $O=\{High, Low\}$ olan teorik bir sistem üzerinden elle hesaplama yapılmıştır. 
- **Eğitim ve Test Verisi (2. Bölüm):** Python uygulaması için kategorik indekslere (0 ve 1) dönüştürülmüş temsili dinleme dizileri oluşturulmuştur. "EV" ve "OKUL" modellerini eğitmek ve test etmek için NumPy dizileri kullanılmıştır.

## ⚙️ Yöntem
1. **Viterbi Algoritması:** Gelen gözlem dizisinin `[High, Low]` arka planındaki en olası fonem yolunu bulmak için dinamik programlama tabanlı Viterbi algoritması ile manuel hesaplamalar yapılmıştır.
2. **Python ile Sınıflandırma:** `hmmlearn` kütüphanesi kullanılarak (`CategoricalHMM` modülü ile) "EV" ve "OKUL" kelimeleri için iki ayrı model eğitilmiştir. Gelen yeni test verisi her iki modele sokularak Log-Likelihood skorları karşılaştırılmıştır.

## 🚀 Sonuçlar
- **Teorik Hesaplama:** Viterbi algoritması sonucunda `[High, Low]` gözlem dizisi için en olası fonem dizisinin **"e-v"** olduğu kanıtlanmıştır.
- **Model Sınıflandırması:** Yazılan Python scripti, verilen test verisini her iki HMM modeli üzerinden başarıyla puanlamış ve en yüksek olasılık değerini üreten kelimeyi tahmin etmiştir. Manuel hesaplamaların detayları `report/cozum_anahtari.pdf` dosyasında mevcuttur.

## 🧠 Yorum ve Tartışma
- **Gürültünün Etkisi:** Ses verisindeki gürültü, doğrudan modelin Emisyon (Yayılma) Olasılıklarını hedef alır ve belirsizliği artırır. Bu durum Viterbi algoritmasının güven skorunu düşürerek sistemi kararsızlaştırır ve yanlış yolların seçilmesine sebep olabilir.
-**HMM vs. Derin Öğrenme:** Gerçek dünyadaki binlerce kelimelik sistemlerde HMM kullanımı, devasa fonem sayısı yüzünden "Durum Uzayı Patlaması"na (State Space Explosion) yol açar ve işlemci limitlerini aşar. Ayrıca HMM'lerin bağlam (context) eksikliği handikabına karşın, Derin Öğrenme modelleri uçtan uca öğrenme ile özellikleri kendi kendine çıkarabildiği ve bağlamı anlayabildiği için modern sistemlerde tercih edilmektedir.

## 🛠️ Kurulum ve Çalıştırma
Projeyi kendi ortamınızda çalıştırmak için:

1. Gerekli kütüphaneleri kurun:
   ```bash
   pip install -r requirements.txt

2. Sınıflandırma kodunu çalıştırın:
   python src/recognizer.py

