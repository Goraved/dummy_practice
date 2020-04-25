import math
import string

"""
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/08-Functions%20and%20Methods%20Homework.ipynb
"""


def vol(rad):
    """
    Write a function that computes the volume of a sphere given its radius.
    """
    print(4 / 3 * math.pi * rad ** 3)


def ran_check(num, low, high):
    """
    Write a function that checks whether a number is in a given range (inclusive of high and low)
    """
    if low <= num <= high:
        return f'{num} is in range between {low} and {high}'
    else:
        return f'{num} is out of range'


def up_low(string):
    """
    Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters
    """
    low, up = 0, 0
    for letter in string:
        if not letter.isalpha():
            continue
        elif letter == letter.lower():
            low += 1
        elif letter == letter.upper():
            up += 1
    return f"""
    No. of Upper case characters :  {up}
    No. of Lower case Characters :  {low}
    """


def unique_list(lst):
    """
    Write a Python function that takes a list and returns a new list with unique elements of the first list.
    """
    return list(set(lst))


def multiply(numbers):
    """
    Write a Python function to multiply all the numbers in a list.
    """
    multiplied = 1
    for number in numbers:
        multiplied *= number
    return multiplied


def palindrome(s):
    """
    Write a Python function that checks whether a passed in string is palindrome or not.
    """
    return s.lower() == s[::-1].lower()


def ispangram(str, alphabet=string.ascii_lowercase):
    """
    Write a Python function to check whether a string is pangram or not.
    """
    for char in alphabet:
        if char not in str:
            return f'False - letter "{char}" is missed'
    return True
