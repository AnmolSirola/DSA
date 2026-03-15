# 1 Count frequency of elements in a list using a dictionary

numbers = [1, 2, 2, 3, 3, 3]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

# A dictionary is used to store counts of each element.

# Output - {1: 1, 2: 2, 3: 3}

# I iterate through the list and update the count of each element in the dictionary.



# 2 Count frequency of characters in a string

text = "banana"

freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)

# get() helps retrieve the value safely with a default.

# Output - {'b':1,'a':3,'n':2}

# I use get() to initialize counts if the key does not exist.



# 3 Find the key with the maximum value

data = {"a": 10, "b": 25, "c": 5}

key = max(data, key=data.get)

print(key)

# max() can be used with key=data.get to find the key with the highest value.

# Output - b

# I used max() with dictionary values to determine the key with the largest value.



# 4 Find the key with the minimum value

data = {"a": 10, "b": 25, "c": 5}

key = min(data, key=data.get)

print(key)

# min() finds the key associated with the smallest value.

# Output - c

# I used min() with key=data.get.



# 5 Invert a dictionary (swap keys and values)

data = {"a": 1, "b": 2, "c": 3}

inverted = {v: k for k, v in data.items()}

print(inverted)

# Dictionary comprehension swaps keys and values.

# Output - {1:'a',2:'b',3:'c'}

# I iterate over key-value pairs and reverse them.



# 6 Merge two dictionaries

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = {**d1, **d2}

print(merged)

# ** unpacks dictionaries and merges them.

# Output - {'a':1,'b':2,'c':3,'d':4}

# I merged two dictionaries using dictionary unpacking.



# 7 Sum all values in a dictionary

data = {"a": 10, "b": 20, "c": 30}

total = sum(data.values())

print(total)

# values() returns all dictionary values.

# Output - 60

# I summed all values using sum().



# 8 Multiply all values in a dictionary

data = {"a": 2, "b": 3, "c": 4}

product = 1

for value in data.values():
    product *= value

print(product)

# Multiply each value.

# Output - 24

# I iterate over dictionary values and multiply them.



# 9 Find length of dictionary

data = {"a": 1, "b": 2, "c": 3}

print(len(data))

# len() counts key-value pairs.

# Output - 3

# len() returns number of entries.



# 10 Remove a key if it exists

data = {"a": 1, "b": 2}

key = "b"

if key in data:
    del data[key]

print(data)

# Check existence before deletion.

# Output - {'a':1}

# I safely remove the key using membership check.



# 11 Sort dictionary by keys

data = {"b": 2, "a": 1, "c": 3}

sorted_dict = dict(sorted(data.items()))

print(sorted_dict)

# sorted() sorts key-value pairs.

# Output - {'a':1,'b':2,'c':3}

# I sorted the dictionary based on keys.



# 12 Sort dictionary by values

data = {"a": 3, "b": 1, "c": 2}

sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))

print(sorted_dict)

# lambda extracts values for sorting.

# Output - {'b':1,'c':2,'a':3}

# I sorted based on dictionary values.



# 13 Find the most frequent element

numbers = [1,2,2,3,3,3]

freq = {}

for n in numbers:
    freq[n] = freq.get(n,0) + 1

most_freq = max(freq, key=freq.get)

print(most_freq)

# max() finds element with highest frequency.

# Output - 3

# I used frequency dictionary then max().



# 14 Group numbers by even and odd

numbers = [1,2,3,4,5]

group = {"even":[], "odd":[]}

for n in numbers:
    if n % 2 == 0:
        group["even"].append(n)
    else:
        group["odd"].append(n)

print(group)

# Separate numbers using dictionary categories.

# Output - {'even':[2,4],'odd':[1,3,5]}

# I categorized numbers using keys.



# 15 Create dictionary from two lists

keys = ["name","age"]
values = ["Anmol",22]

d = dict(zip(keys,values))

print(d)

# zip pairs elements together.

# Output - {'name':'Anmol','age':22}

# I used zip to combine two lists.



# 16 Find common keys between dictionaries

d1 = {"a":1,"b":2}
d2 = {"b":3,"c":4}

common = d1.keys() & d2.keys()

print(common)

# '&' finds intersection.

# Output - {'b'}

# I used set intersection of keys.



# 17 Remove keys with specific value

data = {"a":1,"b":0,"c":2}

result = {k:v for k,v in data.items() if v != 0}

print(result)

# Dictionary comprehension filters values.

# Output - {'a':1,'c':2}

# I rebuild the dictionary excluding unwanted values.



# 18 Check if two dictionaries are equal

d1 = {"a":1,"b":2}
d2 = {"a":1,"b":2}

print(d1 == d2)

# Equality checks key-value pairs.

# Output - True

# Python compares both dictionaries directly.



# 19 Convert list of tuples to dictionary

pairs = [("a",1),("b",2)]

d = dict(pairs)

print(d)

# dict() converts tuples to dictionary.

# Output - {'a':1,'b':2}

# Each tuple becomes key-value pair.



# 20 Find total number of keys

data = {"a":1,"b":2,"c":3}

print(len(data.keys()))

# keys() returns all keys.

# Output - 3

# I count keys using len().



# 21 Count vowels in a string

text = "hello"

vowels = "aeiou"

count = {}

for char in text:
    if char in vowels:
        count[char] = count.get(char,0) + 1

print(count)

# Dictionary stores vowel frequencies.

# Output - {'e':1,'o':1}

# I track vowel counts using dictionary.



# 22 Map numbers to their squares

numbers = [1,2,3,4]

square = {n:n*n for n in numbers}

print(square)

# Dictionary comprehension builds mapping.

# Output - {1:1,2:4,3:9,4:16}

# Keys are numbers and values are their squares.



# 23 Find key with maximum length

data = {"apple":1,"banana":2,"kiwi":3}

longest = max(data, key=len)

print(longest)

# key=len compares length of keys.

# Output - banana

# max() identifies longest key.



# 24 Create dictionary from string characters

text = "abc"

d = {char:ord(char) for char in text}

print(d)

# ord() gives ASCII value.

# Output - {'a':97,'b':98,'c':99}

# I map characters to ASCII codes.



# 25 Find keys with value greater than threshold

data = {"a":10,"b":5,"c":20}

result = [k for k,v in data.items() if v > 10]

print(result)

# Filter keys using condition.

# Output - ['c']

# I iterate through items and filter.



# 26 Check if key exists safely

data = {"a":1}

print(data.get("b") is None)

# get() avoids KeyError.

# Output - True

# I check existence using get().



# 27 Build dictionary using loop

numbers = [1,2,3]

d = {}

for n in numbers:
    d[n] = n*10

print(d)

# Assign computed values.

# Output - {1:10,2:20,3:30}

# I create dictionary dynamically.



# 28 Find difference between dictionary keys

d1 = {"a":1,"b":2,"c":3}
d2 = {"b":2}

diff = d1.keys() - d2.keys()

print(diff)

# '-' finds difference.

# Output - {'a','c'}

# I compare keys using set operations.



# 29 Count words in sentence

text = "this is a test this is"

freq = {}

for word in text.split():
    freq[word] = freq.get(word,0) + 1

print(freq)

# split() separates words.

# Output - {'this':2,'is':2,'a':1,'test':1}

# I count word frequency using dictionary.



# 30 Find first non-repeating character

text = "swiss"

freq = {}

for char in text:
    freq[char] = freq.get(char,0) + 1

for char in text:
    if freq[char] == 1:
        print(char)
        break

# Frequency dictionary helps find unique character.

# Output - w

# I first count characters then find the first with frequency 1.