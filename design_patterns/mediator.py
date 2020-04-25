import unittest


class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.participants.append(self)

    def say(self, value):
        print(f'Player - "{self}" broadcast {value}')
        self.mediator.increase_score(self, value)


class Mediator:
    participants = []

    def increase_score(self, sender, value):
        for p in self.participants:
            if p != sender:
                p.value += value
                print(f'Player - "{p}" got + {value} and now has score {p.value}')


class TestSuite(unittest.TestCase):
    def test(self):
        m = Mediator()
        p1 = Participant(m)
        p2 = Participant(m)

        self.assertEqual(0, p1.value)
        self.assertEqual(0, p2.value)

        p1.say(2)

        self.assertEqual(0, p1.value)
        self.assertEqual(2, p2.value)

        p2.say(4)

        self.assertEqual(4, p1.value)
        self.assertEqual(2, p2.value)
