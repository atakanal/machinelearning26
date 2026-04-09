import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner


# 1) Veri oluşturma
true_mu = 150.0
true_sigma = 10.0
n_obs = 50

np.random.seed(42)
data = true_mu + true_sigma * np.random.randn(n_obs)

# 2) Bayesyen fonksiyonlar
def log_likelihood(theta, data):
    mu, sigma = theta
    if sigma <= 0:
        return -np.inf
    return -0.5 * np.sum(((data - mu) / sigma) ** 2 + np.log(2 * np.pi * sigma**2))


def log_prior(theta):
    mu, sigma = theta
    if 0 < mu < 300 and 0 < sigma < 50:
        return 0.0
    return -np.inf


def log_probability(theta, data):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, data)

# 3) MCMC örnekleyici
initial = [140, 5]
n_walkers = 32
n_dim = 2

pos = initial + 1e-4 * np.random.randn(n_walkers, n_dim)

sampler = emcee.EnsembleSampler(n_walkers, n_dim, log_probability, args=(data,))
sampler.run_mcmc(pos, 2000, progress=True)

# 4) Örnekleri toplama
flat_samples = sampler.get_chain(discard=500, thin=15, flat=True)

# 5) Özet istatistikler
mu_samples = flat_samples[:, 0]
sigma_samples = flat_samples[:, 1]

mu_q16, mu_med, mu_q84 = np.percentile(mu_samples, [16, 50, 84])
sigma_q16, sigma_med, sigma_q84 = np.percentile(sigma_samples, [16, 50, 84])

mu_abs_error = abs(mu_med - true_mu)
sigma_abs_error = abs(sigma_med - true_sigma)

print("=== PARAMETRE SONUÇLARI ===")
print(f"mu (Parlaklık) -> Median: {mu_med:.4f}, %16: {mu_q16:.4f}, %84: {mu_q84:.4f}, Mutlak Hata: {mu_abs_error:.4f}")
print(f"sigma (Hata Payı) -> Median: {sigma_med:.4f}, %16: {sigma_q16:.4f}, %84: {sigma_q84:.4f}, Mutlak Hata: {sigma_abs_error:.4f}")

# 6) Corner plot
fig = corner.corner(
    flat_samples,
    labels=[r"$\mu$ (Parlaklık)", r"$\sigma$ (Hata)"],
    truths=[true_mu, true_sigma],
    show_titles=True,
)
plt.savefig("corner_plot.png", dpi=300, bbox_inches="tight")
plt.show()

# 7) Trace plot
samples_chain = sampler.get_chain()
fig, axes = plt.subplots(2, figsize=(10, 6), sharex=True)
axes[0].plot(samples_chain[:, :, 0], alpha=0.3)
axes[0].axhline(true_mu, linestyle="--")
axes[0].set_ylabel("mu")

axes[1].plot(samples_chain[:, :, 1], alpha=0.3)
axes[1].axhline(true_sigma, linestyle="--")
axes[1].set_ylabel("sigma")
axes[1].set_xlabel("Adım")

plt.tight_layout()
plt.savefig("trace_plot.png", dpi=300, bbox_inches="tight")
plt.show()
