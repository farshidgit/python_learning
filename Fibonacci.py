import numpy as np


def fibon(n):  # nth Fibonachi numbebr
    result = 0
    if (n == 0) or (n == 1):
        result = 1
        return result
    elif n > 1:
        result = fibon(n-1) + fibon(n-2)
        return result

print fibon(7)
