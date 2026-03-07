import numpy as np
from hmmlearn import hmm

# --- 'EV' Modeli ---
model_ev = hmm.CategoricalHMM(n_components=2)
model_ev.startprob_ = np.array([1.0, 0.0]) # 

# Geçiş Olasılıkları
model_ev.transmat_ = np.array([
    [0.6, 0.4], # P(e->e)=0.6, P(e->v)=0.4
    [0.2, 0.8]  # P(v->e)=0.2, P(v->v)=0.8
])

# Emisyon (Yayılma) Olasılıkları
model_ev.emissionprob_ = np.array([
    [0.7, 0.3], # e durumundayken: P(High|e)=0.7, P(Low|e)=0.3
    [0.1, 0.9]  # v durumundayken: P(High|v)=0.1, P(Low|v)=0.9
])


# --- 'OKUL' Modeli ---
model_okul = hmm.CategoricalHMM(n_components=2)
# OKUL için temsili eğitim verisini data klasöründen çekiyoruz
dosya_yolu = "data/okul_egitim_verisi.txt" # src klasöründen bir üst dizine çıkıp data'ya giriyoruz
X_okul_train = np.loadtxt(dosya_yolu, dtype=int).reshape(-1, 1)
lengths_okul = [4, 4, 4, 4, 4]
model_okul.fit(X_okul_train, lengths_okul)



def siniflandirici(test_verisi, model_1, model_2):
    # Hangi model daha yüksek puan veriyor?
    score_ev = model_1.score(test_verisi)
    score_okul = model_2.score(test_verisi)
    
    print(f"EV Modeli Puanı: {score_ev:.4f}")
    print(f"OKUL Modeli Puanı: {score_okul:.4f}")
    
    if score_ev > score_okul:
        return "EV"
    else:
        return "OKUL"


# --- TEST AŞAMASI ---
test_data = np.array([[0, 1, 1]]).T # Gözlemlerin indexleri

print("--- Log-Likelihood Hesaplamaları ---")
tahmin = siniflandirici(test_data, model_ev, model_okul)
print(f"\nSistem Kararı: Bu ses kaydı '{tahmin}' kelimesine aittir.")