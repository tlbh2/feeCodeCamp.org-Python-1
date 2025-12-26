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