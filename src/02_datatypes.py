"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

assert x + int(7) == 12, "Should be 12"


# Write a print statement that combines x + y into the string value 57

assert str(x) + y == "57", "Should be 57"
