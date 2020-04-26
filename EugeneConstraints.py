class EugeneConstraints:

    def __init__(self):
        pass

    def containsConstraint(self, parts, variables):
        temp = variables
        for p in parts:
            for x in variables:
                if variables[x] == parts[p]:
                    temp[x] = True
                else:
                    temp[x] = False
        return any(temp)

    def morethanConstraint(self, part, n, variables):
        for x in variables:
            if variables[x] == part:
                variables[x] = True
            else:
                variables[x] = False
        occurrences = sum(variables)
        if occurrences > n:
            return True
        else:
            return False

    def exactlyConstraint(self, part, n, variables):
        for x in variables:
            if variables[x] == part:
                variables[x] = True
            else:
                variables[x] = False
        occurrences = sum(variables)
        if occurrences == n:
            return True
        else:
            return False

    def thenConstraint(self, A, B, variables):
        existA = False
        existB = False
        for x in variables:
            if variables[x] == A:
                existA = True
            if variables[x] == B:
                existB = True
        if existA and existB:
            return True
        elif existB:
            return True
        else:
            return False

    def withConstraint(self, A, B, variables):
        existA = False
        existB = False
        for x in variables:
            if variables[x] == A:
                existA = True
            if variables[x] == B:
                existB = True
        if existA and existB:
            return True
        else:
            return False

    def startswithConstraint(self, part, variables):
        existA = False
        for x in variables:
            if variables[x] == part:
                existA = True
            else:
                return False
        if variables[0] == part:
            return True
        else:
            return False

    def endswithConstraint(self, part, variables):
        existA = False
        for x in variables:
            if variables[x] == part:
                existA = True
            else:
                return False
        lastIndex = variables.length - 1
        if variables[lastIndex] == part:
            return True
        else:
            return False

    def all_afterConstraint(self, A, B, variables):
        firstA = None
        lastB = None
        for x in variables:
            if variables[x] == B:
                lastB = variables[x]
        for x in variables:
            if variables[x] == A:
                firstA = variables[x]
                break
        if lastB < firstA:
            return True
        else:
            return False

    def some_afterConstraint(self, A, B, variables):
        foundA = []
        foundB = []
        for x in variables:
            if variables[x] == A:
                foundA.append(x)
            if variables[x] == B:
                foundB.append(x)
        for i in foundA:
            for j in foundB:
                if foundB[j] < foundA[i]:
                    break
                    return True
        return False

    def all_beforeConstraint(self, A, B, variables):
        firstB = None
        lastA = None
        for x in variables:
            if variables[x] == A:
                lastA = variables[x]
        for x in variables:
            if variables[x] == B:
                firstB = variables[x]
                break
        if lastA < firstB:
            return True
        else:
            return False

    def some_beforeConstraint(self, A, B, variables):
        foundA = []
        foundB = []
        for x in variables:
            if variables[x] == A:
                foundA.append(x)
            if variables[x] == B:
                foundB.append(x)
        for i in foundA:
            for j in foundB:
                if foundA[j] < foundB[i]:
                    break
                    return True
        return False
