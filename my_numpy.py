import numpy as np


def my_numpy_array():
    first = np.array([3, 6, 9, 12, 16])
    second = np.array([[4, 8], [12, 16], [4, 8], [120, 160], [400, 80]])
    second_transp = second.transpose()
    res = np.multiply(second_transp, first)
    return res
