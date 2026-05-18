import numpy as np

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