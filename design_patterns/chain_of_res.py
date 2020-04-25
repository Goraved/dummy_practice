import unittest
from abc import ABC
from enum import Enum


class Creature(ABC):
    def __init__(self, game, attack, defense):
        self.game = game
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def defense(self):
        pass

    @property
    def attack(self):
        pass

    def query(self, source, query):
        pass


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def defense(self):
        q = Query(self.initial_defense, WhatToQuery.DEFENSE)
        for g in self.game.creatures:
            g.query(self, q)
        return q.value

    @property
    def attack(self):
        q = Query(self.initial_attack, WhatToQuery.ATTACK)
        for g in self.game.creatures:
            g.query(self, q)
        return q.value

    def query(self, source, query):
        if self != source and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 1


class GoblinKing(Goblin):
    def __init__(self, game, attack=3, defense=3):
        super().__init__(game, attack, defense)

    def query(self, source, query):
        if self != source and query.what_to_query == WhatToQuery.ATTACK:
            query.value += 1
        else:
            super().query(source, query)


class Query:
    def __init__(self, initial_value, what_to_query):
        self.value = initial_value
        self.what_to_query = what_to_query


class Game:
    def __init__(self):
        self.creatures = []


class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)

        goblin2 = Goblin(game)
        game.creatures.append(goblin2)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(2, goblin.defense)

        goblin3 = GoblinKing(game)
        game.creatures.append(goblin3)

        self.assertEqual(2, goblin.attack)
        self.assertEqual(3, goblin.defense)