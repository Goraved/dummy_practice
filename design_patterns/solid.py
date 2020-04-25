from enum import Enum


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Color(Enum):
    GREEN = 1
    RED = 2
    BLUE = 3


class Product:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return CombineSpec(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class CombineSpec(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Size.SMALL, Color.RED)
car = Product('Car', Size.MEDIUM, Color.RED)
house = Product('House', Size.LARGE, Color.BLUE)
items = [apple, car, house]

bf = BetterFilter()
print('Filtered items:')
print('> Red items:')
red = ColorSpecification(Color.RED)
red_items = bf.filter(items, red)
for item in red_items:
    print(f'{item.name} - is {item.color.name}')
print('> Big items:')
large = SizeSpecification(Size.LARGE)
big_items = bf.filter(items, SizeSpecification(Size.LARGE))
for item in big_items:
    print(f'{item.name} - is {item.size.name}')
print('> Medium red items:')
medium_red = red and SizeSpecification(Size.MEDIUM)
medium_red_items = bf.filter(items, medium_red)
for item in medium_red_items:
    print(f'{item.name} - is {item.size.name} and {item.color.name}')
