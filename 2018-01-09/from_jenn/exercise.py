# problem 1
# ------------------------------------------------------------------- #
"""
python -m doctest -v exercise.py

"""

people = ['Bob Smith', 'Ken Jones', 'Alex Bradino']

def sort_by_last_name(people, order):
    """
    sorts list alphabetically
    >>> sort_by_last_name(people,False)
    ['Alex Bradino', 'Ken Jones', 'Bob Smith']
    >>> sort_by_last_name(people,True)
    ['Bob Smith', 'Ken Jones', 'Alex Bradino']
    """
    # return full names sorted by last name in ascending order
    # ['Alex Bradino', 'Ken Jones', 'Bob Smith']
    # add doctests make sure it passes
    return sorted(people, key=lambda person: person.split()[-1], reverse=order)


# problem 2
# ------------------------------------------------------------------- #
names = ['James', 'Susan', 'Maggie']
ages = [4, 9, 12]

def create_dictionary_from_lists(names, ages):
    """
    creates a new dictionary from lists names and ages
    >>> create_dictionary_from_lists(names, ages)
    {'James': 4, 'Maggie': 12, 'Susan': 9}
    """
    # {'James':4, 'Susan':9, 'Maggie':12}
    # add doctests make sure it passes
    mydict = {}
    for i in range(len(names)):
        mydict[names[i]] = ages[i]
    return mydict

# problem 3
# ------------------------------------------------------------------- #
numbers = [5, 6, 7, 8, 9, 10, 11, 12]


def square_even_values_and_sum_under_10(numbers):
    """
    the squares for only the even values in list numbers that are less than 10
    >>> square_even_values_and_sum_under_10(numbers)
    100
    """
    # 6^2 + 8^2]
    # add doctests make sure it passes
    return sum([n**2 for n in numbers if (n<10 and n%2==0)])
