numbers = [1, 2, 2, 3, 4, 4, 5]

# set(numbers)

# A set stores only unique elements.

# list(set(numbers))

# Convert it back to a list.
unique = list(set(numbers))

print(unique)



# Find common elements in two lists
list1 = [1,2,3,4]
list2 = [3,4,5,6]

common = list(set(list1) & set(list2))

print(common)

#Output [3,4]

# Find duplicate elements
numbers = [1,2,3,2,4,1]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)

#Output - [1,2]