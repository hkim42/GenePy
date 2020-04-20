#!/usr/bin/env python

from genepy import genepy

if __name__ == '__main__':
    gp = genepy(5)
    gp.some_after("p1",["h1","h2","h3"])
    print(gp.rules)
