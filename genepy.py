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
        if n > N:
            raise Exception('invalid n: n must be less than or equal to N')
        else:
            self.rules['exactly'][a] = n

    def then(self, a: str, B: str):
        self.rules['then'][a] = B

    #def with(self, a: str, B: str):
    #    self.rules['with'][a] = B

    def startswith(self, a: str):
        self.rules['startswith'][a] = True

    def endswith(self, a: str):
        self.rules['endswith'][a] = True

    def all_after(self, a: str, B: list):
        self.rules['all_after'][a] = B

    def some_after(self, a: str, B: list):
        self.rules['some_after'][a] = B

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

    # generate a certain number of sequences
    def generate(self):
        pass

    # generate all possible sequences
    # may take a while
    def generate_all(self):
        pass

    # add rules post-processing
    # these rules are stored separately and applied to already generated sequences (when regenerate is called)
    def add_rules(self):
        pass

    # regenerate sequences post-processing
    # add_rules should come before this to make a difference
    # uses rules added by add_rules to filter the existing sequences
    def regenerate(self):
        pass
