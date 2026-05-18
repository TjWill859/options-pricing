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

S = 100      # stock at $100
K = 100      # at-the-money (strike = stock price)
T = 1        # 1 year
r = 0.05     # 5% risk-free rate
sigma = 0.2  # 20% volatility

if __name__ == "__main__":
    
    call = black_scholes(S, K, T, r, sigma, 'call')
    put = black_scholes(S, K, T, r, sigma, 'put')

    lhs = call - put
    rhs = S - K * np.exp(-r * T)

    print(f"C - P = {lhs:.4f}")
    print(f"S - Ke^(-rT) = {rhs:.4f}")
    print(f"Parity holds: {abs(lhs - rhs) < 1e-10}")