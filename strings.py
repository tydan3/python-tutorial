# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
# x = str("s1")  # x will be 's1'
# y = str(2)    # y will be '2'
# z = str(3.0)  # z will be '3.0'


# ------------------------------------------------
# Multiline Strings
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# ------------------------------------------------
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# a = "Hello, World!"
# print(a[1])


# ------------------------------------------------
# Loop through the letters in the word "banana":
# for x in "banana":
#     print(x)


# ------------------------------------------------
# To get the length of a string, use the len() function.
# a = "Hello, World!"
# print(len(a))


# ------------------------------------------------
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# txt = "The best things in life are free!"
# print("free" in txt)


# ------------------------------------------------
# Use it in an if statement:
# txt = "The best things in life are free!"
# if "free" in txt:
#     print("Yes, 'free' is present.")


# ------------------------------------------------
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# txt = "The best things in life are free!"
# print("expensive" not in txt)


# ------------------------------------------------
# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
