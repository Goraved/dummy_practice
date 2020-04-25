import unittest


class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        self.combination = '12345'

    def reset(self):
        self.status = 'LOCKED'

    def enter_digit(self, digit):
        if self.status == 'LOCKED':
            self.status = str(digit)
        elif len(self.status) < len(self.combination):
            self.status += str(digit)
        self.check_for_correctness()

    def check_for_correctness(self):
        if not self.combination.startswith(self.status):
            self.status = 'ERROR'
        if self.status == self.combination:
            self.status = 'OPEN'


class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)

    def test_failure(self):
        cl = CombinationLock([1, 2, 3])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(5)
        self.assertEqual('ERROR', cl.status)
