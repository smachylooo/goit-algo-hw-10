import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

def f(x: float) -> float:
    return x ** 2

def monte_carlo_integral(func, a: float, b: float, num_points: int = 100_000) -> float:
    total = 0

    for _ in range(num_points):
        x = random.uniform(a, b)
        total += func(x)

    return (b - a) * total / num_points

def build_plot(a: float, b: float, filename: str = "integral_plot.png") -> None:
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Integral of f(x) = x^2 from {a} to {b}")
    plt.grid()
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    a = 0
    b = 2
    num_points = 100_000
    monte_carlo_result = monte_carlo_integral(f, a, b, num_points)
    quad_result, quad_error = spi.quad(f, a, b)
    analytical_result = (b ** 3) / 3 - (a ** 3) / 3
    build_plot(a, b)
    print(f"Monte Carlo result: {monte_carlo_result}")
    print(f"Quad result: {quad_result}")
    print(f"Quad error estimate: {quad_error}")
    print(f"Analytical result: {analytical_result}")
    print(f"Absolute difference Monte Carlo vs quad: {abs(monte_carlo_result - quad_result)}")
    print("Plot saved as integral_plot.png")
