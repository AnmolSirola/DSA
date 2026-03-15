# 1 Find common elements between two lists using sets

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)

print(common)

# '&' performs intersection between sets.

# Output - {3, 4}

# I convert lists to sets and find common elements using intersection.



# 2 Remove duplicates from a list

numbers = [1, 2, 2, 3, 4, 4]

unique = list(set(numbers))

print(unique)

# set removes duplicate values automatically.

# Output - [1, 2, 3, 4]

# I convert the list into a set to remove duplicates.



# 3 Check if two lists have common elements

list1 = [1, 2, 3]
list2 = [4, 5, 3]

result = not set(list1).isdisjoint(list2)

print(result)

# isdisjoint checks if two sets share elements.

# Output - True

# Since 3 exists in both lists, the result is True.



# 4 Find elements present in first list but not second

list1 = [1, 2, 3, 4]
list2 = [3, 4]

result = set(list1) - set(list2)

print(result)

# '-' finds difference between sets.

# Output - {1, 2}

# I subtract elements of the second set from the first.



# 5 Find union of two lists

list1 = [1, 2, 3]
list2 = [3, 4, 5]

union = set(list1) | set(list2)

print(union)

# '|' performs union operation.

# Output - {1, 2, 3, 4, 5}

# Union combines elements from both lists.



# 6 Find symmetric difference between lists

list1 = [1, 2, 3]
list2 = [3, 4, 5]

result = set(list1) ^ set(list2)

print(result)

# '^' finds elements present in only one set.

# Output - {1, 2, 4, 5}

# Elements common to both sets are removed.



# 7 Check if one set is subset of another

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))

# issubset checks if all elements of a exist in b.

# Output - True

# Every element of a is present in b.



# 8 Check if one set is superset of another

a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))

# issuperset checks if a contains all elements of b.

# Output - True

# a includes every element of b.



# 9 Find common characters in two strings

s1 = "hello"
s2 = "world"

common = set(s1) & set(s2)

print(common)

# Convert strings to sets to compare characters.

# Output - {'o', 'l'}

# Intersection finds shared characters.



# 10 Find unique characters in a string

text = "programming"

unique = set(text)

print(unique)

# set removes duplicate characters.

# Output - {'p','r','o','g','a','m','i','n'}

# Only unique characters remain.



# 11 Check if list contains duplicates

numbers = [1, 2, 3, 3]

print(len(numbers) != len(set(numbers)))

# Duplicate exists if lengths differ.

# Output - True

# set removes duplicates so length changes.



# 12 Find number of unique elements

numbers = [1, 2, 2, 3, 4, 4]

print(len(set(numbers)))

# set removes duplicates.

# Output - 4

# I count unique elements using len().



# 13 Find common elements among three sets

a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 4, 5}

result = a & b & c

print(result)

# Intersection across three sets.

# Output - {3}

# Element must exist in all sets.



# 14 Find union of multiple sets

a = {1, 2}
b = {2, 3}
c = {3, 4}

result = a | b | c

print(result)

# Union combines all elements.

# Output - {1, 2, 3, 4}

# Elements appear only once.



# 15 Find elements present in exactly one set

a = {1, 2}
b = {2, 3}

result = a ^ b

print(result)

# Symmetric difference removes common elements.

# Output - {1, 3}

# Elements appear in only one set.



# 16 Remove duplicates while preserving order

numbers = [1, 2, 2, 3, 4]

seen = set()
result = []

for num in numbers:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)

# Set tracks seen elements.

# Output - [1, 2, 3, 4]

# This keeps the original order.



# 17 Find elements greater than 2

s = {1, 2, 3, 4, 5}

result = {x for x in s if x > 2}

print(result)

# Set comprehension filters elements.

# Output - {3, 4, 5}

# I filter values greater than 2.



# 18 Convert list to set and back to list

numbers = [1, 2, 2, 3]

unique_list = list(set(numbers))

print(unique_list)

# set removes duplicates.

# Output - [1, 2, 3]

# Convert back to list for indexing.



# 19 Check if two sets share elements

a = {1, 2, 3}
b = {4, 5}

print(not a.isdisjoint(b))

# isdisjoint checks if sets share elements.

# Output - False

# These sets share no elements.



# 20 Find difference between sets

a = {1, 2, 3}
b = {2}

result = a.difference(b)

print(result)

# difference removes elements present in other set.

# Output - {1, 3}

# Only elements unique to a remain.



# 21 Find intersection size

a = {1, 2, 3}
b = {2, 3, 4}

print(len(a & b))

# Intersection gives common elements.

# Output - 2

# I count elements in the intersection.



# 22 Check if set is empty

s = set()

print(len(s) == 0)

# Empty set has length 0.

# Output - True

# I check emptiness using len().



# 23 Find largest element in set

s = {10, 20, 5}

print(max(s))

# max returns largest value.

# Output - 20

# I used the built-in max() function.



# 24 Find smallest element in set

s = {10, 20, 5}

print(min(s))

# min returns smallest value.

# Output - 5

# I used the built-in min() function.



# 25 Sum elements of set

s = {1, 2, 3, 4}

print(sum(s))

# sum adds all elements.

# Output - 10

# Built-in sum() calculates total.



# 26 Convert string to set

text = "hello"

s = set(text)

print(s)

# set stores unique characters.

# Output - {'h','e','l','o'}

# Duplicate letters removed.



# 27 Find difference between two strings

s1 = "hello"
s2 = "world"

diff = set(s1) - set(s2)

print(diff)

# Convert strings to sets.

# Output - {'h','e'}

# Characters in s1 but not s2.



# 28 Check membership in set

s = {1, 2, 3}

print(2 in s)

# 'in' checks membership.

# Output - True

# Returns True if element exists.



# 29 Find symmetric difference using method

a = {1, 2, 3}
b = {3, 4}

result = a.symmetric_difference(b)

print(result)

# symmetric_difference returns elements not shared.

# Output - {1, 2, 4}

# Same as '^' operator.



# 30 Convert set to sorted list

s = {4, 1, 3}

sorted_list = sorted(s)

print(sorted_list)

# sorted converts set to ordered list.

# Output - [1, 3, 4]

# Sets are unordered by default.