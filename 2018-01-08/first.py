def add(num1, num2):
    return(num1 + num2)

# compute the volume of a cube
def vol_cube(l):
    # return(l*l*l)
    return(l**3)

def mean(numbers):
    # l = len(numbers)
    # s = 0
    # for el in numbers:
    #     s = s + el
    # return(s/l)
    return(sum(numbers)/len(numbers))

def median(numbers):
    """Computes the median of a list of numbers.

    argument: list of numbers
    return: the median

    >>> median([2,1,6])
    2
    >>> median([3,5,4,9])
    4.5
    """
    # l = len(numbers)
    # srt = sorted(numbers)
    # mid = l // 2 # also called flooring
    
    # 39127
    # sort --> 12379
    # middle --> 3
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        # even list
        return sum(numbers[middle - 1:middle + 1]) / 2
    else:
        # odd list
        return numbers[middle]

# 391274
# sort --> 123479
# avg of middle --> 3=4/2 --> 3.5

# mod to see if even
# use function sorted(x) to sort

def mode(numbers):
    """Find the most common value in the list

    argument: list of numbers
    returns: the mode

    >>> mode([1,2,2,2,3,3,4])
    2
    """

    # pass
    from collections import defaultdict
    d = defaultdict(int)
    # print(d)
    for n in numbers:
        d[n] += 1
    return(sorted(d, key=lambda key: d[key])[-1])


