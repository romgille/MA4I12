#!/usr/bin/python3

import matplotlib.pyplot as plt
from math import *
import numpy as np

def binom(n,p):
    """
    Return the binomial coefficient for values n, p
    """
    return factorial(n) / ( factorial(p) * factorial(n-p) )

def bernstein(n, i, t):
    """
    Return the Bernstein formula for a value t
    """
    return binom(n, i) * t ** i * (1 - t) ** (n-i)

def bezier(pts):
    """
    Return an array of points representing the Bezier curve
    """
    return [ point(pts, t) for t in np.linspace(0, 1, 100) ]

def point(pts, t):
    """
    Apply the Bernstein formula on the points' coordinates
    for a given t value
    Return a point which is the sum of all coordinates
    """
    n = len(pts)
    x = [ pts[i][0] * bernstein(n-1, i, t) for i in range(n) ]
    y = [ pts[i][1] * bernstein(n-1, i, t) for i in range(n) ]
    return ( sum(x), sum(y) )

def drawPts(pts):
    """
    Draw the points
    Label each point Pi and mark them with a red cross
    """
    x, y = zip(*pts)
    for i in range( len(pts) ):
        plt.annotate("P" + str(i), (x[i], y[i]))
    plt.scatter(x, y, s=10, marker="x", c="red")

def draw(pts):
    """
    Draw a curve from an array of points
    """
    x, y = zip(*pts)
    plt.plot(x, y)

if __name__ == '__main__' :
    a = 0
    b = 10
    #control points
    pts = [ ( (2 * i) + 1, sin((2 * i) + 1) ) for i in range( a, b+1 ) ]
    #draw the control points and the line linking each ones
    drawPts(pts)
    draw(pts)
    #draw the Bezier curve
    draw(bezier(pts))

    plt.show()
