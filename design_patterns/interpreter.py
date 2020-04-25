import unittest
from enum import Enum, auto


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        l = self.lex(expression)
        digits = [int(_.text) for _ in l if _.type == Token.Type.INTEGER]
        operators = [_ for _ in l if _.type != Token.Type.INTEGER]
        result = 0
        if len(l) == 1 and l[0].type == Token.Type.INTEGER:
            return int(expression)
        if len(digits) - 1 != len(operators):
            return result
        else:
            for ind, o in enumerate(operators):
                if o.type.value == Token.Type.PLUS.value:
                    result = digits[ind] + digits[ind + 1]
                elif o.type.value == Token.Type.MINUS.value:
                    result = digits[ind] - digits[ind + 1]
        return result

    def lex(self, input):
        result = []
        i = 0
        while i < len(input):
            if input[i] == '+':
                result.append(Token(Token.Type.PLUS, '+'))
            elif input[i] == '-':
                result.append(Token(Token.Type.MINUS, '-'))
            else:
                try:
                    result.append(Token(Token.Type.INTEGER, int(input[i])))
                except ValueError:
                    if self.variables.get(input[i]):
                        result.append(Token(Token.Type.INTEGER, int(self.variables[input[i]])))
                    else:
                        result.append(Token(Token.Type.ERROR, 'EMPTY VARIABLE'))

            i += 1
        return result


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        ERROR = auto()

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return self.text


class FirstTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ep = ExpressionProcessor()
        ep.variables['x'] = 5
        cls.ep = ep

    def test_simple(self):
        self.assertEqual(1, self.ep.calculate('1'))

    def test_addition(self):
        self.assertEqual(3, self.ep.calculate('1+2'))

    def test_addition_with_variable(self):
        self.assertEqual(6, self.ep.calculate('1+x'))

    def test_failure(self):
        self.assertEqual(0, self.ep.calculate('1+xy'))
