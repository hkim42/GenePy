class genepy:
    def __init__(self, N:int):
        if length < 1:
            raise Exception('invalid N: sequence length N must be larger than 0')
        else:
            self.length = N

        self.rules = {
            'morethan': {},
            'lessthan': {},
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

    def get_length(self):
        return self.length

    def set_length(self, arg:int):
        if arg < 1:
            raise Exception('invalid N: sequence length N must be larger than 0')
        else:
            self.length = arg

    def get_rules(self):
        return self.rules

    def get_sequences(self):
        return self.sequences

    def is_in_database(self, a:str, b=None):
        if b == None:
            pass
        elif type(b) == str:
            pass
        elif type(b) == list:
            pass
        else:
            pass
        return True

    def morethan(self, a:str, n:int):
        if n > self.get_length() or n < 0:
            raise Exception('invalid n: n must be between 0 and N')
        else:
            if is_in_database(self, a):
                self.rules['morethan'][a] = n
            else:
                raise Exception('invalid part: part(s) must be in the database')

    # just use morethan with 0 as n
    # def contains(self, a:str):
    #     self.rules['contains'][a] = True

    def lessthan(self, a:str, n:int):
        if n > self.get_length()+1 or n < 1:
            raise Exception('invalid n: n must be between 1 and N+1')
        else:
            if is_in_database(self, a):
                self.rules['lessthan'][a] = n
            else:
                raise Exception('invalid part: part(s) must be in the database')

    def exactly(self, a:str, n:int):
        if n > self.get_length() or n < 0:
            raise Exception('invalid n: n must be between 0 and N')
        else:
            if is_in_database(self, a):
                self.rules['exactly'][a] = n
            else:
                raise Exception('invalid part: part(s) must be in the database')

    def then(self, a:str, B:list):
        if is_in_database(self, a):
            self.rules['then'][a] = B
        else:
            raise Exception('invalid part: part(s) must be in the database')

    # just use morethan twice with 0 as n
    # def with(self, a:str, b:str):
    #     self.rules['with'][a] = b

    def startswith(self, a:str):
        if is_in_database(self, a):
            self.rules['startswith'][a] = True
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def endswith(self, a:str):
        if is_in_database(self, a):
            self.rules['endswith'][a] = True
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def all_after(self, a:str, B:list):
        if is_in_database(self, a, B):
            self.rules['all_after'][a] = B
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def some_after(self, a:str, B:list):
        if is_in_database(self, a, B):
            self.rules['some_after'][a] = B
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def all_before(self, a:str, B:list):
        if is_in_database(self, a, B):
            self.rules['all_before'][a] = B
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def some_before(self, a:str, B:list):
        if is_in_database(self, a, B):
            self.rules['some_before'][a] = B
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def all_nextto(self, a:str, B:list):
        if is_in_database(self, a, B):
            self.rules['all_nextto'][a] = B
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def some_nextto(self, a:str, B:list):
        if is_in_database(self, a, B):
            self.rules['some_nextto'][a] = B
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def all_forward_if(self, a:str):
        if is_in_database(self, a):
            self.rules['all_forward_if'][a] = True
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def all_reverse_if(self, a:str):
        if is_in_database(self, a):
            self.rules['all_reverse_if'][a] = True
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def some_forward(self, a:str):
        if is_in_database(self, a):
            self.rules['some_forward'][a] = True
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def some_reverse(self, a:str):
        if is_in_database(self, a):
            self.rules['some_reverse'][a] = True
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def all_forward(self):
        self.rules['all_forward'] = True

    def all_reverse(self):
        self.rules['all_reverse'] = True

    def represses(self, g:str, P:list):
        if is_in_database(self, g, P):
            self.rules['represses'][g] = P
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def induces(self, _in:str, P:list):
        if is_in_database(self, _in, P):
            self.rules['induces'][_in] = P
        else:
            raise Exception('invalid part: part(s) must be in the database')

    def drives(self, g:str, P:list):
        if is_in_database(self, g, P):
            self.rules['drives'][g] = P
        else:
            raise Exception('invalid part: part(s) must be in the database')

    # generate a certain number of sequences
    def generate(self, arg):
        pass

    # generate all possible sequences
    # may take a while
    def generate_all(self):
        pass
