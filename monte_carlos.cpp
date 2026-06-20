#include <iostream>
#include <cmath>
#include <random>
#include <chrono>
#include <string>

double monte_carlo(double S, double K, double T, double r, double sigma,
                    long n_simulations, const std::string& option_type) {

    std::mt19937 generator(42);
    std::normal_distribution<double> dist(0.0, 1.0);

    double drift = (r - 0.5 * sigma * sigma) * T;
    double diffusion = sigma * std::sqrt(T);
    double payoff_sum = 0.0;

    for (long i = 0; i < n_simulations; ++i) {
        double Z = dist(generator);
        double S_T = S * std::exp(drift + Z * diffusion);

        double payoff = 0.0;
        if (option_type == "call") {
            payoff = std::max(S_T - K, 0.0);
        } else if (option_type == "put") {
            payoff = std::max(K - S_T, 0.0);
        }

        payoff_sum += payoff;
    }

    double price = (payoff_sum / n_simulations) * std::exp(-r * T);
    return price;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <n_simulations>" << std::endl;
        return 1;
    }

    long n_simulations = std::stol(argv[1]);
    double S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2;

    auto start = std::chrono::high_resolution_clock::now();
    double price = monte_carlo(S, K, T, r, sigma, n_simulations, "call");
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed_us = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    double elapsed_ms = elapsed_us / 1000.0;

    std::cout << price << "," << elapsed_ms << std::endl;

    return 0;
}