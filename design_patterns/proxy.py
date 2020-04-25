from unittest import TestCase


class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person
        self.age = person.age
        self._person = Person(person)

    def drive(self):
        if self.age >= 16:
            return self._person.drive()
        else:
            return 'too young'

    def drink(self):
        if self.age >= 18:
            return self._person.drink()
        else:
            return 'too young'

    def drink_and_drive(self):
        return 'dead'


# p = Person(10)
# p1 = Person(16)
# p2 = Person(17)
# p3 = Person(18)
# p4 = Person(20)
# pp = [p, p1, p2, p3, p4]
# for _ in pp:
#     rp = ResponsiblePerson(_)
#     rp.drive()
#     rp.drink()
#     rp.drink_and_drive()
#     print('__')

class Evaluate(TestCase):
    def test_exercise(self):
        p = Person(10)
        rp = ResponsiblePerson(p)

        self.assertEqual('too young', rp.drive())
        self.assertEqual('too young', rp.drink())
        self.assertEqual('dead', rp.drink_and_drive())

        rp.age = 20

        self.assertEqual('driving', rp.drive())
        self.assertEqual('drinking', rp.drink())
        self.assertEqual('dead', rp.drink_and_drive())
