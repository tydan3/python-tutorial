# Often, when dealing with iterators, we also get need to keep a count of iterations.
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
# This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.

# Syntax:
#   enumerate(iterable, start=0)
# Parameters:
#   Iterable: any object that supports iteration
#   Start: the index value from which the counter is to be started, by default it is 0


# ------------------------------------------------
# # Python program to illustrate enumerate function
# l1 = ["eat", "sleep", "repeat"]
# s1 = "geek"

# # creating enumerate objects
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)

# print("Return type:", type(obj1))
# print(list(enumerate(l1)))

# # changing start index to 2 from 0
# print(list(enumerate(s1, 2)))


# ------------------------------------------------
# Using Enumerate object in loops:
# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)

# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print(count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)
