import numpy as np
from black_scholes import black_scholes
from monte_carlos import monte_carlo
import matplotlib.pyplot as plt

bs_call = black_scholes(100, 100, 1, 0.05, 0.2, 'call')

sim_counts = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000, 500_000]
mc_prices  = []

for n in sim_counts:
    mc_prices.append(monte_carlo(100, 100, 1, 0.05, 0.2, n_simulations=n, option_type='call'))
# YOUR CODE: loop through sim_counts, call monte_carlo() each time, append to mc_prices

plt.figure(figsize=(10, 5))

# YOUR CODE: plot mc_prices vs sim_counts (use plt.plot or plt.semilogx)
plt.semilogx(sim_counts, mc_prices, label='Convergence Analysis')
# YOUR CODE: add a flat horizontal line for bs_call (use plt.axhline)
plt.axhline(y=bs_call, color='r', linestyle='--', label='Black-Scholes')

plt.xlabel("Number of Simulations")
plt.ylabel("Option Price ($)")
plt.title("Monte Carlo Convergence to Black-Scholes")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()