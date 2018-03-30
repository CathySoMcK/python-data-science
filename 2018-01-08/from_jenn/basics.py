#1. lists  when order is important and you need to be able to change them

odds = [5,7,9]
sum(odds) # will total up this list
total = 0 #variable set up to hold a value
for num in odds: #another way to get the total
    total = total + num  #same as total=+num

total2 = 0
for i, num in enumerate(odds):
    total2 = total2 + (i * num)

#list comprehensions
squares = [n**2 for n in odds]
squareroots = [n**.5 for n in odds]
cuberoots = [n**.33 for n in odds]

sumofsquares = sum(n**2 for n in odds) #squares each value and then adds them together

#range starts at zero and goes up to but not including the last value
divisibleby5 = [n for n in range(31) if n%5==0] #all the numbers divisible by 5 between 0 and 30
divisibleby5cubes = [n**.33 for n in range(31) if n%5==0]

list(map(lambda n: n**(.33), odds))

#map function applies the same function to each element of a sequence.  Only works inside of a list
def squares(x):
    return x**2
maptest = list(map(squares, odds))

from functools import reduce
reduce(lambda total, n: total * n, odds,1)

#2 Tuple   when order is needed but immutable (does all the things lists do)
tup1 = (3,4)

#3 Sets  unordered
s1 = {3,4,5,6}
s2 = {5,6,7,8}
intersections = s1 | s2 #intersection
differneces = s1 ^ s2 #difference


#4dictionaries   no order, iterable (can loop thruough)  keys are unique and must be hashable(immutable)
d = {}  # creates a blank dictionary
for n in range(5):
    d[n] = n**2
d.get(5)  #get pulls out of the dictionary - doesn't put it in
d.get(5,0)

for k,v in d.items():
    print('key', k, 'value:', v)
{n:n**0.5 for n in range(100) if n%10==0}#dictionary comprehensiion


s = "a b c"
splitstring = s.split(' ')
l1 = [3,4,5]
l2 = [6,7,8]
total = 0
for i,n in enumerate(l1):
    total = total + n + l2[i]

list(zip(l1,l2))
