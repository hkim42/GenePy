from constraint import *
import json
import os

class genepy:
    def __init__(self, length: int, check_conflicts=False):
        if length < 1:
            raise Exception('invalid length')
        else:
            self.length = length

        self.check_conflicts = check_conflicts
        self.rules = {
            'morethan': {},
            'contains': {},
            'exactly': {},
            'then': {},
            'witH': {},
            'startswith': {},
            'endswith': {},
            'all_after': {},
            'some_after': {},
            'all_before': {},
            'some_before': {},
            'all_nextto': {},
            'some_nextto': {},
            'all_forward_if': {},
            'all_reverse_if': {},
            'some_forward': {},
            'some_reverse': {},
            'all_forward': {},
            'all_reverse': {},
            'represses': {},
            'induces': {},
            'drives': {}
        }
        self.problem = Problem()
        self.solutions = None

        self.containsParts = None
        self.morethanParts = None
        self.morethanValues = None
        self.exactlyParts = None
        self.exactlyValues = None
        self.thenPartsA = None
        self.thenPartsB = None

    def change_length(arg: int):
        """Change sequence length after initilization. Must be called BEFORE generating solutions."""
        if arg < 1:
            raise Exception('invalid length')
        else:
            self.length = arg

    # User methods to implement Eugene rules
    # Counting Rules
    def morethan(self, a: str, n: int):
        """a MORETHAN n --> morethan(a, n)"""
        if n > self.length or n < 1:
            raise Exception('invalid n')
        else:
            self.rules['morethan'][a] = n

    def contains(self, a: str):
        """CONTAINS a --> contains(a)"""
        self.rules['contains'][a] = True

    def exactly(self, a: str, n: int):
        """a EXACTLY n --> exactly(a, n) """
        if n > self.length:
            raise Exception('invalid n: n must be less than or equal to N')
        else:
            self.rules['exactly'][a] = n

    def then(self, a: str, B: str):
        """a THEN B --> then(a, B)"""
        self.rules['then'][a] = B

    def witH(self, a: str, B: str):
        """a WITH B ---> witH(a, B)"""
        self.rules['witH'][a] = B

    # Positioning Rules
    def startswith(self, a: str):
        """STARTSWITH a --> startswith(a) """
        self.rules['startswith'][a] = True

    def endswith(self, a: str):
        """ENDSWITH a --> endswith(a)"""
        self.rules['endswith'][a] = True

    def all_after(self, a: str, B: list):
        """a ALL_AFTER B / a AFTER B --> all_after(a, B)"""
        self.rules['all_after'][a] = B

    def some_after(self, a: str, B: list):
        """a SOME_AFTER B --> some_after(a, B)"""
        self.rules['some_after'][a] = B

    def all_before(self, a: str, B: list):
        """a ALL_BEFORE B --> all_before(a, B)"""
        self.rules['all_before'][a] = B

    def some_before(self, a: str, B: list):
        """a SOME_BEFORE B --> some_before(a, B)"""
        self.rules['some_before'][a] = B

    def all_nextto(self, a: str, B: list):
        """a ALL_NEXTTO B --> all_nextto(a, B)"""
        self.rules['all_nextto'][a] = B

    def some_nextto(self, a: str, B: list):
        """a SOME_NEXTTO B --> some_nextto(a, B)"""
        self.rules['some_nextto'][a] = B

    # Orientation Rules
    def all_forward_if(self, a: str):
        """ALL_FORWARD a --> all_forward(a)"""
        self.rules['all_forward_if'][a] = True

    def all_reverse_if(self, a: str):
        """ALL_REVERSE a --> all_reverse_if(a)"""
        self.rules['all_reverse_if'][a] = True

    def some_forward(self, a: str):
        """SOME_FORWARD a --> some_forward(a)"""
        self.rules['some_forward'][a] = True

    def some_reverse(self, a: str):
        """SOME_REVERSE a --> some_reverse(a)"""
        self.rules['some_reverse'][a] = True

    def all_forward(self):
        """ALL_FORWARD --> all_forward()"""
        self.rules['all_forward'] = True

    def all_reverse(self):
        """ALL_REVERSE --> all_reverse()"""
        self.rules['all_reverse'] = True

    # Interaction Rules
    def represses(self, a: str, B: str):
        """g REPRESSES p --> represses(g, p)"""
        self.rules['represses'][a] = B

    def induces(self, a: str, B: str):
        """a INDUCES B --> induces(a, B)"""
        self.rules['induces'][a] = B

    def drives(self, a: str, B: str):
        """a DRIVES B --> drives(a, B)"""
        self.rules['drives'][a] = B


    # Constraint methods for python-constraint solver
    # Not inteded for user
    def containsConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'contains()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        parts = self.containsParts
        count = 0
        for x in range(len(parts)):
            if parts[x] in variables:
                count += 1
        if count == len(parts):
            return True
        else:
            return False

    def morethanConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'morethan()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        parts = self.morethanParts
        n = self.morethanValues
        count = 0
        for x in range(len(parts)):
            if variables.count(parts[x]) > n[x]:
                count += 1
        if count == len(parts):
            return True
        else:
            return False

    def exactlyConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'exactly()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        parts = self.exactlyParts
        n = self.exactlyValues
        count = 0
        for x in range(len(parts)):
            if variables.count(parts[x]) == n[x]:
                count += 1
        if count == len(parts):
            return True
        else:
            return False

    def thenConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'then()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        partsA = self.thenPartsA
        partsB = self.thenPartsB
        count = 0
        for x in range(len(partsA)):
            if partsA[x] in variables:
                if partsB[x] in variables:
                    count += 1
        if count == len(partsA):
            return True
        else:
            return False

    def withConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'witH()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        partsA = self.witHPartsA
        partsB = self.witHPartsB
        count = 0
        for x in range(len(partsA)):
            if (partsA[x] in variables) and (partsB[x] in variables):
                if partsB in variables:
                    count += 1
        if count == len(partsA):
            return True
        else:
            return False

    def startswithConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'startswith()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        ruleList = list(self.rules["startswith"].keys())
        if len(ruleList) > 1:
            print("startswith used on multiple parts")
            return False
        if ruleList[0] in variables:
            if variables[0] == ruleList[0]:
                return True
            else:
                return False

    def endswithConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'endswith()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        ruleList = list(self.rules["endswith"].keys())
        if len(ruleList) > 1:
            print("endswith used on multiple parts")
            return False
        if ruleList[0] in variables:
            if variables[len(variables)-1] == ruleList[0]:
                return True
            else:
                return False

    def all_afterConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'all_after()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        partsA = list(self.rules["all_after"].keys())
        partsB = list(self.rules["all_after"].values())
        firstA = None
        lastB = None
        for x in range(len(variables)):
            done = False
            for i in range(len(partsA)):
                if partsA[i] == variables[x]:
                    firstA = x
                    done = True
                    break
            if done:
                break

        for x in range(len(variables)):
            for i in range(len(partsB)):
                if partsB[i] == variables[x]:
                    lastB = x
        if lastB < firstA:
            return True
        else:
            return False

    def some_afterConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'some_after()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        partsA = list(self.rules["some_after"].keys())
        partsB = list(self.rules["some_after"].values())
        foundA = []
        foundB = []
        for x in range(len(variables)):
            if variables[x] in partsA:
                foundA.append(x)
            if variables[x] in partsB:
                foundB.append(x)
        for a in foundA:
            for b in foundB:
                if b < a:
                    return True
        return False

    def all_beforeConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'all_before()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        partsA = list(self.rules["all_before"].keys())
        partsB = list(self.rules["all_before"].values())
        firstB = None
        lastA = None
        for x in range(len(variables)):
            done = False
            for i in range(len(partsB)):
                if partsB[i] == variables[x]:
                    firstB = x
                    done = True
                    break
            if done:
                break

        for x in range(len(variables)):
            for i in range(len(partsA)):
                if partsA[i] == variables[x]:
                    lastA = x
        if lastA < firstB:
            return True
        else:
            return False

    def some_beforeConstraint(self, *argv):
        """Returns True if potential sequence satifies all 'some_before()' constraints desribed by user."""
        variables = []
        for arg in argv:
            variables.append(arg)
        partsA = list(self.rules["some_before"].keys())
        partsB = list(self.rules["some_before"].values())
        foundA = []
        foundB = []
        for x in range(len(variables)):
            if variables[x] in partsA:
                foundA.append(x)
            if variables[x] in partsB:
                foundB.append(x)
        for a in foundA:
            for b in foundB:
                if a < b:
                    return True
        return False

    def generate(self, number=0):
        """Return all sequences that satifies user described constraints. If not given a number for sequences method returns all solutions."""
        # Create domain for each position in sequence using Counting rules
        self.containsParts = list(self.rules["contains"].keys())
        self.morethanParts = list(self.rules["morethan"].keys())
        self.morethanValues = list(self.rules["morethan"].values())
        self.exactlyParts = list(self.rules["exactly"].keys())
        self.exactlyValues = list(self.rules["exactly"].values())
        self.thenPartsA = list(self.rules["then"].keys())
        self.thenPartsB = list(self.rules["then"].values())
        self.witHPartsA = list(self.rules["witH"].keys())
        self.witHPartsB = list(self.rules["witH"].values())
        domain = self.morethanParts + self.containsParts + self.exactlyParts + self.thenPartsA + self.thenPartsB + self.witHPartsA + self.witHPartsB
        self.problem.addVariables(range(self.length), domain)

        # If certain rule was implemented by user, then apply to solver
        if self.rules["contains"]:
            self.problem.addConstraint(self.containsConstraint, list(range(self.length)))
        if self.rules["morethan"]:
            self.problem.addConstraint(self.morethanConstraint, list(range(self.length)))
        if self.rules["exactly"]:
            self.problem.addConstraint(self.exactlyConstraint, list(range(self.length)))
        if self.rules["then"]:
            self.problem.addConstraint(self.thenConstraint, list(range(self.length)))
        if self.rules["witH"]:
            self.problem.addConstraint(self.withConstraint, list(range(self.length)))
        if self.rules["startswith"]:
            self.problem.addConstraint(self.startswithConstraint, list(range(self.length)))
        if self.rules["endswith"]:
            self.problem.addConstraint(self.endswithConstraint, list(range(self.length)))
        if self.rules["all_after"]:
            self.problem.addConstraint(self.all_afterConstraint, list(range(self.length)))
        if self.rules["some_after"]:
            self.problem.addConstraint(self.some_afterConstraint, list(range(self.length)))
        if self.rules["all_before"]:
            self.problem.addConstraint(self.all_beforeConstraint, list(range(self.length)))
        if self.rules["some_before"]:
            self.problem.addConstraint(self.some_beforeConstraint, list(range(self.length)))

        # Return solutions
        if number == 0:
            self.solutions = self.problem.getSolution()
            return self.solutions
        elif number == 1:
            solver = MinConflictsSolver()
            self.problem.setSolver(solver)
            while self.solutions == None:
                self.solutions = self.problem.getSolution()
            return self.solutions
        else:
            self.solutions = self.problem.getSolutions()
            return self.solutions[0:number]

    def solutionsToFile(self, filename, number=0):
        """Write generated solutions to json file. If not given a number all solutions are written to the file"""
        fileCheck = os.path.splitext(filename)
        if fileCheck[1] != ".json":
            raise Exception("Filename must be of type json")
        path = "./Solutions/" + filename

        f = open(path, "w")
        if number == 0:
            json.dump(self.solutions, f)
            f.close()
        else:
            json.dump(self.solutions[0:number], f)
            f.close()

    def rulesToFile(self, filename):
        """Write rules to json file."""
        fileCheck = os.path.splitext(filename)
        if fileCheck[1] != ".json":
            raise Exception("Filename must be of type json")
        path = "./Rules/" + filename

        f = open(path, "w")
        json.dump(self.rules, f)
        f.close()
