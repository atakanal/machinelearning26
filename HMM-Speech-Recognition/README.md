# HMM ile İzole Kelime Tanıma Sistemi Tasarımı

[cite_start]Bu proje, YZM212 Makine Öğrenmesi dersi I. Laboratuvar değerlendirmesi kapsamında geliştirilmiştir[cite: 1]. [cite_start]Temel amacı, Saklı Markov Modelleri (HMM - Hidden Markov Model) kullanılarak istatistiksel tabanlı bir izole kelime tanıma (speech recognition) sistemi simüle etmektir[cite: 2, 20].

## 📌 Problem Tanımı
[cite_start]Konuşma tanıma sistemlerinde kelimeler, "fonem" adı verilen temel ses birimlerinden oluşur[cite: 4]. [cite_start]Bu projede fonemler HMM içerisindeki "Gizli Durumlar" (Hidden States) olarak modellenmiş olup, dışarıdan alınan ses spektrumu frekansları (High/Low) ise "Gözlemler" (Observations) olarak ele alınmıştır[cite: 5, 9]. [cite_start]Amaç, belirli olasılık matrislerine dayanarak, verilen bir ses dizisini en yüksek olasılıkla (Log-Likelihood) üretebilecek kelimeyi (EV veya OKUL) tespit etmektir[cite: 23, 25, 26].

## 📊 Veri
Projede iki tür veri kullanılmıştır:
- [cite_start]**Teorik Veri (1. Bölüm):** Durum uzayı $S=\{e,v\}$ ve gözlem uzayı $O=\{High, Low\}$ olan teorik bir sistem üzerinden elle hesaplama yapılmıştır[cite: 8, 9, 17]. 
- [cite_start]**Eğitim ve Test Verisi (2. Bölüm):** Python uygulaması için kategorik indekslere (0 ve 1) dönüştürülmüş temsili dinleme dizileri oluşturulmuştur[cite: 24, 33]. [cite_start]"EV" ve "OKUL" modellerini eğitmek ve test etmek için NumPy dizileri kullanılmıştır[cite: 23, 29].

## ⚙️ Yöntem
1. [cite_start]**Viterbi Algoritması:** Gelen gözlem dizisinin `[High, Low]` arka planındaki en olası fonem yolunu bulmak için dinamik programlama tabanlı Viterbi algoritması ile manuel hesaplamalar yapılmıştır[cite: 17].
2. [cite_start]**Python ile Sınıflandırma:** `hmmlearn` kütüphanesi kullanılarak (`CategoricalHMM` modülü ile) "EV" ve "OKUL" kelimeleri için iki ayrı model eğitilmiştir[cite: 22, 23]. [cite_start]Gelen yeni test verisi her iki modele sokularak Log-Likelihood skorları karşılaştırılmıştır[cite: 25, 26].

## 🚀 Sonuçlar
- [cite_start]**Teorik Hesaplama:** Viterbi algoritması sonucunda `[High, Low]` gözlem dizisi için en olası fonem dizisinin **"e-v"** olduğu kanıtlanmıştır[cite: 17, 82].
- [cite_start]**Model Sınıflandırması:** Yazılan Python scripti, verilen test verisini her iki HMM modeli üzerinden başarıyla puanlamış ve en yüksek olasılık değerini üreten kelimeyi tahmin etmiştir[cite: 26, 34]. [cite_start]Manuel hesaplamaların detayları `report/cozum_anahtari.pdf` dosyasında mevcuttur[cite: 50].

## 🧠 Yorum ve Tartışma
- [cite_start]**Gürültünün Etkisi:** Ses verisindeki gürültü, doğrudan modelin Emisyon (Yayılma) Olasılıklarını hedef alır ve belirsizliği artırır[cite: 38, 86, 87, 88]. [cite_start]Bu durum Viterbi algoritmasının güven skorunu düşürerek sistemi kararsızlaştırır ve yanlış yolların seçilmesine sebep olabilir[cite: 90, 91].
- [cite_start]**HMM vs. Derin Öğrenme:** Gerçek dünyadaki binlerce kelimelik sistemlerde HMM kullanımı, devasa fonem sayısı yüzünden "Durum Uzayı Patlaması"na (State Space Explosion) yol açar ve işlemci limitlerini aşar[cite: 39, 92, 94, 95]. [cite_start]Ayrıca HMM'lerin bağlam (context) eksikliği handikabına karşın, Derin Öğrenme modelleri uçtan uca öğrenme ile özellikleri kendi kendine çıkarabildiği ve bağlamı anlayabildiği için modern sistemlerde tercih edilmektedir[cite: 96, 97, 98, 99].

## 🛠️ Kurulum ve Çalıştırma
Projeyi kendi ortamınızda çalıştırmak için:

1. Gerekli kütüphaneleri kurun:
   ```bash
   pip install -r requirements.txt

2. Sınıflandırma kodunu çalıştırın:
   python src/recognizer.py
