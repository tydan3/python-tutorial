# print("hello world")
# if 5 > 2:
#     print("five is greater than two")
# x = 5  # x is of type int
# y = "hello world!"
# print(x)
# print(y)
# # This is a comment
# x = "sally"  # x is now sally
# print(x)


# ------------------------------------------------
# # Many Values to Multiple Variables
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


# ------------------------------------------------
# # One Value to Multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


# ------------------------------------------------
# # Unpack a Collection
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)


# ------------------------------------------------
# You can use the + operator to output multiple variables:
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)


# ------------------------------------------------
# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
# x = 5
# y = "John"
# print(x, y)


# ------------------------------------------------
# # If you create a variable with the same name inside a function, this variable will be local,
# # and can only be used inside the function. The global variable with the same name will remain
# # as it was, global and with the original value.
# x = "awesome"


# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)


# myfunc()

# print("Python is " + x)


# ------------------------------------------------
# # If you use the global keyword, the variable belongs to the global scope:
# def myfunc():
#     global x
#     x = "fantastic"


# myfunc()

# print("Python is " + x)
