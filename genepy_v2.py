class genepy:
    def __init__(self, length:int):
        if length < 1:
            raise Exception('invalid length')
        else:
            self.length = length
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

    def get_length(self):
        return self.length

    def set_length(self, arg:int):
        if arg < 1:
            raise Exception('error: invalid length')
        else:
            self.length = arg

    def is_in_database(self, a:str, b:str=None):
        return True

    def morethan(self, a:str, n:int):
        if is_in_database(self, a):
            if n > N or n < 1:
                print('warning: invalid n')
            else:
                self.rules['morethan'][a] = n
                self.rules['contains'].pop(a, None)
        else:
            print('warning: part(s) not in database')

    def contains(self, a:str):
        if is_in_database(self, a):
            try:
                temp = self.rules['morethan'][a]
                print('warning: morethan already exists for this part')
            except KeyError:
                # self.rules['contains'][a] = True
                self.morethan(self, a, 0)
        else:
            print('warning: part(s) not in database')

    def exactly(self, a:str, n:int):
        if is_in_database(self, a):
            if n > N or n < 1:
                print('warning: invalid n')
            else:
                self.rules['morethan'].pop(a, None)
                self.rules['contains'].pop(a, None)
                self.rules['exactly'][a] = n
        else:
            print('warning: part(s) not in database')

    def then(self, a:str, b:str):
        if is_in_database(self, a, b):
            self.rules['then'][a] = b
        else:
            print('warning: part(s) not in database')

    def with(self, a:str, b:str):
        self.contains(self, a)
        self.contains(self, b)

    def startswith(self, a:str):
        if is_in_database(self, a):
            self.rules['startswith'][a] = True
        else:
            print('warning: part(s) not in database')

    def endswith(self, a:str):
        if is_in_database(self, a):
            self.rules['endswith'][a] = True
        else:
            print('warning: part(s) not in database')

    def all_after(self, a:str, b:str):
        if is_in_database(self, a, b):
            self.rules['all_after'][a] = b
        else:
            print('warning: part(s) not in database')

    def some_after(self, a:str, b:str):
        if is_in_database(self, a, b):
            self.rules['some_after'][a] = b
        else:
            print('warning: part(s) not in database')

    def all_before(self, a:str, b:str):
        if is_in_database(self, a, b):
            self.rules['all_before'][a] = b
        else:
            print('warning: part(s) not in database')

    def some_before(self, a:str, b:str):
        if is_in_database(self, a, b):
            self.rules['some_before'][a] = b
        else:
            print('warning: part(s) not in database')

    def all_nextto(self, a:str, b:str):
        if is_in_database(self, a, b):
            self.rules['all_nextto'][a] = b
        else:
            print('warning: part(s) not in database')

    def some_nextto(self, a:str, b:str):
        if is_in_database(self, a, b):
            self.rules['some_nextto'][a] = b
        else:
            print('warning: part(s) not in database')

    def all_forward_if(self, a:str):
        if is_in_database(self, a):
            self.rules['all_forward_if'][a] = True
        else:
            print('warning: part(s) not in database')

    def all_reverse_if(self, a:str):
        if is_in_database(self, a):
            self.rules['all_reverse_if'][a] = True
        else:
            print('warning: part(s) not in database')

    def some_forward(self, a:str):
        if is_in_database(self, a):
            self.rules['some_forward'][a] = True
        else:
            print('warning: part(s) not in database')

    def some_reverse(self, a:str):
        if is_in_database(self, a):
            self.rules['some_reverse'][a] = True
        else:
            print('warning: part(s) not in database')

    def all_forward(self):
        if self.rules['all_reverse'] == True:
            self.rules['all_reverse'] = False
            print('warning: all_reverse is changed to False from True')
        self.rules['all_forward'] = True

    def all_reverse(self):
        if self.rules['all_forward'] == True:
            self.rules['all_forward'] = False
            print('warning: all_forward is changed to False from True')
        self.rules['all_reverse'] = True

    def represses(self, a:str, b:str):
        if is_in_database(self, a, b):
            self.rules['represses'][a] = b
        else:
            print('warning: part(s) not in database')

    def induces(self, a:str, b:str):
        if is_in_database(self, a, b):
            self.rules['induces'][a] = b
        else:
            print('warning: part(s) not in database')

    def drives(self, a:str, b:str):
        if is_in_database(self, a, b):
            self.rules['drives'][a] = b
        else:
            print('warning: part(s) not in database')

    def part_exists(self, a:str):
        try:
            temp = self.rules['morethan'][a]
            return True
        except KeyError:
            try:
                temp = self.rules['exactly'][a]
                if temp > 0:
                    return True
                else:
                    return False
            except KeyError:
                return False

    def rule_cleanup(self):
        for key in self.rules['then']:
            if part_exists(key):
                self.contains(self, self.rules['then'][key])
            else:
                self.rules['then'].pop(key)

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

def main():
    gp1 = genepy(4)
    pass

if __name__ == '__main__':
    main()
