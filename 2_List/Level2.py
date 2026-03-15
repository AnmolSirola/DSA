# 1 Find the largest element in a list

numbers = [10, 25, 8, 40, 15]

largest = max(numbers)

print(largest)

# max() returns the largest value in the list.

# Output - 40

# I used the built-in max() function which returns the maximum element from the list.



# 2 Find the smallest element in a list

numbers = [10, 25, 8, 40, 15]

smallest = min(numbers)

print(smallest)

# min() returns the smallest value in the list.

# Output - 8

# I used the built-in min() function which returns the smallest element.



# 3 Find the sum of elements in a list

numbers = [10, 20, 30]

total = sum(numbers)

print(total)

# sum() adds all elements of the list.

# Output - 60

# I used the built-in sum() function to calculate the total of all elements.



# 4 Find the average of list elements

numbers = [10, 20, 30]

average = sum(numbers) / len(numbers)

print(average)

# Average is calculated as sum divided by number of elements.

# Output - 20.0

# I calculated the average using sum() divided by len().



# 5 Count even numbers in a list

numbers = [1, 2, 3, 4, 5, 6]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(count)

# Even numbers are divisible by 2.

# Output - 3

# I loop through the list and count numbers divisible by 2.



# 6 Count odd numbers in a list

numbers = [1, 2, 3, 4, 5]

count = 0

for num in numbers:
    if num % 2 != 0:
        count += 1

print(count)

# Odd numbers are not divisible by 2.

# Output - 3

# I check if the remainder after dividing by 2 is not zero.



# 7 Find the second largest element

numbers = [10, 20, 4, 45, 99]

numbers.sort()

second_largest = numbers[-2]

print(second_largest)

# Sorting places numbers in ascending order.

# Output - 45

# After sorting, the second last element is the second largest.



# 8 Remove duplicates from a list

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))

print(unique)

# A set stores only unique elements.

# Output - [1,2,3,4,5]

# I converted the list to a set to remove duplicates.



# 9 Find duplicate elements in a list

numbers = [1, 2, 3, 2, 4, 1]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)

# count() checks how many times each element appears.

# Output - [1, 2]

# I check if the element appears more than once.



# 10 Find common elements in two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = list(set(list1) & set(list2))

print(common)

# '&' finds intersection of two sets.

# Output - [3,4]

# I converted lists to sets and found common elements.



# 11 Remove all occurrences of a value

numbers = [1, 2, 2, 3, 2, 4]

result = [x for x in numbers if x != 2]

print(result)

# List comprehension filters elements.

# Output - [1,3,4]

# I rebuild the list excluding the value 2.



# 12 Multiply all numbers in a list

numbers = [1, 2, 3, 4]

product = 1

for num in numbers:
    product *= num

print(product)

# Multiply each element with the running product.

# Output - 24

# I loop through the list and multiply each element.



# 13 Check if a list is empty

numbers = []

if not numbers:
    print("List is empty")

# An empty list evaluates to False.

# Output - List is empty

# I check the list using a boolean condition.



# 14 Flatten a nested list

nested = [[1,2],[3,4],[5,6]]

flat = [num for sublist in nested for num in sublist]

print(flat)

# Nested loops flatten the list.

# Output - [1,2,3,4,5,6]

# I used list comprehension to extract elements from sublists.



# 15 Move all zeros to the end

numbers = [0,1,0,3,12]

result = [x for x in numbers if x != 0] + [x for x in numbers if x == 0]

print(result)

# Separate non-zero and zero elements.

# Output - [1,3,12,0,0]

# I place all non-zero elements first and append zeros.



# 16 Check if a list is sorted

numbers = [1,2,3,4]

is_sorted = numbers == sorted(numbers)

print(is_sorted)

# Compare list with its sorted version.

# Output - True

# If both lists are equal, the list is sorted.



# 17 Reverse a list without built-in function

numbers = [1,2,3,4]

reversed_list = []

for num in numbers:
    reversed_list = [num] + reversed_list

print(reversed_list)

# Insert elements at the beginning.

# Output - [4,3,2,1]

# I build a new list by adding elements at the front.



# 18 Add two lists index-wise

list1 = [1,2,3]
list2 = [4,5,6]

result = []

for i in range(len(list1)):
    result.append(list1[i] + list2[i])

print(result)

# Add elements with the same index.

# Output - [5,7,9]

# I iterate through indices and add corresponding elements.



# 19 Find the difference between largest and smallest

numbers = [10, 5, 20, 8]

difference = max(numbers) - min(numbers)

print(difference)

# Difference = max - min.

# Output - 15

# I used max() and min() to compute the range.



# 20 Find the index of the largest element

numbers = [10, 25, 8, 40]

index = numbers.index(max(numbers))

print(index)

# max() finds the largest element.

# Output - 3

# index() returns the position of that element.



# 21 Remove negative numbers

numbers = [1, -2, 3, -4, 5]

result = [x for x in numbers if x >= 0]

print(result)

# Filter numbers greater than or equal to zero.

# Output - [1,3,5]

# I rebuild the list excluding negative values.



# 22 Find elements greater than a given value

numbers = [10, 20, 30, 5]

result = [x for x in numbers if x > 15]

print(result)

# Filter elements greater than 15.

# Output - [20,30]

# I use list comprehension with a condition.



# 23 Find the frequency of each element

numbers = [1,2,2,3,3,3]

frequency = {}

for num in numbers:
    frequency[num] = numbers.count(num)

print(frequency)

# count() calculates occurrences.

# Output - {1:1, 2:2, 3:3}

# I store element frequencies in a dictionary.



# 24 Rotate a list left by one position

numbers = [1,2,3,4]

rotated = numbers[1:] + numbers[:1]

print(rotated)

# Slice the list and rearrange.

# Output - [2,3,4,1]

# I move the first element to the end.



# 25 Check if a list is a palindrome

numbers = [1,2,3,2,1]

print(numbers == numbers[::-1])

# Compare list with its reverse.

# Output - True

# If both lists match, it is a palindrome.