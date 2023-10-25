# List mutable
mylist = ["Ian", "erick", "Joan", "Brian"]
print(mylist)
print(f" My name is {mylist[0]} ")

mylist.sort()
print(mylist)
mylist[1] = "Waweru"
print(mylist)

# Tuples are immutable but are ordered and does not allow object assignment
mytuple = ("kenya", "Uganda", "Tanzania", "Rwanda")
print(mytuple[0])

# mytuple[0] = "Somalia" - runs with an error

# Sets are unordered
fruits = {'mangoes','oranges','pineapples', 'bananas'}
print(fruits)

# Dictionaries
employees = {name}

