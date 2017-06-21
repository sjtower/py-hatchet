import numpy as np


def pretty_print(array):
    print(np.matrix(array))


def create_2d_array(w, h):
    return [[0 for x in range(w)] for y in range(h)]


def rotate(array):
    rotated = list(zip(*array[::-1]))
    return rotated
