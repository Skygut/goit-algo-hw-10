import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2 + 15 * x + 2


a = 0
b = 2
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


def function(x):
    return x**2 + 15 * x + 2


N = 1000000
random_points = np.random.uniform(a, b, N)
average_value = np.mean(function(random_points))
integral = average_value * (b - a)
print(f"Integral = {integral :.5f}")

ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 + 15x + 2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()
