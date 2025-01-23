import math
import numpy as np

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

x = np.array([4, 3, 0])

c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

coeffs = {"c1": c1, "c2": c2, "c3": c3}
outputs = {}

for k, c in coeffs.items():
    z = x @ c
    print(sigmoid(z))
