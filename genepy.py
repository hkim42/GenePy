class genepy:
    def __init__(self, length: int, check_conflicts=False: bool):
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
            'with': {},
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

    def morethan(self, a: str, n: int):
        if n > N or n < 1:
            raise Exception('invalid n')
        else:
            self.rules['morethan'][a] = n

    def contains(self, a: str):
        self.rules['contains'][a] = True

    def exactly(self, a: str, n: int):
        pass

    def then(self):
        pass

    def with(self):
        pass

    def startswith(self):
        pass

    def endswith(self):
        pass

    def all_after(self):
        pass

    def some_after(self):
        pass

    def all_before(self):
        pass

    def some_before(self):
        pass

    def all_nextto(self):
        pass

    def some_nextto(self):
        pass

    def all_forward_if(self):
        pass

    def all_reverse_if(self):
        pass

    def some_forward(self):
        pass

    def some_reverse(self):
        pass

    def all_forward(self):
        pass

    def all_reverse(self):
        pass

    def represses(self):
        pass

    def induces(self):
        pass

    def drives(self):
        pass

    def show_all(self):
        pass

    def delete_rule(self):
        pass

    def delete_all(self):
        pass

    def generate(self):
        pass

    def generate_all(self):
        pass
