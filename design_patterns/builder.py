# from unittest import TestCase
#
#
# class Field:
#     def __init__(self, type, name):
#         self.type = type
#         self.name = name
#
#     def __str__(self):
#         return "{}self.{} = {}".format(" " * 4, self.type, self.name)
#
#
# class Class:
#     def __init__(self, name):
#         self.name = name
#         self.fields = []
#
#     def __str(self):
#         lines = []
#         if self.name:
#             lines.append("class {}:".format(self.name))
#         if self.fields:
#             lines.append("{}def __init__(self):".format(" " * 2))
#             for element in self.fields:
#                 lines.append(str(element))
#         else:
#             lines.append("{}pass".format(" " * 2))
#         return '\n'.join(lines)
#
#     def __str__(self):
#         return self.__str()
#
#
# class CodeBuilder:
#
#     def __init__(self, root_name):
#         self.root_name = root_name
#         self.__class = Class(root_name)
#
#     def add_field(self, type, name):
#         self.__class.fields.append(Field(type, name))
#         return self
#
#     def __str__(self):
#         return str(self.__class)
#
#     def clear(self):
#         self.__class = Class(self.root_name)
#
#
# print('Filled class:\n')
# cb = CodeBuilder('Person').add_field('name', '""').add_field('age', 0)
# print(cb)
# print('\nEmpty class:\n')
# cb.clear()
# print(cb)
#
#
# class Evaluate(TestCase):
#     @staticmethod
#     def preprocess(s=''):
#         return s.strip().replace('\r\n', '\n')
#
#     def test_empty(self):
#         cb = CodeBuilder('Foo')
#         self.assertEqual(
#             self.preprocess(str(cb)),
#             'class Foo:\n  pass'
#         )
#
#     def test_person(self):
#         cb = CodeBuilder('Person').add_field('name', '""') \
#             .add_field('age', 0)
#         self.assertEqual(self.preprocess(str(cb)),
#                          """class Person:
#   def __init__(self):
#     self.name = \"\"
#     self.age = 0""")
