#!/usr/bin/env python


from genepy import genepy

if __name__ == '__main__':
    # initiate class
    gp = genepy(10)

    # add user defined rules with rule methods
    # Counting Rules
    gp.contains("p1")
    gp.contains("p2")
    gp.contains("p3")
    gp.exactly("p4", 2)
    gp.morethan("p5", 1)

    # Positioning Rules
    gp.some_before("p2", "p3")
    gp.endswith("p5")
    gp.startswith("p1")

    # Interaction Rules
    gp.induces("p1", "p3")
    gp.drives("p3", "p2")

    # print out generated solutions that satisfy rules
    print(gp.rules["induces"])
    outputs = gp.generate(1)

    print(outputs)

    gp.solutionsToFile("test_solutions.json")
    gp.rulesToFile("test_rules.json")
