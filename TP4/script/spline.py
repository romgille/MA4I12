#!/usr/bin/python3

import matplotlib.pyplot as plt
from math import *
import numpy as np

"""

██╗  ██╗███████╗██████╗ ███╗   ███╗██╗████████╗███████╗
██║  ██║██╔════╝██╔══██╗████╗ ████║██║╚══██╔══╝██╔════╝
███████║█████╗  ██████╔╝██╔████╔██║██║   ██║   █████╗  
██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║   ██╔══╝  
██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║   ██║   ███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚══════╝

"""                                                      

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
        

"""

███████╗██████╗ ██╗     ██╗███╗   ██╗███████╗███████╗
██╔════╝██╔══██╗██║     ██║████╗  ██║██╔════╝██╔════╝
███████╗██████╔╝██║     ██║██╔██╗ ██║█████╗  ███████╗
╚════██║██╔═══╝ ██║     ██║██║╚██╗██║██╔══╝  ╚════██║
███████║██║     ███████╗██║██║ ╚████║███████╗███████║
╚══════╝╚═╝     ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝

"""

def vecteurB (Y, d, n):
    b = [ (3/d) * (Y[1]-Y[0]) ]
    for i in range(2, n):
        b.append( (3/d) * (Y[i] - Y[i-2]) )
    b.append( (3/d) * (Y[n-1] - Y[n-2]) )
    return b

def matriceM(n):
    M = [[0 for x in range(n)] for y in range(n)]    
    M[0][0] = M[n-1][n-1] = 2
    M[0][1] = M[n-1][n-2] = 1
    
    for i in range(1, n-1):
        M[i][i] = 4
        M[i][i+1] = M[i][i-1] = 1
        
    return M
    
def vecteurV(M, B):
    return np.linalg.solve(M, B)

def main():
    a = 0
    b = 12
    n = 4
    
    l = np.linspace(a, b, n)
    d = (b-a) / n
    X = [ 0, 3, 6, 9 ]
    Y = [ 0, 4, 11, 15 ]
    M = matriceM(n)
    B = vecteurB(Y, d, n)
    V = vecteurV(M, B)
    print(M)
    print(B)
    print(V)
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

if __name__ == '__main__' :
    main()


