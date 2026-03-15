# 1 Find the length of a list

numbers = [10, 20, 30, 40]

length = len(numbers)

print(length)

# len() returns the total number of elements in the list.

# Output - 4

# I used the built-in len() function which returns the number of elements in the list.



# 2 Access an element using index

numbers = [10, 20, 30, 40]

print(numbers[1])

# Lists are zero indexed, so index 1 refers to the second element.

# Output - 20

# Python lists are zero indexed, so accessing index 1 returns the second element.



# 3 Access the last element

numbers = [10, 20, 30, 40]

print(numbers[-1])

# Negative indexing starts from the end of the list.

# Output - 40

# Using -1 allows us to access the last element in the list.



# 4 Access the first element

numbers = [10, 20, 30, 40]

print(numbers[0])

# Index 0 always represents the first element of the list.

# Output - 10

# Since lists start at index 0, accessing index 0 returns the first element.



# 5 Add an element at the end of the list

numbers = [1, 2, 3]

numbers.append(4)

print(numbers)

# append() adds an element at the end of the list.

# Output - [1, 2, 3, 4]

# append() is used to insert a new element at the end of the list.



# 6 Insert an element at a specific index

numbers = [1, 2, 4]

numbers.insert(2, 3)

print(numbers)

# insert(index, value) adds an element at a specific position.

# Output - [1, 2, 3, 4]

# insert() allows inserting an element at a specific index in the list.



# 7 Remove an element by value

numbers = [1, 2, 3, 4]

numbers.remove(3)

print(numbers)

# remove() deletes the first occurrence of the specified value.

# Output - [1, 2, 4]

# remove() searches for the value and removes its first occurrence.



# 8 Remove the last element

numbers = [1, 2, 3]

numbers.pop()

print(numbers)

# pop() removes the last element of the list.

# Output - [1, 2]

# pop() removes and returns the last element.



# 9 Remove an element using index

numbers = [10, 20, 30, 40]

numbers.pop(1)

print(numbers)

# pop(index) removes the element at the given position.

# Output - [10, 30, 40]

# pop(index) removes the element at the specified index.



# 10 Find the index of an element

numbers = [10, 20, 30, 40]

print(numbers.index(30))

# index() returns the position of the first occurrence of the value.

# Output - 2

# index() searches the list and returns the index of the element.



# 11 Count occurrences of an element

numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))

# count() returns how many times a value appears in the list.

# Output - 3

# count() iterates through the list and counts occurrences.



# 12 Sort a list in ascending order

numbers = [4, 1, 3, 2]

numbers.sort()

print(numbers)

# sort() rearranges elements in ascending order.

# Output - [1, 2, 3, 4]

# sort() modifies the list in place and sorts elements.



# 13 Sort a list in descending order

numbers = [4, 1, 3, 2]

numbers.sort(reverse=True)

print(numbers)

# reverse=True sorts the list in descending order.

# Output - [4, 3, 2, 1]

# sort(reverse=True) sorts the list from largest to smallest.



# 14 Reverse a list

numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)

# reverse() reverses the order of elements in the list.

# Output - [4, 3, 2, 1]

# reverse() modifies the list in place.



# 15 Copy a list

list1 = [1, 2, 3]

list2 = list1.copy()

print(list2)

# copy() creates a new list with the same elements.

# Output - [1, 2, 3]

# copy() prevents changes in one list from affecting the other.



# 16 Merge two lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)

# Using + concatenates two lists.

# Output - [1, 2, 3, 4, 5, 6]

# The + operator combines both lists into one.



# 17 Extend a list

list1 = [1, 2, 3]
list2 = [4, 5]

list1.extend(list2)

print(list1)

# extend() adds elements from another list.

# Output - [1, 2, 3, 4, 5]

# extend() appends each element of the second list.



# 18 Repeat a list

numbers = [1, 2, 3]

print(numbers * 2)

# Multiplying a list repeats its elements.

# Output - [1, 2, 3, 1, 2, 3]

# The * operator duplicates the list.



# 19 Check if an element exists

numbers = [1, 2, 3, 4]

print(3 in numbers)

# The 'in' operator checks membership.

# Output - True

# It returns True if the element exists in the list.



# 20 Check if an element does not exist

numbers = [1, 2, 3]

print(5 not in numbers)

# 'not in' checks if the element is absent.

# Output - True

# Returns True if the element is not present.



# 21 Clear a list

numbers = [1, 2, 3]

numbers.clear()

print(numbers)

# clear() removes all elements from the list.

# Output - []

# After clearing, the list becomes empty.



# 22 Convert tuple to list

t = (1, 2, 3)

lst = list(t)

print(lst)

# list() converts iterable objects into lists.

# Output - [1, 2, 3]

# Here we convert a tuple into a list.



# 23 Convert string to list

text = "hello"

letters = list(text)

print(letters)

# list() splits a string into individual characters.

# Output - ['h', 'e', 'l', 'l', 'o']

# Each character becomes an element in the list.



# 24 Create list using range

numbers = list(range(5))

print(numbers)

# range(5) generates numbers from 0 to 4.

# Output - [0, 1, 2, 3, 4]

# list(range()) converts the range into a list.



# 25 Create list using list comprehension

numbers = [x for x in range(5)]

print(numbers)

# List comprehension is a compact way to create lists.

# Output - [0, 1, 2, 3, 4]

# It iterates through range and stores values in a list.