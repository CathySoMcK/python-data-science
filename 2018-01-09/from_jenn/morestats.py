print('Hello World!')
"""
python -m doctest -v morestats.py

"""
def add(num1, num2):
    return num1 + num2

print(add(2,3))


#compute the volume of a rectangle
def vrectangle(length, width, height):
    return length * width * height

#compute the mean of a bunch of numbers
def mean(numbers):
    return sum(numbers) /len(numbers)

#compute the median of a bunch of numbers
def median(numbers):
    """
    Computes the median of a list of numbers
    argument: list of numbers
    return the median
    >>> median([2,1,6])
    2
    >>> median([3,5,4,9])
    4.5
    """
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        # even list
        return sum(numbers[middle - 1:middle + 1]) / 2
    else:
        # odd list
        return numbers[middle]

from collections import defaultdict
def mode(numbers):
    """
    finds the most frequent value of a list
    >>> mode([1,1,1,1,1,1,4,5,6])
    1
    >>> mode([1,2,2,2,3,3,4])
    2
    """
    d = defaultdict(int)
    for num in numbers:
        d[num] += 1
    return sorted(d, key=lambda k:d[k]) [-1]

#varience tells us about the spread of the data
#the square root of varience is the standard deviation
#1 standard deviation is also called 1 sigma
#compute varience

numbers = [1, 2, 3, 4, 5, 6, 7]
def variance (numbers, ddof):
    """
    determines the variance of a set of numbers
    >>> variance(numbers, 0)
    1.3720238095238095

    """
    return sum([(num - mean(numbers)) ** 2 for num in numbers]) / (len(numbers) - ddof)


def stdev (numbers, ddof):
    """
    finds the standard deviation for a population or a sample
    >>> stdev(numnbers, 0)
    1
    >>> stdev(numnbers, 1)
    2
    """
    return variance(numbers, ddof) ** 0.5
