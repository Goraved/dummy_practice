from abc import ABC
from collections import Iterable
from unittest import TestCase


class Values(ABC, Iterable):
    @property
    def sum(self):
        total = 0
        for a in self:
            for b in a:
                total += b
        return total


class SingleValue(Values):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, Values):
    pass


class Evaluate(TestCase):
    def test_exercise(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        a = all_values.sum
        self.assertEqual(all_values.sum, 66)
