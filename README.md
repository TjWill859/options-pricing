# European Options Pricing: Black-Scholes vs Monte Carlo

A Python implementation comparing two approaches to pricing European options.

## What it does
- Implements the **Black-Scholes** closed-form formula for exact option pricing
- Implements a **Monte Carlo simulation** using Geometric Brownian Motion
- Compares both models across varying volatility, time to expiry, and strike price
- Analyzes Monte Carlo convergence toward the Black-Scholes benchmark

## Files
| File | Description |
|------|-------------|
| `black_scholes.py` | Black-Scholes formula implementation |
| `monte_carlos.py` | Monte Carlo simulation implementation |
| `comparison.py` | Price comparison tables across inputs |
| `plots.py` | Visualization of comparisons and convergence |
| `options_pricing.ipynb` | Full write-up and results in Jupyter notebook |

## Usage
```bash
pip install numpy scipy matplotlib
jupyter notebook options_pricing.ipynb
```

## Key Results
- Both models agree to within ~\$0.05-0.15 at 100,000 simulations
- Monte Carlo error decays at the theoretical 1/√N rate
- Option prices rise with volatility and time, fall with higher strike prices
