# 1 Find the largest element in an array

arr = [10, 25, 8, 40, 15]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print(largest)

# Iterate through array and keep updating the largest value.

# Output - 40

# I compare each element and update the largest value found.



# 2 Find the smallest element in an array

arr = [10, 25, 8, 40, 15]

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print(smallest)

# Compare each element with the current smallest.

# Output - 8

# I update the smallest value whenever a smaller element is found.



# 3 Find the second largest element

arr = [10, 20, 4, 45, 99]

arr.sort()

print(arr[-2])

# Sorting places the second largest element at index -2.

# Output - 45

# After sorting, the second last element is the second largest.



# 4 Reverse an array without built-in functions

arr = [1, 2, 3, 4]

reversed_arr = []

for num in arr:
    reversed_arr = [num] + reversed_arr

print(reversed_arr)

# Insert elements at the beginning of a new array.

# Output - [4, 3, 2, 1]

# I build the reversed array by placing elements at the front.



# 5 Check if array is sorted

arr = [1, 2, 3, 4]

is_sorted = arr == sorted(arr)

print(is_sorted)

# Compare array with its sorted version.

# Output - True

# If both arrays match, the array is sorted.



# 6 Remove duplicates from array

arr = [1, 2, 2, 3, 4, 4]

unique = list(set(arr))

print(unique)

# Set removes duplicate elements.

# Output - [1, 2, 3, 4]

# I convert the array to a set and back to remove duplicates.



# 7 Find duplicate elements

arr = [1, 2, 3, 2, 4, 1]

duplicates = []

for num in arr:
    if arr.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)

# count() checks occurrences.

# Output - [1, 2]

# I collect numbers appearing more than once.



# 8 Move zeros to the end

arr = [0, 1, 0, 3, 12]

result = [x for x in arr if x != 0] + [x for x in arr if x == 0]

print(result)

# Separate non-zero and zero elements.

# Output - [1, 3, 12, 0, 0]

# I rebuild the array placing zeros at the end.



# 9 Count even numbers

arr = [1, 2, 3, 4, 5, 6]

count = 0

for num in arr:
    if num % 2 == 0:
        count += 1

print(count)

# Even numbers are divisible by 2.

# Output - 3

# I check divisibility by 2.



# 10 Count odd numbers

arr = [1, 2, 3, 4, 5]

count = 0

for num in arr:
    if num % 2 != 0:
        count += 1

print(count)

# Odd numbers are not divisible by 2.

# Output - 3

# I check remainder when dividing by 2.



# 11 Find sum of array elements

arr = [1, 2, 3, 4]

total = 0

for num in arr:
    total += num

print(total)

# Add each element to total.

# Output - 10

# I accumulate values while iterating.



# 12 Find average of array

arr = [10, 20, 30]

avg = sum(arr) / len(arr)

print(avg)

# Average = sum / number of elements.

# Output - 20.0

# I divide total sum by length.



# 13 Find common elements in two arrays

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

common = list(set(arr1) & set(arr2))

print(common)

# Intersection of sets gives common elements.

# Output - [3, 4]

# I convert arrays to sets and find intersection.



# 14 Find elements greater than a value

arr = [10, 20, 30, 5]

result = [x for x in arr if x > 15]

print(result)

# Filter elements greater than 15.

# Output - [20, 30]

# I use list comprehension to filter elements.



# 15 Rotate array left by one

arr = [1, 2, 3, 4]

rotated = arr[1:] + arr[:1]

print(rotated)

# Slice and rearrange.

# Output - [2, 3, 4, 1]

# I move the first element to the end.



# 16 Rotate array right by one

arr = [1, 2, 3, 4]

rotated = arr[-1:] + arr[:-1]

print(rotated)

# Move last element to front.

# Output - [4, 1, 2, 3]

# I slice the last element and place it first.



# 17 Find maximum difference

arr = [10, 5, 20, 8]

difference = max(arr) - min(arr)

print(difference)

# Difference = max - min.

# Output - 15

# I use max() and min().



# 18 Multiply all elements

arr = [1, 2, 3, 4]

product = 1

for num in arr:
    product *= num

print(product)

# Multiply elements sequentially.

# Output - 24

# I update product each iteration.



# 19 Flatten nested array

arr = [[1,2],[3,4],[5,6]]

flat = [num for sub in arr for num in sub]

print(flat)

# Nested loops flatten array.

# Output - [1,2,3,4,5,6]

# I iterate through subarrays.



# 20 Find index of largest element

arr = [10, 25, 8, 40]

index = arr.index(max(arr))

print(index)

# Find max value then its index.

# Output - 3

# index() returns the position.



# 21 Remove negative numbers

arr = [1, -2, 3, -4, 5]

result = [x for x in arr if x >= 0]

print(result)

# Filter non-negative numbers.

# Output - [1, 3, 5]

# I rebuild array excluding negatives.



# 22 Square all elements

arr = [1, 2, 3]

squares = [x**2 for x in arr]

print(squares)

# Each element is squared.

# Output - [1, 4, 9]

# List comprehension transforms elements.



# 23 Find frequency of elements

arr = [1,2,2,3,3,3]

freq = {}

for num in arr:
    freq[num] = freq.get(num,0) + 1

print(freq)

# Dictionary tracks counts.

# Output - {1:1,2:2,3:3}

# I store frequencies in dictionary.



# 24 Add two arrays element-wise

arr1 = [1,2,3]
arr2 = [4,5,6]

result = []

for i in range(len(arr1)):
    result.append(arr1[i] + arr2[i])

print(result)

# Add elements with same index.

# Output - [5,7,9]

# I iterate through indices.



# 25 Find missing number

arr = [1,2,4,5]

for i in range(1,6):
    if i not in arr:
        print(i)

# Check which number is absent.

# Output - 3

# I compare expected range with array.



# 26 Check if array is palindrome

arr = [1,2,3,2,1]

print(arr == arr[::-1])

# Compare with reversed array.

# Output - True

# If both arrays match, it is palindrome.



# 27 Remove specific value

arr = [1,2,3,2,4]

result = [x for x in arr if x != 2]

print(result)

# Filter out unwanted value.

# Output - [1,3,4]

# I rebuild array excluding the value.



# 28 Count elements greater than average

arr = [10,20,30]

avg = sum(arr)/len(arr)

count = len([x for x in arr if x > avg])

print(count)

# Compare each element with average.

# Output - 1

# I filter elements greater than average.



# 29 Find pair with given sum

arr = [1,2,3,4,5]

target = 6

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == target:
            print(arr[i],arr[j])

# Check all pairs.

# Output - 1 5 / 2 4

# I use nested loops to find pairs.



# 30 Find smallest missing positive number

arr = [1,2,0]

i = 1

while True:
    if i not in arr:
        print(i)
        break
    i += 1

# Check positive numbers sequentially.

# Output - 3

# I increment until a missing number is found.



# 31 Separate even and odd numbers

arr = [1,2,3,4,5]

even = [x for x in arr if x%2==0]
odd = [x for x in arr if x%2!=0]

print(even,odd)

# Filter based on divisibility.

# Output - [2,4] [1,3,5]

# I categorize numbers into two arrays.



# 32 Find cumulative sum

arr = [1,2,3,4]

cumsum = []

total = 0

for num in arr:
    total += num
    cumsum.append(total)

print(cumsum)

# Running sum is stored.

# Output - [1,3,6,10]

# I keep updating cumulative total.



# 33 Remove element at specific position

arr = [10,20,30,40]

index = 2

arr.pop(index)

print(arr)

# pop(index) removes element at position.

# Output - [10,20,40]

# pop() removes element using index.



# 34 Replace negative numbers with zero

arr = [1,-2,3,-4]

result = [0 if x<0 else x for x in arr]

print(result)

# Conditional replacement.

# Output - [1,0,3,0]

# I replace negative values with zero.



# 35 Find maximum sum of two elements

arr = [10,20,5,8]

arr.sort()

print(arr[-1] + arr[-2])

# Largest two numbers are added.

# Output - 30

# After sorting, last two elements are largest.