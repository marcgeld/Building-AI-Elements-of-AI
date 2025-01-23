import math
import random
import numpy as np
import io
from io import StringIO
import random


def main():
    favourite = "bats"  # change this
    number = random.randint(1, 100)
    if number in range(1, 80, 1):
        favourite = 'dogs'
    elif number in range(81, 91, 1):
        favourite = 'cats'

    print("I love " + favourite)


main()