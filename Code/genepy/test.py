#!/usr/bin/env python


from genepy import genepy

if __name__ == '__main__':
    # initiate class
    gp = genepy(10)

    # add user defined rules with rule methods
    # Counting Rules
    gp.contains("p1")
    gp.exactly("p2", 2)
    gp.morethan("p3", 1)

    # Positioning Rules
    gp.some_before("p2", "p3")
    gp.endswith("p3")

    # Interaction Rules
    gp.induces("p1", "p3")

    # print out generated solutions that satisfy rules
    print(gp.rules["induces"])
    outputs = gp.generate(5)

    print(outputs)

    gp.solutionsToFile("test_solutions.json")
    gp.rulesToFile("test_rules.json")
