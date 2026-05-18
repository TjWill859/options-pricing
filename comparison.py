import numpy as np
from black_scholes import black_scholes
from monte_carlos import monte_carlo

# Fixed parameters
S, K, T, r = 100, 100, 1, 0.05

# Vary sigma
sigmas = [0.1, 0.2, 0.3, 0.4, 0.5]

print(f"{'Sigma':>8} {'BS Call':>10} {'MC Call':>10} {'Difference':>12}")
print("-" * 44)

for sigma in sigmas:
    bs = black_scholes(S, K, T, r, sigma, 'call')
    mc = monte_carlo(S, K, T, r, sigma, option_type='call')
    # YOUR CODE: print a formatted row with sigma, bs, mc, and abs(bs - mc)
    print(f"{sigma:>8.1f} {bs:>10.4f} {mc:>10.4f} {abs(bs - mc):>12.4f}")

# Vary T (time to expiry)
sigma = 0.2
times = [0.25, 0.5, 1.0, 1.5, 2.0]
# YOUR CODE: same structure, fix sigma=0.2, loop over T
print("\n" + f"{'Time':>8} {'BS Call':>10} {'MC Call':>10} {'Difference':>12}")
print("-" * 44)
for T in times:
    bs = black_scholes(S, K, T, r, 0.2, 'call')
    mc = monte_carlo(S, K, T, r, 0.2, option_type='call')
    print(f"{T:>8.2f} {bs:>10.4f} {mc:>10.4f} {abs(bs - mc):>12.4f}")

# Vary K (strike price)  
T = 1
strikes = [80, 90, 100, 110, 120]
# YOUR CODE: same structure, fix sigma=0.2, T=1, loop over K
print("\n" + f"{'Strike':>8} {'BS Call':>10} {'MC Call':>10} {'Difference':>12}")
print("-" * 44)
for K in strikes:
    bs = black_scholes(S, K, T, r, 0.2, 'call')
    mc = monte_carlo(S, K, T, r, 0.2, option_type='call')
    print(f"{K:>8} {bs:>10.4f} {mc:>10.4f} {abs(bs - mc):>12.4f}")