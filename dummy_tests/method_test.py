# WARMUP SECTION:
def lesser_of_two_evens(a, b):
    """
    LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but
    returns the greater if one or both numbers are odd
    """
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


def animal_crackers(text):
    """
    ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    """
    text = text.split()
    return text[0][0] == text[1][0]


def makes_twenty(n1, n2):
    """
    MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
    If not, return False
    """
    return sum([n1, n2]) == 20 or 20 in [n1, n2]


# LEVEL 1 PROBLEMS
def old_macdonald(name):
    """
    OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
    """
    return name[:3].capitalize() + name[3:].capitalize()


def master_yoda(text):
    """
    MASTER YODA: Given a sentence, return a sentence with the words reversed
    """
    return " ".join(sorted(text.split(), reverse=True))


def almost_there(n):
    """
    ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
    """
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


# LEVEL 2 PROBLEMS
def has_33(nums):
    """
    FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    """
    for i in range(0, len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            return True
    return False


def paper_doll(text):
    """
    PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    """
    return "".join([t * 3 for t in text])


def blackjack(a, b, c):
    """
    BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
    If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum
    (even after adjustment) exceeds 21, return 'BUST'
    """
    sum_nums = sum([a, b, c])
    if sum_nums <= 21:
        return sum_nums
    elif sum_nums - 10 <= 21 and 11 in [a, b, c]:
        return sum_nums - 10
    return 'BUST'


def summer_69(arr):
    """
    SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
    and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
    """
    sum = 0
    six = False
    for num in arr:
        if num == 6:
            six = True
        elif num == 9:
            six = False
            continue
        if six is False:
            sum += num
    return sum
