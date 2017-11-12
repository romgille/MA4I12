#!/usr/bin/python3

from math import *
import matplotlib.pyplot as plt
import numpy as np

def createList(a, b, n):
    """
    Return an array of n values between a and b
    """
    X = []
    step = (b - a) / n
    for i in range( n+1 ):
        X.append(a)
        a += step
    return X

def createTchebychev(a, b, n):
    """
    Return an array of n values between a and b, with the Tchebychev
    formula applied on each value
    """
    X = []
    for k in range( n+1 ) :
        x = (a+b) / 2 + (b-a) / 2 * cos( ( 2*k+1 ) * pi / (2*n+1) )
        X.append(x)
    return X

def vandermonde(X, Y, x):
    """
    Return the result of Vandermonde on arrays X, Y for a known x value
    """
    V = []
    for i in range( len(X) ):
        V.append( [ X[i] ** j for j in range( len(X) ) ] )
    A = np.linalg.inv(V).dot(Y)

    P = 0
    for i in range( len(A) ):
        P += A[i] * x ** i
    return P

def lagrange(X, Y, x):
    """
    Return the result of Lagrange on arrays X, Y for a known x value
    """
    P = 0
    for i in range( len(X) ):
        L = 1
        for j in range( len(X) ):
            if j != i:
                L = L * (x - X[j]) / (X[i] - X[j])
        P += L * Y[i]
    return P

def maxGap(Y1, Y2):
    max = 0
    for i in range( len(Y1) ) :
        gap = abs( Y1[i] - Y2[i] )
        if gap > max:
            max = gap
    return round(max,4)

def display(X, Y, P, n, labelFnt, labelP, subplotNumber):
    plt.subplot(subplotNumber)
    plt.plot(X, Y, label=labelFnt)
    plt.plot(X, P, label=labelP)
    plt.legend()
    plt.text(-1, 0.5, "Number of interpolation points: " + str(n))
    plt.text(-1, 0.35, "Maximum gap: " + str( maxGap(Y,P) ))

def displayVandermonde (a, b, fnt, label, subplotNumber, n, N):
    """
    Display a function fnt and its interpolation using
    the Vandermonde matrix on interval [a, b]
    """
    # fnt used for calculations
    xCalc = createList(a, b, n)
    yCalc = [ fnt(x) for x in xCalc ]
    # fnt used for drawing
    xDisplay = createList(a, b, N)
    yDisplay = [ fnt(x) for x in xDisplay ]
    # calc Vandermonde
    P = [ vandermonde(xCalc, yCalc, x) for x in xDisplay ]
    display(xDisplay, yDisplay, P, n, label, "Vandermonde", subplotNumber)

def displayLagrange (a, b, fnt, label, subplotNumber, n, N) :
    """
    Display a function fnt and its interpolation using
    Lagrange on interval [a, b]
    """
    # fnt used for calculations
    xCalc = createList(a, b, n)
    yCalc = [ fnt(x) for x in xCalc ]
    # fnt used for drawing
    xDisplay = createList(a, b, N)
    yDisplay = [ fnt(x) for x in xDisplay ]
    # calc Lagrange
    P = [ lagrange(xCalc, yCalc, x) for x in xDisplay ]
    display(xDisplay, yDisplay, P, n, label, "Lagrange", subplotNumber)

def displayTchebychev(a, b, fnt, label, subplotNumber, n, N):
    """
    Display a function fnt and its interpolation using
    Lagrange and the Tchebychev formula on interval [a, b]
    """
    # fnt used for calculations
    xCalc = createTchebychev(a, b, n)
    yCalc = [ fnt(x) for x in xCalc ]
    # fnt used for drawing
    xDisplay = createTchebychev(a, b, N)
    yDisplay = [ fnt(x) for x in xDisplay ]
    # calc Lagrange
    P = [ lagrange(xCalc, yCalc, x) for x in xDisplay ]
    display(xDisplay, yDisplay, P, n, label, "Tchebychev", subplotNumber)

if __name__ == '__main__' :
    displayVandermonde(-10, 10, sin, "sin(x)", 321, 12, 500)
    displayVandermonde(-1, 1, lambda x: 1/(1+10*x**2), "1 / (1+10*x**2)", 322, 12, 500)
    displayLagrange(-10, 10, sin, "sin(x)", 323, 12, 500)
    displayLagrange(-1, 1, lambda x: 1/(1+10*x**2), "1 / (1+10*x**2)", 324, 15, 500)
    displayTchebychev(-10, 10, sin, "sin(x)", 325, 12, 500)
    displayTchebychev(-1, 1, lambda x: 1/(1+10*x**2), "1 / (1+10*x**2)", 326, 15, 500)
    plt.show()
