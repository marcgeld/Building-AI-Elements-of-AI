import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200, -50, 5000, 100],
              [2000, -250, -100, 150, 250],
              [3000, -100, -150, 0, 150]])


def find_best(X, y, c):
    errors = []
    for coeff in c:
        y_hat = X @ coeff
        error = (sum((y - y_hat) ** 2))
        errors.append(error)
    best_index = np.argmin(errors)
    print("the best set is set %d" % best_index)


"""

def find_best(X, y, c):
    smallest_error = np.inf
    best_index = -1
    for coeff in c:
        err = 0
        for i in range(0, len(y)):
            err += (y[i] - np.dot(X[i], coeff)) ** 2
        if err < smallest_error:
            smallest_error = err
            best_index = i - 1
    print("the best set is set %d" % best_index)
"""

find_best(X, y, c)
