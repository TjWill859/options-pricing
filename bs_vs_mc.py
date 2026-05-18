import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, options_type='call'):
    """Calculate the Black-Scholes price of a European call option."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if options_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif options_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("options_type must be 'call' or 'put'")
    return price

def monte_carlo(S, K, T, r, sigma, n_simulations=100_000, option_type='call'):

    Z = np.random.normal(0, 1, n_simulations)

    S_T = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    if option_type == 'call':
        payoffs = np.maximum(S_T - K, 0)
    elif option_type == 'put':
        payoffs = np.maximum(K - S_T, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    price = np.mean(payoffs) * np.exp(-r * T)
    return price

S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2

bs_call = black_scholes(S, K, T, r, sigma, 'call')
bs_put  = black_scholes(S, K, T, r, sigma, 'put')

mc_call = monte_carlo(S, K, T, r, sigma, option_type='call')
mc_put  = monte_carlo(S, K, T, r, sigma, option_type='put')

print(f"{'':10} {'Black-Scholes':>15} {'Monte Carlo':>15} {'Difference':>12}")
print(f"{'Call':10} {bs_call:>15.4f} {mc_call:>15.4f} {abs(bs_call-mc_call):>12.4f}")
print(f"{'Put':10} {bs_put:>15.4f} {mc_put:>15.4f} {abs(bs_put-mc_put):>12.4f}")