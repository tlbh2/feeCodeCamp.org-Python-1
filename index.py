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