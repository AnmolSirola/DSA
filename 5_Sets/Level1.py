# 1 Create a set

numbers = {1, 2, 3, 4}

print(numbers)

# A set is an unordered collection of unique elements.

# Output - {1, 2, 3, 4}

# Sets automatically remove duplicate elements.



# 2 Create a set using set()

numbers = set([1, 2, 3, 4])

print(numbers)

# set() converts a list into a set.

# Output - {1, 2, 3, 4}

# This is another way to create a set.



# 3 Check the type of a set

numbers = {1, 2, 3}

print(type(numbers))

# type() returns the data type.

# Output - <class 'set'>

# This confirms the variable is a set.



# 4 Add an element to a set

numbers = {1, 2, 3}

numbers.add(4)

print(numbers)

# add() inserts a new element into the set.

# Output - {1, 2, 3, 4}

# Sets ignore duplicates automatically.



# 5 Add multiple elements using update()

numbers = {1, 2}

numbers.update([3, 4])

print(numbers)

# update() adds multiple elements.

# Output - {1, 2, 3, 4}

# update() can take lists, tuples, or sets.



# 6 Remove an element using remove()

numbers = {1, 2, 3}

numbers.remove(2)

print(numbers)

# remove() deletes the element.

# Output - {1, 3}

# remove() raises an error if element does not exist.



# 7 Remove element using discard()

numbers = {1, 2, 3}

numbers.discard(2)

print(numbers)

# discard() removes element safely.

# Output - {1, 3}

# discard() does not raise error if element is absent.



# 8 Remove random element using pop()

numbers = {1, 2, 3}

numbers.pop()

print(numbers)

# pop() removes a random element.

# Output - example {2, 3}

# Sets are unordered so pop removes arbitrary element.



# 9 Clear a set

numbers = {1, 2, 3}

numbers.clear()

print(numbers)

# clear() removes all elements.

# Output - set()

# The set becomes empty.



# 10 Find length of a set

numbers = {1, 2, 3, 4}

print(len(numbers))

# len() counts elements.

# Output - 4

# Sets store unique values only.



# 11 Check membership

numbers = {1, 2, 3}

print(2 in numbers)

# 'in' checks if element exists.

# Output - True

# Membership testing is very fast in sets.



# 12 Check non-membership

numbers = {1, 2, 3}

print(5 not in numbers)

# 'not in' checks absence.

# Output - True

# Returns True if element is not present.



# 13 Iterate through a set

numbers = {1, 2, 3}

for num in numbers:
    print(num)

# Loop through elements.

# Output - 1 2 3 (order may vary)

# Sets are unordered.



# 14 Copy a set

numbers = {1, 2, 3}

copy_set = numbers.copy()

print(copy_set)

# copy() creates a new set.

# Output - {1, 2, 3}

# Changes in one set will not affect the other.



# 15 Convert list to set

numbers = [1, 2, 2, 3]

unique = set(numbers)

print(unique)

# set() removes duplicates.

# Output - {1, 2, 3}

# Useful for removing duplicates.



# 16 Convert set to list

numbers = {1, 2, 3}

lst = list(numbers)

print(lst)

# list() converts set to list.

# Output - [1, 2, 3]

# Lists allow indexing.



# 17 Create empty set

numbers = set()

print(numbers)

# {} creates dictionary, so set() is used.

# Output - set()

# set() initializes empty set.



# 18 Union of two sets

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

# '|' operator performs union.

# Output - {1, 2, 3, 4, 5}

# Union combines elements of both sets.



# 19 Intersection of sets

a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)

# '&' finds common elements.

# Output - {2, 3}

# Intersection returns shared elements.



# 20 Difference of sets

a = {1, 2, 3}
b = {2, 3}

print(a - b)

# '-' removes elements in second set.

# Output - {1}

# Difference returns elements only in first set.



# 21 Symmetric difference

a = {1, 2, 3}
b = {3, 4}

print(a ^ b)

# '^' returns elements in either set but not both.

# Output - {1, 2, 4}

# Symmetric difference excludes common elements.



# 22 Check subset

a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))

# issubset() checks if all elements exist in another set.

# Output - True

# Every element of a exists in b.



# 23 Check superset

a = {1, 2, 3}
b = {1, 2}

print(a.issuperset(b))

# issuperset() checks if set contains another set.

# Output - True

# All elements of b exist in a.



# 24 Check if sets are disjoint

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))

# isdisjoint() checks if sets share elements.

# Output - True

# No common elements exist.



# 25 Update set with union

a = {1, 2}
b = {3, 4}

a.update(b)

print(a)

# update() adds elements from another set.

# Output - {1, 2, 3, 4}

# Similar to union but modifies original set.



# 26 Intersection update

a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)

print(a)

# intersection_update keeps common elements.

# Output - {2, 3}

# It modifies the original set.



# 27 Difference update

a = {1, 2, 3}
b = {2}

a.difference_update(b)

print(a)

# difference_update removes elements present in other set.

# Output - {1, 3}

# Original set is modified.



# 28 Symmetric difference update

a = {1, 2, 3}
b = {3, 4}

a.symmetric_difference_update(b)

print(a)

# symmetric_difference_update updates with non-common elements.

# Output - {1, 2, 4}

# Removes common and adds unique elements.



# 29 Create set from string

text = "hello"

s = set(text)

print(s)

# set() creates unique characters.

# Output - {'h','e','l','o'}

# Duplicate characters are removed.



# 30 Remove duplicates from list

numbers = [1, 2, 2, 3, 4]

unique = list(set(numbers))

print(unique)

# set removes duplicates.

# Output - [1, 2, 3, 4]

# This is a common technique to remove duplicates.