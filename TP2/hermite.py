#!/usr/bin/python3

import matplotlib.pyplot as plt
from math import *

def phi1(x):
    if x < 0 or x > 1:
        return 0
    return (x - 1)**2 * (2 * x + 1)


def phi2(x):
    if x < 0 or x > 1:
        return 0
    return x**2 * (3 - 2 * x)


def phi3(x):
    if x < 0 or x > 1:
        return 0
    return x * (x - 1)**2


def phi4(x):
    if x < 0 or x > 1:
        return 0
    return x**2 * (x - 1)


def foncHermite(X, Y, V, x):
    P = 0
    for k in range(len(X)-1):
        d = X[k+1] - X[k]
        t = (x - X[k]) / d
        P += Y[k] * phi1(t) + Y[k+1] * phi2(t) + d * (V[k] * phi3(t) + V[k+1] * phi4(t))
    return P

def draw(X, Y, c):
    plt.plot(X, Y, color=c)

def tangentes(X, Y, V):
    for k in range(len(X)):
        Xtan = [X[k] - 1, X[k] + 1]
        Ytan = [Y[k] - V[k], V[k] + Y[k]]
        draw(Xtan, Ytan, '#ff00ff')

if __name__ == '__main__' :
    X = [1, 5, 7, 8, 10]
    Y = [6, 2, -1, 1, 2]
    V = [3/2, -3, 0, 4, 1]

    N = 500
    a = min(X)
    b = max(X)

    P = []
    Xaff = []
    Yaff = []
    for k in range(N):
        Xaff.append(a + k * (b-a)/N)
        Yaff.append(foncHermite(X, Y, V, a + k * (b-a)/N))

    tangentes(X, Y, V)

    draw(Xaff, Yaff, '#0080ff')
    plt.show()
