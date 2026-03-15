# 1 Create an array using Python list (Python uses lists as arrays)

arr = [10, 20, 30, 40]

print(arr)

# In Python, lists are commonly used as arrays.

# Output - [10, 20, 30, 40]

# Python does not have a fixed array structure like C/C++, so lists are used as dynamic arrays.



# 2 Access element using index

arr = [10, 20, 30, 40]

print(arr[2])

# Arrays use zero-based indexing.

# Output - 30

# Index 2 refers to the third element.



# 3 Access the first element

arr = [5, 10, 15]

print(arr[0])

# Index 0 always represents the first element.

# Output - 5

# Arrays start indexing from 0.



# 4 Access the last element

arr = [5, 10, 15]

print(arr[-1])

# Negative indexing accesses elements from the end.

# Output - 15

# -1 refers to the last element.



# 5 Find the length of an array

arr = [10, 20, 30, 40]

length = len(arr)

print(length)

# len() returns the number of elements.

# Output - 4

# I used len() to determine the size of the array.



# 6 Iterate through an array

arr = [10, 20, 30]

for num in arr:
    print(num)

# A loop allows us to access each element.

# Output - 10 20 30

# I iterate through the array using a for loop.



# 7 Iterate using index

arr = [10, 20, 30]

for i in range(len(arr)):
    print(arr[i])

# range(len(arr)) generates indices.

# Output - 10 20 30

# I iterate through indices to access elements.



# 8 Add element to array

arr = [1, 2, 3]

arr.append(4)

print(arr)

# append() adds an element to the end.

# Output - [1, 2, 3, 4]

# append() dynamically expands the array.



# 9 Insert element at specific index

arr = [1, 2, 4]

arr.insert(2, 3)

print(arr)

# insert(index,value) inserts element at position.

# Output - [1, 2, 3, 4]

# insert() shifts elements to the right.



# 10 Remove element by value

arr = [10, 20, 30]

arr.remove(20)

print(arr)

# remove() deletes the specified value.

# Output - [10, 30]

# remove() removes the first occurrence of the value.



# 11 Remove element using index

arr = [10, 20, 30]

arr.pop(1)

print(arr)

# pop(index) removes element at index.

# Output - [10, 30]

# pop() removes and returns the element.



# 12 Reverse an array

arr = [1, 2, 3, 4]

arr.reverse()

print(arr)

# reverse() reverses order of elements.

# Output - [4, 3, 2, 1]

# reverse() modifies the array in place.



# 13 Sort an array in ascending order

arr = [4, 1, 3, 2]

arr.sort()

print(arr)

# sort() arranges elements in ascending order.

# Output - [1, 2, 3, 4]

# sort() modifies the array.



# 14 Sort array in descending order

arr = [4, 1, 3, 2]

arr.sort(reverse=True)

print(arr)

# reverse=True sorts elements from largest to smallest.

# Output - [4, 3, 2, 1]

# sort(reverse=True) changes sorting order.



# 15 Find maximum element

arr = [10, 50, 20, 5]

print(max(arr))

# max() returns largest element.

# Output - 50

# I used the built-in max() function.



# 16 Find minimum element

arr = [10, 50, 20, 5]

print(min(arr))

# min() returns smallest element.

# Output - 5

# I used min() to find smallest element.



# 17 Find sum of elements

arr = [1, 2, 3, 4]

print(sum(arr))

# sum() adds all elements.

# Output - 10

# sum() calculates the total.



# 18 Find average of array

arr = [10, 20, 30]

average = sum(arr) / len(arr)

print(average)

# Average = sum / number of elements.

# Output - 20.0

# I divide the sum by the length.



# 19 Check if element exists

arr = [1, 2, 3, 4]

print(3 in arr)

# 'in' checks membership.

# Output - True

# Returns True if element exists.



# 20 Find index of element

arr = [10, 20, 30]

print(arr.index(20))

# index() returns position of element.

# Output - 1

# index() searches for the value.



# 21 Count occurrences of element

arr = [1, 2, 2, 3]

print(arr.count(2))

# count() returns number of times element appears.

# Output - 2

# count() counts occurrences.



# 22 Copy an array

arr = [1, 2, 3]

arr_copy = arr.copy()

print(arr_copy)

# copy() creates a new array.

# Output - [1, 2, 3]

# Changes in one array will not affect the other.



# 23 Merge two arrays

arr1 = [1, 2]
arr2 = [3, 4]

result = arr1 + arr2

print(result)

# '+' concatenates arrays.

# Output - [1, 2, 3, 4]

# This combines two arrays.



# 24 Create array using range

arr = list(range(5))

print(arr)

# range() generates numbers.

# Output - [0, 1, 2, 3, 4]

# list(range()) converts range to array.



# 25 Create array using list comprehension

arr = [x for x in range(5)]

print(arr)

# List comprehension generates elements.

# Output - [0, 1, 2, 3, 4]

# This is a concise way to build arrays.