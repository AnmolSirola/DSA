# 1 Find the largest element in a tuple

t = (10, 25, 8, 40, 15)

largest = t[0]

for num in t:
    if num > largest:
        largest = num

print(largest)

# Iterate through tuple and track the largest value.

# Output - 40

# I compare each element and update the largest value found.



# 2 Find the smallest element in a tuple

t = (10, 25, 8, 40, 15)

smallest = t[0]

for num in t:
    if num < smallest:
        smallest = num

print(smallest)

# Compare elements to track the smallest value.

# Output - 8

# I update the smallest element whenever a smaller value appears.



# 3 Find the second largest element

t = (10, 20, 4, 45, 99)

sorted_t = sorted(t)

print(sorted_t[-2])

# sorted() converts tuple into sorted list.

# Output - 45

# After sorting, the second last element is the second largest.



# 4 Reverse a tuple

t = (1, 2, 3, 4)

reversed_t = t[::-1]

print(reversed_t)

# Slicing with step -1 reverses the tuple.

# Output - (4, 3, 2, 1)

# I used slicing to reverse the tuple.



# 5 Check if tuple is palindrome

t = (1, 2, 3, 2, 1)

print(t == t[::-1])

# Compare tuple with its reversed version.

# Output - True

# If both tuples match, it is a palindrome.



# 6 Count even numbers in tuple

t = (1, 2, 3, 4, 5, 6)

count = 0

for num in t:
    if num % 2 == 0:
        count += 1

print(count)

# Even numbers are divisible by 2.

# Output - 3

# I count numbers divisible by 2.



# 7 Count odd numbers in tuple

t = (1, 2, 3, 4, 5)

count = 0

for num in t:
    if num % 2 != 0:
        count += 1

print(count)

# Odd numbers are not divisible by 2.

# Output - 3

# I count numbers that leave remainder when divided by 2.



# 8 Find sum of tuple elements

t = (1, 2, 3, 4)

total = 0

for num in t:
    total += num

print(total)

# Add elements one by one.

# Output - 10

# I accumulate values while iterating.



# 9 Find average of tuple elements

t = (10, 20, 30)

avg = sum(t) / len(t)

print(avg)

# Average = sum / number of elements.

# Output - 20.0

# I divide the total sum by number of elements.



# 10 Remove duplicates from tuple

t = (1, 2, 2, 3, 4, 4)

unique = tuple(set(t))

print(unique)

# Set removes duplicate elements.

# Output - (1, 2, 3, 4)

# I convert tuple to set and back.



# 11 Find duplicate elements

t = (1, 2, 3, 2, 4, 1)

duplicates = []

for num in t:
    if t.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(tuple(duplicates))

# count() checks occurrences.

# Output - (1, 2)

# I collect elements appearing more than once.



# 12 Flatten nested tuple

t = ((1,2),(3,4),(5,6))

flat = []

for sub in t:
    for num in sub:
        flat.append(num)

print(tuple(flat))

# Nested loops flatten the tuple.

# Output - (1, 2, 3, 4, 5, 6)

# I iterate through sub-tuples.



# 13 Find common elements between two tuples

t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

common = tuple(set(t1) & set(t2))

print(common)

# Intersection of sets finds common elements.

# Output - (3, 4)

# I convert tuples to sets.



# 14 Find elements greater than a value

t = (10, 20, 30, 5)

result = tuple(x for x in t if x > 15)

print(result)

# Filter elements greater than threshold.

# Output - (20, 30)

# I rebuild the tuple using comprehension.



# 15 Multiply all elements

t = (1, 2, 3, 4)

product = 1

for num in t:
    product *= num

print(product)

# Multiply each element.

# Output - 24

# I update product during iteration.



# 16 Find index of largest element

t = (10, 25, 8, 40)

index = t.index(max(t))

print(index)

# max() finds largest value.

# Output - 3

# index() returns the position.



# 17 Square all elements

t = (1, 2, 3)

squares = tuple(x**2 for x in t)

print(squares)

# Transform each element.

# Output - (1, 4, 9)

# I square each value using comprehension.



# 18 Find frequency of elements

t = (1, 2, 2, 3, 3, 3)

freq = {}

for num in t:
    freq[num] = freq.get(num,0) + 1

print(freq)

# Dictionary stores counts.

# Output - {1:1,2:2,3:3}

# I use dictionary to count occurrences.



# 19 Add two tuples element-wise

t1 = (1,2,3)
t2 = (4,5,6)

result = tuple(t1[i] + t2[i] for i in range(len(t1)))

print(result)

# Add values at same index.

# Output - (5,7,9)

# I iterate through indices.



# 20 Separate even and odd numbers

t = (1,2,3,4,5)

even = tuple(x for x in t if x%2==0)
odd = tuple(x for x in t if x%2!=0)

print(even, odd)

# Filter elements based on condition.

# Output - (2,4) (1,3,5)

# I categorize numbers.



# 21 Count elements greater than average

t = (10,20,30)

avg = sum(t)/len(t)

count = len([x for x in t if x > avg])

print(count)

# Compare elements with average.

# Output - 1

# I filter elements greater than average.



# 22 Find cumulative sum

t = (1,2,3,4)

cumsum = []

total = 0

for num in t:
    total += num
    cumsum.append(total)

print(tuple(cumsum))

# Running sum stored sequentially.

# Output - (1,3,6,10)

# I keep updating cumulative sum.



# 23 Replace negative numbers with zero

t = (1,-2,3,-4)

result = tuple(0 if x < 0 else x for x in t)

print(result)

# Conditional replacement.

# Output - (1,0,3,0)

# I replace negative numbers with zero.



# 24 Find maximum difference

t = (10,5,20,8)

difference = max(t) - min(t)

print(difference)

# Difference = max - min.

# Output - 15

# I compute difference between largest and smallest.



# 25 Convert tuple of tuples into dictionary

pairs = (("a",1),("b",2),("c",3))

d = dict(pairs)

print(d)

# dict() converts pairs into dictionary.

# Output - {'a':1,'b':2,'c':3}

# Each tuple becomes key-value pair.



# 26 Find pair with given sum

t = (1,2,3,4,5)

target = 6

for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i] + t[j] == target:
            print(t[i],t[j])

# Check all pairs.

# Output - 1 5 / 2 4

# I use nested loops to find matching pairs.



# 27 Remove specific value

t = (1,2,3,2,4)

result = tuple(x for x in t if x != 2)

print(result)

# Filter out unwanted value.

# Output - (1,3,4)

# I rebuild tuple excluding the value.



# 28 Find smallest missing positive number

t = (1,2,4,5)

i = 1

while True:
    if i not in t:
        print(i)
        break
    i += 1

# Check numbers sequentially.

# Output - 3

# I increment until missing value found.



# 29 Count occurrences of each element

t = (1,2,2,3,3,3)

counts = {}

for num in t:
    counts[num] = counts.get(num,0) + 1

print(counts)

# Dictionary tracks frequencies.

# Output - {1:1,2:2,3:3}

# I use dictionary to count elements.



# 30 Merge two tuples and remove duplicates

t1 = (1,2,3)
t2 = (3,4,5)

merged = tuple(set(t1 + t2))

print(merged)

# Concatenate then remove duplicates.

# Output - (1,2,3,4,5)

# I merge tuples and convert to set.



# 31 Find maximum sum of two elements

t = (10,20,5,8)

sorted_t = sorted(t)

print(sorted_t[-1] + sorted_t[-2])

# Largest two elements added.

# Output - 30

# After sorting, last two elements are largest.



# 32 Count numbers divisible by 3

t = (3,6,7,9,10)

count = 0

for num in t:
    if num % 3 == 0:
        count += 1

print(count)

# Check divisibility by 3.

# Output - 3

# I count numbers divisible by 3.



# 33 Convert tuple to string

t = ('H','e','l','l','o')

s = "".join(t)

print(s)

# join() combines characters.

# Output - Hello

# I convert tuple of characters into string.



# 34 Find longest tuple inside tuple

t = ((1,2),(1,2,3),(4,5))

longest = max(t, key=len)

print(longest)

# key=len compares lengths.

# Output - (1,2,3)

# max() finds tuple with greatest length.



# 35 Find tuples containing a specific element

t = ((1,2),(3,4),(2,5))

result = [sub for sub in t if 2 in sub]

print(result)

# Check membership inside each tuple.

# Output - [(1,2),(2,5)]

# I filter tuples containing the value.