from constraint import *
from EugeneConstraints import *

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

        self.sequences = []

        self.problem = Problem()
        self.constraints = EugeneConstraints()

        self.containsParts = None
        self.morethanParts = None
        self.morethanValues = None
        self.exactlyParts = None
        self.exactlyValues = None
        self.thenPartsA = None
        self.thenPartsB = None

    def change_length(arg: int):
        if arg < 1:
            raise Exception('invalid length')
        else:
            self.length = arg

    def toggle_check_conflicts(arg=None):
        if arg == None:
            self.check_conflicts = not self.check_conflicts
        else:
            if type(arg) != bool:
                raise Exception('invalid type')
            else:
                self.check_conflicts = arg

    # Counting Rules
    def morethan(self, a: str, n: int):
        if n > self.length or n < 1:
            raise Exception('invalid n')
        else:
            self.rules['morethan'][a] = n

    def contains(self, a: str):
        self.rules['contains'][a] = True

    def exactly(self, a: str, n: int):
        if n > self.length:
            raise Exception('invalid n: n must be less than or equal to N')
        else:
            self.rules['exactly'][a] = n

    def then(self, a: str, B: str):
        self.rules['then'][a] = B

    def witH(self, a: str, B: str):
        self.rules['witH'][a] = B

    # Positioning Rules
    def startswith(self, a: str):
        self.rules['startswith'][a] = True

    def endswith(self, a: str):
        self.rules['endswith'][a] = True

    def all_after(self, a: str, B: list):
        self.rules['all_after'][a] = B

    def some_after(self, a: str, B: list):
        self.rules['some_after'][a] = B

    def all_before(self, a: str, B: list):
        self.rules['all_before'][a] = B

    def some_before(self, a: str, B: list):
        self.rules['some_before'][a] = B

    def all_nextto(self, a: str, B: list):
        self.rules['all_nextto'][a] = B

    def some_nextto(self, a: str, B: list):
        self.rules['some_nextto'][a] = B

    # Orientation Rules
    def all_forward_if(self, a: str):
        self.rules['all_forward_if'][a] = True

    def all_reverse_if(self, a: str):
        self.rules['all_reverse_if'][a] = True

    def some_forward(self, a: str):
        self.rules['some_forward'][a] = True

    def some_reverse(self, a: str):
        self.rules['some_reverse'][a] = True

    def all_forward(self):
        self.rules['all_forward'] = True

    def all_reverse(self):
        self.rules['all_reverse'] = True

    # Interaction Rules
    def represses(self, g: str, p: str):
        self.rules['represses'][g] = p

    def induces(self, i: str, p: str):
        self.rules['induces'][i] = p

    def drives(self, g: str, p: str):
        self.rules['drives'][g] = p

    # Constraint Methods
    def containsConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
        parts = self.containsParts
        count = 0
        for x in range(len(parts)):
            if parts[x] in variables:
                count += 1
        if count == len(parts):
            return True
        else:
            return False

    def morethanConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
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

    def exactlyConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
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

    def thenConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
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

    def withConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
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

    def startswithConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
        ruleList = list(self.rules["startswith"].keys())
        if len(ruleList) > 1:
            print("startswith used on multiple parts")
            return False
        if ruleList[0] in variables:
            if variables[0] == ruleList[0]:
                return True
            else:
                return False

    def endswithConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
        ruleList = list(self.rules["endswith"].keys())
        if len(ruleList) > 1:
            print("endswith used on multiple parts")
            return False
        if ruleList[0] in variables:
            if variables[len(variables)-1] == ruleList[0]:
                return True
            else:
                return False

    def all_afterConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
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

    def some_afterConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
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

    def all_beforeConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
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

    def some_beforeConstraint(self, first, second, third, fourth, fifth):
        variables = [first, second, third, fourth, fifth]
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

    # generate a certain number of sequences
    def generate(self, number=0):
        # make domain for each variable
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

        # Apply contains rules
        # contains, morethan, exactly, then, startswith, endswith,
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

        #Get solutions
        solutions = self.problem.getSolutions()
        if number == 0:
            return solutions
        else:
            return solutions[0:number]
