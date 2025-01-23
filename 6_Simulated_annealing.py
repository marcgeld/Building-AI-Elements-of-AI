import math
import random

import numpy as np

N = 100      # Storlek på landskapet (N x N)
steps = 3000 # Antal iterationer
tracks = 50  # Antal söktrådar

# Generera ett landskap med multipla lokala optima
def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N - x0) * np.pi) + np.sin((y/N - y0) * np.pi) + \
           0.07 * np.cos(12 * (x/N - x0) * np.pi) + 0.07 * np.cos(12 * (y/N - y0) * np.pi)

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

# Startpunkter för söktrådarna
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def main():
    global x, y

    T_max = 10  # Starttemperatur
    alpha = 2   # Avkylningshastighet

    for step in range(steps):
        # Simulated annealing temperatur
        T = T_max * ((steps - step) / steps) ** alpha

        for i in range(tracks):
            # Dynamisk rörelsebaserad på temperatur
            move_range = max(1, int(T / 2))  # Stor rörelse vid hög T, små vid låg T
            x_new = np.clip(x[i] + np.random.randint(-move_range, move_range + 1), 0, N-1)
            y_new = np.clip(y[i] + np.random.randint(-move_range, move_range + 1), 0, N-1)

            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            # Simulated annealing acceptansregel
            if S_new > S_old or random.random() < math.exp((S_new - S_old) / T):
                x[i], y[i] = x_new, y_new

    # Antal spår som hittar toppunkten
    print(sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)]))

main()