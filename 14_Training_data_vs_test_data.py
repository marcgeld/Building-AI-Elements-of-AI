from io import StringIO

import numpy as np

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''


def main():
    np.set_printoptions(precision=1)  # this just changes the output settings for easier reading
    data_train = np.genfromtxt(StringIO(train_string), skip_header=1)
    y_train = data_train[:, 5].reshape(1, -1)[0]
    x_train = np.delete(data_train, 5, axis=1)
    c = np.linalg.lstsq(x_train, y_train)[0]

    # read in the test data and separate x_test from it
    data_test = np.genfromtxt(StringIO(test_string), skip_header=1)
    #y_test = data_train[:, 5].reshape(1, -1)[0]
    x_test = np.delete(data_test, 5, axis=1)

    # print out the linear regression coefficients
    print(c)
    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)

main()
