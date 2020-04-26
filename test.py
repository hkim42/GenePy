#!/usr/bin/env python

from genepy import genepy

if __name__ == '__main__':
    gp = genepy(5)
    gp.contains("p1")
    gp.morethan("p3", 1)
    gp.exactly("p5", 1)

    gp.some_before("p3", "p1")
    gp.endswith("p5")

    gp.induces("p1", "p3")
    print(gp.rules["induces"])
    outputs = gp.generate(2)

    for x in outputs:
        print(x)
