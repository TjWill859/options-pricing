import subprocess
import time
from monte_carlos import monte_carlo

S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
option_type = "call"

sim_counts = [1_000, 10_000, 100_000, 1_000_000, 5_000_000]
n_trials = 5

python_times = []
cpp_times = []

for n in sim_counts:
    min_python_time = float('inf')
    for _ in range(n_trials):
        start = time.perf_counter()
        monte_carlo(S, K, T, r, sigma, n, option_type)
        elapsed = (time.perf_counter() - start) * 1000
        min_python_time = min(min_python_time, elapsed)
    python_times.append(min_python_time)

    min_cpp_time = float('inf')
    for _ in range(n_trials):
        result = subprocess.run(["./monte_carlo", str(n)], capture_output=True, text=True)
        price_str, time_str = result.stdout.strip().split(",")
        elapsed = float(time_str)
        min_cpp_time = min(min_cpp_time, elapsed)
    cpp_times.append(min_cpp_time)

    print(f"N={n}: Python={python_times[-1]:.2f}ms, C++={cpp_times[-1]:.2f}ms")