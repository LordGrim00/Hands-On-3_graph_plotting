import timeit
import matplotlib.pyplot as plt
import numpy as np
from merge_sort import test_merge_sort  # Importing the merge sort test function

# Task 1: Function f(n) for runtime analysis
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1
    return x

# Task 2: Time the function for various n and plot the time vs n
def time_function():
    n_values = list(range(1, 501))  # Choose a suitable range for n
    times = []

    # Measure execution time for each n
    for n in n_values:
        time_taken = timeit.timeit(lambda: f(n), number=10)
        times.append(time_taken)

    return n_values, times

# Task 3: Fit a polynomial and find bounds
def fit_polynomial(n_values, times):
    # Fit a polynomial curve
    coefficients = np.polyfit(n_values, times, 2)  # Fitting a quadratic curve
    polynomial = np.poly1d(coefficients)
    
    return polynomial, coefficients

# Task 4: Zoom into the plot to find n₀
def find_n0_plot(n_values, times):
    return n_values[:50], times[:50]

if __name__ == "__main__":
    print("Timing function f(n)...")
    n_values, times = time_function()

    print("Fitting a polynomial to the data...")
    polynomial, coefficients = fit_polynomial(n_values, times)

    print("Zooming in to find n₀...")
    n_zoomed, times_zoomed = find_n0_plot(n_values, times)

    # Plotting all in one figure
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))  # 3 subplots in one figure

    # Plot 1: Time vs n
    axs[0].plot(n_values, times, label='Execution Time', color='blue')
    axs[0].set_title('Time vs n for function f(n)')
    axs[0].set_xlabel('n')
    axs[0].set_ylabel('Time (seconds)')
    axs[0].legend()

    # Plot 2: Time vs n with polynomial fit
    axs[1].plot(n_values, times, label='Original Time Data', color='blue')
    axs[1].plot(n_values, polynomial(n_values), label='Fitted Polynomial Curve', linestyle='--', color='red')
    axs[1].set_title('Time vs n with Polynomial Fit')
    axs[1].set_xlabel('n')
    axs[1].set_ylabel('Time (seconds)')
    axs[1].legend()

    # Plot 3: Zoomed view for n₀
    axs[2].plot(n_zoomed, times_zoomed, label='Zoomed Execution Time', color='green')
    axs[2].set_title('Zoomed Time vs n (Finding n₀)')
    axs[2].set_xlabel('n')
    axs[2].set_ylabel('Time (seconds)')
    axs[2].legend()

    # Adjust layout for better readability
    plt.tight_layout()
    plt.show()

    print("Testing merge sort on array [5, 2, 4, 7, 1, 3, 2, 6]...")
    test_merge_sort()
