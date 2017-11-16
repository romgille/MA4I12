#!/usr/bin/python3

import matplotlib.pyplot as plot

def phi1(x):
    if x <= 0 or x >= 1:
        return 0
    return (x - 1)**2 * (2 * x + 1)


def phi2(x):
    if x <= 0 or x >= 1:
        return 0
    return x**2 * (3 - 2 * x)


def phi3(x):
    if x <= 0 or x >= 1:
        return 0
    return x * (x - 1)**2


def phi4(x):
    if x <= 0 or x >= 1:
        return 0
    return x**2 * (x - 1)


def foncHermite(X, Y, V, x):
    xParam = (x - X[0])/(X[1] - X[0])
    p = Y[0] * phi1(xParam) + Y[1] * phi2(xParam)
    + (X[1] - X[0]) * (V[0] * phi3(xParam) + V[1] * phi4(xParam))
    return p


def draw(value):
    return plot.plot(value)


def main():
    X = [1, 5]
    Y = [6, 2]
    V = [3/2, -3]
    foncHermite(X, Y, V, 3)


main()
