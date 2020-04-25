#!/usr/bin/env python

from genepy import genepy
from z3 import *

if __name__ == '__main__':
    x = Int('x')
    y = Int('y')
    solve(x > 2, y < 10, x + 2*y == 7)
    #gp = genepy(5)
    #gp.some_after("p1",["h1","h2","h3"])
    #print(gp.rules)
