#!/usr/bin/python3

import matplotlib.pyplot as plt
from math import *

def binom(n,p):
    return factorial(n) / (factorial(p) * factorial(n-p))

def bernstein(n,i,t):
    return binom(n,i) * t ** i * (1 - t) ** (n-i)

def bezier(beta, n, t):
    B = 0;
    for i in range(n):
        B += beta[i] * bernstein(n,i,t)
    return B


def draw(X, Y):
    plt.plot(X, Y)

if __name__ == '__main__' :
    print( binom(5,3) )
    print(bernstein(5,5,5))

