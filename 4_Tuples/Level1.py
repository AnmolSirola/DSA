# 1 Create a tuple

numbers = (10, 20, 30)

print(numbers)

# A tuple is an ordered and immutable collection of elements.

# Output - (10, 20, 30)

# Tuples store multiple values in a single variable and cannot be modified after creation.



# 2 Access element using index

numbers = (10, 20, 30)

print(numbers[1])

# Tuples use zero-based indexing like lists.

# Output - 20

# Index 1 refers to the second element.



# 3 Access the first element

numbers = (5, 10, 15)

print(numbers[0])

# Index 0 represents the first element.

# Output - 5

# The first element can be accessed using index 0.



# 4 Access the last element

numbers = (5, 10, 15)

print(numbers[-1])

# Negative indexing accesses elements from the end.

# Output - 15

# -1 refers to the last element of the tuple.



# 5 Find the length of a tuple

numbers = (10, 20, 30, 40)

print(len(numbers))

# len() returns the number of elements in the tuple.

# Output - 4

# len() counts the elements stored in the tuple.



# 6 Iterate through a tuple

numbers = (10, 20, 30)

for num in numbers:
    print(num)

# A for loop can iterate through each element.

# Output - 10 20 30

# I iterate through the tuple using a loop.



# 7 Check if an element exists

numbers = (1, 2, 3, 4)

print(3 in numbers)

# 'in' checks membership.

# Output - True

# The 'in' operator verifies if the element exists in the tuple.



# 8 Count occurrences of an element

numbers = (1, 2, 2, 3)

print(numbers.count(2))

# count() returns number of occurrences.

# Output - 2

# count() counts how many times the element appears.



# 9 Find index of an element

numbers = (10, 20, 30)

print(numbers.index(20))

# index() returns position of the element.

# Output - 1

# index() searches the tuple and returns the index.



# 10 Concatenate two tuples

t1 = (1, 2)
t2 = (3, 4)

result = t1 + t2

print(result)

# '+' combines two tuples.

# Output - (1, 2, 3, 4)

# Tuple concatenation merges both tuples.



# 11 Repeat a tuple

numbers = (1, 2, 3)

print(numbers * 2)

# '*' repeats tuple elements.

# Output - (1, 2, 3, 1, 2, 3)

# Multiplication duplicates the tuple.



# 12 Slice a tuple

numbers = (10, 20, 30, 40)

print(numbers[1:3])

# Slicing extracts a portion of the tuple.

# Output - (20, 30)

# Slice returns elements from index 1 to 2.



# 13 Convert tuple to list

numbers = (1, 2, 3)

lst = list(numbers)

print(lst)

# list() converts tuple to list.

# Output - [1, 2, 3]

# This allows modifying elements since lists are mutable.



# 14 Convert list to tuple

numbers = [1, 2, 3]

t = tuple(numbers)

print(t)

# tuple() converts list to tuple.

# Output - (1, 2, 3)

# tuple() creates an immutable collection.



# 15 Create single element tuple

t = (5,)

print(t)

# A comma is required to create a single element tuple.

# Output - (5,)

# Without the comma Python treats it as a normal value.



# 16 Tuple unpacking

t = (10, 20, 30)

a, b, c = t

print(a, b, c)

# Tuple elements can be assigned to variables.

# Output - 10 20 30

# This is called tuple unpacking.



# 17 Nested tuple

t = (1, (2, 3), 4)

print(t[1])

# Tuples can contain other tuples.

# Output - (2, 3)

# This is called a nested tuple.



# 18 Access element inside nested tuple

t = (1, (2, 3), 4)

print(t[1][0])

# First index selects inner tuple.

# Output - 2

# Second index accesses element inside nested tuple.



# 19 Find maximum element

numbers = (10, 5, 20)

print(max(numbers))

# max() returns largest element.

# Output - 20

# max() compares all elements in the tuple.



# 20 Find minimum element

numbers = (10, 5, 20)

print(min(numbers))

# min() returns smallest element.

# Output - 5

# min() finds the minimum value.



# 21 Find sum of elements

numbers = (1, 2, 3, 4)

print(sum(numbers))

# sum() adds all elements.

# Output - 10

# sum() computes the total of all elements.



# 22 Check tuple type

numbers = (1, 2, 3)

print(type(numbers))

# type() returns data type.

# Output - <class 'tuple'>

# This confirms the variable is a tuple.



# 23 Convert string to tuple

text = "hello"

t = tuple(text)

print(t)

# tuple() converts iterable to tuple.

# Output - ('h','e','l','l','o')

# Each character becomes a tuple element.



# 24 Check if tuple is empty

t = ()

print(len(t) == 0)

# An empty tuple has length 0.

# Output - True

# I check emptiness using len().



# 25 Create tuple using range

t = tuple(range(5))

print(t)

# range() generates numbers.

# Output - (0, 1, 2, 3, 4)

# tuple(range()) converts range to tuple.