class PolishNotation():
    _result = []
    _stack = []

    _PRIORITY = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        ')': 0,
        '(': 0,
        None: -1,
    }

    def __init__(self, input):
        self.user_input = input
        self.expression_for_loop = self.user_input.replace('(', '( ').replace(')', ' )').split(' ')
        self.main_loop()

    def get_priority(self, el):
        return self._PRIORITY[el]

    @property
    def result(self):
        return self._result

    @property
    def stack(self):
        return self._stack

    def add_in_result(self, el):
        self.result.append(el)

    def get_el_from_stack(self):
        try:
            return self.stack.pop()
        except IndexError:
            pass

    def add_in_stack(self, el):
        self.stack.append(el)

    def check_element(self, el):
        if el not in self._PRIORITY:
            self.add_in_result(el)

        elif el == ')':
            self.brackets_loop()

        else:
            self.priority_loop(el)

    def brackets_loop(self):
        last = self.get_el_from_stack()
        while last != '(':
            self.add_in_result(last)
            last = self.get_el_from_stack()

        self.get_el_from_stack()

    def priority_loop(self, el):
        last = None if not self.stack else self.stack[-1]
        while self.get_priority(last) >= self.get_priority(el):
            last = None if not self.stack else self.get_el_from_stack()
            if not last is None: self.add_in_result(last)
        self.add_in_stack(el)


    def main_loop(self):
        for item in self.expression_for_loop:
            self.check_element(item)

    def calculate_result(self):
        return eval(self.user_input)

    def get_result(self):
        last_el_in_stack = self.get_el_from_stack()
        calculate =  self.calculate_result()
        self.add_in_result(last_el_in_stack)
        self.add_in_result(calculate)
        result = ' '.join([str(el) for el in self.result])
        print(result)
        return result



if __name__ == "__main__":
    example = PolishNotation('(1 + 2) * 4 + 3')
    example.get_result()

