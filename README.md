# European Options Pricing: Black-Scholes vs Monte Carlo

A Python implementation comparing two approaches to pricing European options, with a C++ performance extension.

## What it does
- Implements the **Black-Scholes** closed-form formula for exact option pricing
- Implements a **Monte Carlo simulation** using Geometric Brownian Motion
- Compares both models across varying volatility, time to expiry, and strike price
- Analyzes Monte Carlo convergence toward the Black-Scholes benchmark
- Benchmarks a **C++ port** of the Monte Carlo simulation against the vectorized Python/NumPy version

## Files
| File | Description |
|------|-------------|
| `black_scholes.py` | Black-Scholes formula implementation |
| `monte_carlos.py` | Monte Carlo simulation implementation (Python) |
| `comparison.py` | Price comparison tables across inputs |
| `plots.py` | Visualization of comparisons and convergence |
| `monte_carlos.cpp` | Monte Carlo simulation implementation (C++), optimized and benchmarked against the Python version |
| `bench.py` | Benchmark harness comparing Python and C++ runtimes across simulation counts |
| `options_pricing.ipynb` | Full write-up and results in Jupyter notebook |

## Usage
```bash
pip install numpy scipy matplotlib
jupyter notebook options_pricing.ipynb
```

To reproduce the C++ benchmark:
```bash
g++ monte_carlos.cpp -O3 -march=native -o monte_carlo
python bench.py
```

## Key Results
- Both pricing models agree to within ~\$0.05-0.15 at 100,000 simulations
- Monte Carlo error decays at the theoretical 1/√N rate
- Option prices rise with volatility and time, fall with higher strike prices
- A compiled, optimized C++ implementation (loop-invariant hoisting, `-O3 -march=native`) was benchmarked against vectorized NumPy; **NumPy was faster at every simulation count tested**, illustrating that vectorization — not language choice alone — is often the dominant factor in numerical performance. See the notebook for full analysis.
