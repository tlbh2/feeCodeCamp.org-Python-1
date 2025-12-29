# List
myList = [1, 3, 5, 7, 9]
print(myList)

for i in myList:
    print(i)

print("--------------------")

# Tuple
myTuple = tuple([1, 2, 4, 6, 8, 9, 10])
print(myTuple) 

myTupleFromList = tuple(myList)
print(myTupleFromList)

for i in myTuple:
    print(i)

if 5 in myTuple:
    print("5 is in the tuple")
else:
    print("5 is not in the tuple")

print(myTuple.count(3))
print(myTuple.index(6)) 

a = myTuple[1:]
print(a)

b = myTuple[:3]
print(b)

c = myTuple[::2]
print(c)

reversed = myTuple[::-1]
print(reversed)

i1, *i2, i3 = myTuple
print(i1)
print(i2)
print(i3)

print("--------------------")
#compare list and tuple
import sys
myList2 = [1, 2, 4, 6, 8, 9, 10]
myTuple2 = (1, 2, 4, 6, 8, 9, 10)
print("List size:", sys.getsizeof(myList2), "bytes")
print("Tuple size:", sys.getsizeof(myTuple2), "bytes")

import timeit
list_time = timeit.timeit(stmt="[1, 2, 4, 6, 8, 9, 10]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 4, 6, 8, 9, 10)", number=1000000)
print("List creation time:", list_time)
print("Tuple creation time:", tuple_time)

print("--------------------")
# Dictionary
myDict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(myDict)
my2Dict = dict(name="Bob", age=25, city="Los Angeles")
print(my2Dict)

# make copy of dictionary instead of reference
my1Dict = dict(myDict)
my3Dict = myDict.copy()

del my1Dict["age"]
print(my1Dict)
my3Dict.pop("city")
print(my3Dict)
print("myDict :", myDict)

myDict.update(my2Dict)
print(myDict)

# can't use index to access dictionary items
for key in myDict:
    print(key, ":", myDict[key])

print('--------------------')
# Set
mySet = set("Hello") #good way to split string into nonduplicate characters
print(mySet)

mySet2 = {1, 2, 3, 4, 5, 5, 5}
print(mySet2)

mySet2.discard(3) #removes item if exists, no error if not unlike remove()
print(mySet2)

print(mySet2.pop()) #removes and returns an arbitrary item
print(mySet2)

#union and intersection
odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

u = odd.union(even)
print("Union:", u)

i = odd.intersection(prime)
print("Intersection:", i)

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

diff = setA.difference(setB) #items in setA not in setB
print("Difference (setA - setB):", diff)

sym_diff = setA.symmetric_difference(setB) #items in either setA or setB but not in both
print("Symmetric Difference:", sym_diff)

setA.update(setB) #adds items from setB to setA
print("Updated setA:", setA)

setA.intersection_update(prime) #keeps only items also in prime
print("setA after intersection_update with prime:", setA)

setA.difference_update({6, 7, 8}) #removes items found in the given set
print("setA after difference_update with {6, 7, 8}:", setA)

setA.symmetric_difference_update({2, 3}) #keeps items in either setA or the given set but not in both
print("setA after symmetric_difference_update with {2, 3}:", setA)  

setA= {1, 2, 3, 4 , 5 ,6}
setB= {1, 2, 3}

print("setB is subset of setA:", setB.issubset(setA))
print("setA is superset of setB:", setA.issuperset(setB))
print("setA and setB are disjoint:", setA.isdisjoint(setB))

# make copy of dictionary instead of reference
setB = set(setA) 
setB = setA.copy()
print(setB)

print("--------------------")
# Frozen Set
myFrozenSet = frozenset([1, 2, 3, 4 , 5])
print(myFrozenSet)      
for i in myFrozenSet:
    print(i)        
if 3 in myFrozenSet:
    print("3 is in the frozen set")
else:
    print("3 is not in the frozen set")
print(myFrozenSet.union({6, 7, 8}))
print(myFrozenSet.intersection({4, 5, 6, 7}))   
print(myFrozenSet.difference({2, 3, 4}))
print(myFrozenSet.symmetric_difference({5, 6, 7}))

print("--------------------")
# String
myString = "Hello, World!"
print(myString)

for char in myString:
    print(char)

myString1 = "how are you doing ?"
listString = myString1.split()
print("List of words:", listString)

print("Length of string:", len(myString))
print("Substring (0-5):", myString[0:5])
print("Uppercase:", myString.upper())
print("Lowercase:", myString.lower())
print("Replace 'World' with 'Python':", myString.replace("World", "Python"))
print("Find 'o':", myString.find("o"))
print("Split by comma:", myString.split(","))
print("Is alphabetic:", myString.isalpha())
print("Is numeric:", myString.isdigit())
print("Strip whitespace:", "   Hello   ".strip())
print("Count 'l':", myString.count("l"))
print("Starts with 'Hello':", myString.startswith("Hello"))
print("Ends with '!':", myString.endswith("!"))
print("Format string:", "Name: {}, Age: {}".format("Alice", 30))
print("F-string:", f"Name: {'Bob'}, Age: {25}")
print("Reversed string:", myString[::-1])
print("Substring with step 2:", myString[::2])
print("Index of 'W':", myString.index("W"))
print("Join list into string:", "-".join(["2024", "06", "15"]))

print("----------Collections----------")
# Collections Module
from collections import Counter, namedtuple, deque, OrderedDict, defaultdict

# Counter
string = "aaaaaabbbbbbbccccdde"
counter = Counter(string)
print(counter)

print(counter.most_common(2))     # Returns list of tuples (element, count) of the two most common elements
print(counter.most_common(2)[0])  # Returns the first tuple (element, count) of the two most common elements
print(counter.most_common(2)[0][1]) #returns count/value of the first tuple

print(list(counter.elements())) # Returns a list of elements repeated as per their counts

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p)
print(p.x, p.y)

# ordereddict : not important after python 3.7+
# defaultdict
dd = defaultdict(int)
dd['a'] += 1
dd['b'] += 2
print(dd['c'])  # Outputs 0 since 'c' is not present and default factory is int

try:
    dd_none = dict()  # reg dict with no default factory provided
    print(dd_none['x'])  # This will raise a KeyError since 'x' is not present in the dictionary
except KeyError as e:
    print(f"KeyError: {e}")

# deque
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)    
print(dq)

dq.pop()
dq.popleft()
print(dq)

dq.extend([5, 6, 7])
dq.extendleft([-2, -1])  # Note: extends to the left in reverse
print(dq)

dq.rotate(2)  # Rotate right by 2
print(dq)

dq.rotate(-3)  # Rotate left by 3
print(dq)

print("------------Itertools--------")
# Itertools Module: product, permutations, combinations, accumulate, groupby, infinite iterators
from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat

# Product : gives out all possible combinations by taking one element from each iterable
a = [1, 2]
b = ['A', 'B']
prod = product(a, b)
print(prod) # Prints the product object
print(list(prod)) # Converts to list 

# Permutations
c = [1, 2, 3]
perm = permutations(c)
print(list(perm))

perm = permutations(c,2) #length 2
print(list(perm)) #different orderings with length 2

# Combinations
d = [1, 2, 3, 4]
comb = combinations(d, 2) #length 2
print(list(comb))

comb = combinations(d, 3) #length 3
print(list(comb))

from itertools import combinations_with_replacement
comb_wr = combinations_with_replacement(d, 2)
print(list(comb_wr))

# Accumulate
e = [1, 2, 3, 4]
acc = accumulate(e) # by default does sum
print(list(acc))

import operator
acc_mul = accumulate(e, func=operator.mul) # multiplication
print(list(acc_mul))

acc_max = accumulate(e, func=max) # maximum value
print(list(acc_max))

# Groupby
persons = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 30},
    {'name': 'David', 'age': 25}
]

# Note: groupby requires the input to be sorted by the key for correct grouping
persons = sorted(persons, key=lambda x: x['age'])

grouped_persons = groupby(persons, key=lambda x: x['age'])
for key, value in grouped_persons:
    print(key, list(value))

# Infinite Iterators
from itertools import count, cycle, repeat

#count
for i in count(12): # start val of 12, infinite loop until break condition
    print(i)
    if i == 15:
        break

#cycle
f = [1,2,3]
for i in cycle(f): 
    print(i)
    if i == 3:
        break

# repeat
for i in repeat('Hello', 3): # repeats 'Hello' 3 times
    print(i)