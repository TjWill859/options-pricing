import numpy as np
import matplotlib.pyplot as plt
from black_scholes import black_scholes
from monte_carlos import monte_carlo

S, r = 100, 0.05

# --- Recalculate the data ---
sigmas  = [0.1, 0.2, 0.3, 0.4, 0.5]
times   = [0.25, 0.5, 1.0, 1.5, 2.0]
strikes = [80, 90, 100, 110, 120]

bs_sigmas  = [black_scholes(S, 100, 1, r, s, 'call') for s in sigmas]
mc_sigmas  = [monte_carlo(S, 100, 1, r, s, option_type='call') for s in sigmas]

bs_times   = [black_scholes(S, 100, t, r, 0.2, 'call') for t in times]
mc_times   = [monte_carlo(S, 100, t, r, 0.2, option_type='call') for t in times]

bs_strikes = [black_scholes(S, k, 1, r, 0.2, 'call') for k in strikes]
mc_strikes = [monte_carlo(S, k, 1, r, 0.2, option_type='call') for k in strikes]

# --- Plot ---
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Subplot 1 — vary sigma
axes[0].plot(sigmas, bs_sigmas, 'b-o', label='Black-Scholes')
axes[0].plot(sigmas, mc_sigmas, 'r--o', label='Monte Carlo')
axes[0].set_xlabel('Volatility (σ)')
axes[0].set_ylabel('Call Price ($)')
axes[0].set_title('Price vs Volatility')
axes[0].legend()

# Subplot 2 — vary T
# YOUR CODE: same structure using axes[1], times, bs_times, mc_times
axes[1].plot(times, bs_times, 'b-o', label='Black-Scholes')
axes[1].plot(times, mc_times, 'r--o', label='Monte Carlo')
axes[1].set_xlabel('Time to Maturity (T)')
axes[1].set_ylabel('Call Price ($)')
axes[1].set_title('Price vs Time to Maturity')
axes[1].legend()

# Subplot 3 — vary K
# YOUR CODE: same structure using axes[2], strikes, bs_strikes, mc_strikes
axes[2].plot(strikes, bs_strikes, 'b-o', label='Black-Scholes')
axes[2].plot(strikes, mc_strikes, 'r--o', label='Monte Carlo')
axes[2].set_xlabel('Strike Price (K)')
axes[2].set_ylabel('Call Price ($)')
axes[2].set_title('Price vs Strike Price')
axes[2].legend()

plt.suptitle('Black-Scholes vs Monte Carlo', fontsize=14)
plt.tight_layout()
plt.show()


bs_ref = black_scholes(100, 100, 1, 0.05, 0.2, 'call')

sim_counts = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000, 500_000]
errors = []

for n in sim_counts:
    mc = monte_carlo(100, 100, 1, 0.05, 0.2, n_simulations=n, option_type='call')
    errors.append(abs(mc - bs_ref))

plt.figure(figsize=(9, 5))
plt.loglog(sim_counts, errors, 'b-o', label='MC Error')

# This line shows the theoretical 1/√N decay rate — the expected convergence speed
n_range = np.linspace(100, 500_000, 1000)
plt.loglog(n_range, 1 / np.sqrt(n_range), 'r--', label='1/√N reference')

plt.xlabel('Number of Simulations')
plt.ylabel('Absolute Error ($)')
plt.title('Monte Carlo Error vs Number of Simulations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()