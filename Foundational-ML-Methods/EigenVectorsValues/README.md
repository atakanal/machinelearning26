# EigenVectorsValues

## Amaç

Bu çalışmada matris manipülasyonu, özdeğer ve özvektör kavramları incelenmiştir.
Ayrıca NumPy kütüphanesindeki `numpy.linalg.eig` fonksiyonu araştırılmış,
son olarak hazır `eig` fonksiyonu kullanilmadan özdeğer hesabı yapan bir yöntem
yeniden uygulanmış ve NumPy ile karşılaştırılmıştır.

---

## 1. Matris Manipülasyonu, Özdeğer ve Özvektörlerin Makine Öğrenmesi ile İlişkisi

### 1.1 Matris Manipülasyonu

Matris, sayıların satır ve sütunlar halinde düzenlenmiş gösterimidir. Makine öğrenmesinde
veri kümeleri çoğunlukla matris biçiminde temsil edilir. Genellikle satırlar gözlemleri,
sütunlar ise özellikleri gösterir. Bu nedenle veri işleme, model kurma ve tahmin üretme
gibi birçok işlem matrisler üzerinden yürür.

Matris manipülasyonu; toplama, çıkarma, çarpma, transpoz alma, ters alma ve determinant
hesaplama gibi işlemleri kapsar. Bu işlemler veri dönüşümü, özellikler arası ilişkilerin
incelenmesi ve model parametrelerinin hesaplanması için kullanılır.

### 1.2 Özdeğer ve Özvektör

Bir kare matris için sıfırdan farklı bir `v` vektörü ve bir `λ` skaler sayısı olmak üzere

`A v = λ v`

eşitliği sağlanıyorsa, `λ` özdeğer, `v` ise özvektördür.

Bu tanıma göre özvektör, matris dönüşümünden sonra yönü değişmeyen özel bir vektördür.
Özdeğer ise bu vektörün ne kadar ölçeklendiğini gösterir. Bu kavramlar, bir lineer
dönüşümün veriyi hangi yönlerde etkilediğini anlamamızı sağlar.

### 1.3 Makine Öğrenmesi ile İlişkisi

Makine öğrenmesinde veriler çoğu zaman yüksek boyutlu uzaylarda yer alır. Bu verilerin
hangi yönlerde daha fazla bilgi taşıdığını anlamak için özdeğer ve özvektör analizi kullanılır.
Özvektörler verinin temel yönlerini, özdeğerler ise bu yönlerin önemini ifade eder.

Bu nedenle şu alanlarda önemlidirler:

- boyut indirgeme
- özellik çıkarımı
- veri sıkıştırma
- gürültü azaltma
- veri yapısının yorumlanması

### 1.4 Kullanıldığı Yöntemler

#### PCA (Principal Component Analysis)

Özdeğer ve özvektörlerin en yaygın kullanım alanlarından biri PCA'dir. Kovaryans matrisinin
özdeğerleri ve özvektörleri hesaplanır. En büyük özdeğere sahip özvektörler verinin en
önemli yönlerini temsil eder. Böylece veri daha düşük boyutta ifade edilir.

#### Spektral Kümeleme

Spektral kümelemede benzerlik grafiği ve Laplasyen matrisi kullanılır. Bu matrislerin
özdeğer ve özvektörleri yardımıyla veri daha uygun bir uzaya taşınır ve kümeleme daha
etkili hale gelir.

#### Kovaryans Analizi

Kovaryans matrisinin özdeğerleri verinin hangi yönlerde daha fazla yayıldığını gösterir.
Özvektörler ise bu yönleri belirler. Böylece verinin iç yapısı daha iyi anlaşılır.

#### Goruntu Isleme ve Veri Sikistirma

Yüksek boyutlu görüntü verileri, temel bileşenler yardımıyla daha düşük boyutta temsil
edilebilir. Bu yaklaşım bilgi kaybını azaltırken depolama ve işlem maliyetini düşürür.

### 1.5 Sonuc

Matris manipülasyonu, özdeğerler ve özvektörler makine öğrenmesinin matematiksel temel
taşlarındandır. Özellikle veri analizi, boyut indirgeme ve dönüşüm işlemlerinde aktif
olarak kullanılmaktadır.

---

## 2. NumPy `linalg.eig` Fonksiyonunun İncelenmesi

NumPy'de `numpy.linalg.eig(a)` fonksiyonu kare bir matrisin özdeğerlerini ve sağ özvektörlerini hesaplar.
Çıktı olarak iki yapı döner:

- özdeğerler dizisi
- özvektörler matrisi

Burada özvektörler sütunlar halinde tutulur. Yani `eigenvectors[:, i]`,
`eigenvalues[i]` değerine karşılık gelen özvektördür.

Dokümantasyonda fonksiyonun genel kare matrisler için LAPACK tabanlı `_geev`
rutinleri ile gerçekleştirildiği belirtilmektedir.

Kaynak kod mantığı özetle şu adımları izler:

1. Girdi dizisini uygun NumPy formatına çevirir.
2. Son iki boyutun kare olduğunu denetler.
3. Gerekli durumlarda sonlu değer kontrolü yapar.
4. Uygun sayısal tür ve dahili lineer cebir çağrılarını seçer.
5. Özdeğer ve özvektörleri döndürür.

`eig` fonksiyonu genel kare matrisler için güçlüdür; ancak simetrik/Hermitian
durumlarda `eigh` kullanmak daha uygun olabilir.

---

## 3. Hazır `eig` Kullanmadan Özdeğer Hesabı ve Karşılaştırma

Bu bölümde referans olarak verilen GitHub reposundaki yaklaşım esas alınmıştır.
Temel fikir, özdeğerleri doğrudan `eig` ile bulmak yerine karakteristik denklem
üzerinden hesaplamaktır.

Bir matrisin özdeğerleri:

`det(A - λI) = 0`

eşitliğini sağlayan `λ` değerleridir.

Bu yöntemde şu adımlar uygulanır:

1. `A - λI` matrisi oluşturulur.
2. Bu yapının determinantı polinom biçiminde elde edilir.
3. Karakteristik polinomun kökleri bulunur.
4. Bu kökler özdeğerler olarak alınır.

Bu yaklaşım öğretici olsa da büyük matrislerde verimli değildir.
Buna karşılık NumPy'nin `eig` yaklaşımı çok daha hızlı ve pratiktir.

---

## 4. Aynı Matris Üzerinde Sonuçların Karşılaştırılması

Çalışmada aşağıdaki matris kullanılmıştır:

```python
A = [[6, 1, -1],
     [0, 7, 0],
     [3, -1, 2]]
```

Bu matris için manuel yöntemle bulunan özdeğerler ile NumPy `eig` fonksiyonu ile
bulunan özdeğerler karşılaştırılmıştır. Sonuç olarak her iki yöntemin aynı özdeğerleri
verdiği görülmüştür. NumPy ek olarak özvektörleri de döndürmektedir.

---

## 5. Kaynakça

1. https://numpy.org/doc/2.1/reference/generated/numpy.linalg.eig.html
2. https://raw.githubusercontent.com/numpy/numpy/v2.1.0/numpy/linalg/_linalg.py
3. https://github.com/LucasBN/Eigenvalues-and-Eigenvectors
4. https://raw.githubusercontent.com/lucasbn/Eigenvalues-and-Eigenvectors/refs/heads/master/main.py
