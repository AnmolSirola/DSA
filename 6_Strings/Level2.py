# 1 Reverse a string without using built-in functions

text = "python"

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)

# Build reversed string by placing characters in front.

# Output - nohtyp

# I iterate through characters and prepend each one.



# 2 Check if a string is a palindrome

text = "madam"

print(text == text[::-1])

# Compare string with its reverse.

# Output - True

# If both match, the string is a palindrome.



# 3 Count frequency of characters

text = "banana"

freq = {}

for char in text:
    freq[char] = freq.get(char,0) + 1

print(freq)

# Dictionary stores character frequencies.

# Output - {'b':1,'a':3,'n':2}

# I update counts while iterating through characters.



# 4 Find first non-repeating character

text = "swiss"

freq = {}

for char in text:
    freq[char] = freq.get(char,0) + 1

for char in text:
    if freq[char] == 1:
        print(char)
        break

# Frequency dictionary identifies unique characters.

# Output - w

# I return the first character with frequency 1.



# 5 Remove duplicate characters

text = "programming"

result = "".join(set(text))

print(result)

# set removes duplicates.

# Output - order may vary

# I convert to set and join back into string.



# 6 Count vowels in string

text = "hello world"

vowels = "aeiou"

count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)

# Check if character belongs to vowel set.

# Output - 3

# I increment count when vowel is found.



# 7 Count consonants in string

text = "hello"

vowels = "aeiou"

count = 0

for char in text:
    if char.isalpha() and char not in vowels:
        count += 1

print(count)

# Count alphabetic characters excluding vowels.

# Output - 3

# h,l,l are consonants.



# 8 Find longest word in sentence

text = "Python is very powerful"

words = text.split()

longest = max(words, key=len)

print(longest)

# max with key=len finds longest word.

# Output - powerful

# I compare word lengths.



# 9 Find shortest word in sentence

text = "Python is very powerful"

words = text.split()

shortest = min(words, key=len)

print(shortest)

# min with key=len finds shortest word.

# Output - is

# Word with minimum length returned.



# 10 Count number of words

text = "Python is easy to learn"

words = text.split()

print(len(words))

# split separates words.

# Output - 5

# I count number of words in the list.



# 11 Check if two strings are anagrams

s1 = "listen"
s2 = "silent"

print(sorted(s1) == sorted(s2))

# Sorted strings match for anagrams.

# Output - True

# Anagrams contain same letters.



# 12 Remove spaces from string

text = "hello world"

result = text.replace(" ","")

print(result)

# replace removes spaces.

# Output - helloworld

# All spaces removed.



# 13 Count uppercase letters

text = "PyThOn"

count = 0

for char in text:
    if char.isupper():
        count += 1

print(count)

# isupper checks uppercase letters.

# Output - 3

# P,T,O are uppercase.



# 14 Count lowercase letters

text = "PyThOn"

count = 0

for char in text:
    if char.islower():
        count += 1

print(count)

# islower checks lowercase letters.

# Output - 3

# y,h,n are lowercase.



# 15 Remove punctuation

import string

text = "hello, world!"

result = ""

for char in text:
    if char not in string.punctuation:
        result += char

print(result)

# Remove punctuation characters.

# Output - hello world

# I filter punctuation marks.



# 16 Replace vowels with '*'

text = "hello"

vowels = "aeiou"

result = ""

for char in text:
    if char in vowels:
        result += "*"
    else:
        result += char

print(result)

# Replace vowels with symbol.

# Output - h*ll*

# I check each character.



# 17 Find most frequent character

text = "banana"

freq = {}

for char in text:
    freq[char] = freq.get(char,0) + 1

most = max(freq, key=freq.get)

print(most)

# max finds highest frequency.

# Output - a

# 'a' occurs most.



# 18 Check if string contains digits

text = "python123"

print(any(char.isdigit() for char in text))

# any returns True if digit exists.

# Output - True

# Checks characters for digits.



# 19 Remove digits from string

text = "pyth0n123"

result = ""

for char in text:
    if not char.isdigit():
        result += char

print(result)

# Filter characters that are not digits.

# Output - pythn

# I remove numbers from string.



# 20 Find second most frequent character

text = "banana"

freq = {}

for char in text:
    freq[char] = freq.get(char,0) + 1

sorted_chars = sorted(freq, key=freq.get, reverse=True)

print(sorted_chars[1])

# Sort characters by frequency.

# Output - n

# 'n' is second most frequent.



# 21 Reverse words in sentence

text = "hello world python"

words = text.split()

reversed_words = words[::-1]

print(" ".join(reversed_words))

# Reverse word order.

# Output - python world hello

# I reverse the list of words.



# 22 Find duplicate characters

text = "programming"

duplicates = set()

seen = set()

for char in text:
    if char in seen:
        duplicates.add(char)
    else:
        seen.add(char)

print(duplicates)

# Track seen characters.

# Output - {'r','g','m'}

# Characters appearing more than once.



# 23 Check if string is numeric

text = "12345"

print(text.isdigit())

# isdigit checks numeric characters.

# Output - True

# All characters are digits.



# 24 Convert characters to ASCII values

text = "abc"

ascii_values = [ord(c) for c in text]

print(ascii_values)

# ord converts character to ASCII.

# Output - [97,98,99]

# ASCII values returned.



# 25 Convert ASCII to characters

values = [97,98,99]

chars = [chr(v) for v in values]

print(chars)

# chr converts ASCII to character.

# Output - ['a','b','c']

# ASCII codes mapped to characters.



# 26 Find common characters in two strings

s1 = "hello"
s2 = "world"

common = set(s1) & set(s2)

print(common)

# Intersection finds shared characters.

# Output - {'o','l'}

# Convert strings to sets.



# 27 Count occurrences of substring

text = "ababab"

print(text.count("ab"))

# count finds substring occurrences.

# Output - 3

# 'ab' appears three times.



# 28 Check if string starts and ends with same letter

text = "level"

print(text[0] == text[-1])

# Compare first and last characters.

# Output - True

# Both characters match.



# 29 Convert sentence to title case manually

text = "python programming language"

words = text.split()

result = ""

for word in words:
    result += word.capitalize() + " "

print(result.strip())

# Capitalize each word.

# Output - Python Programming Language

# I capitalize words individually.



# 30 Remove repeated consecutive characters

text = "aaabbccdaa"

result = text[0]

for char in text[1:]:
    if char != result[-1]:
        result += char

print(result)

# Skip repeated adjacent characters.

# Output - abcda

# Only unique consecutive characters kept.



# 31 Find longest substring without repeating characters (simple approach)

text = "abcabcbb"

unique = set(text)

print(len(unique))

# Count unique characters.

# Output - 3

# Unique characters are a,b,c.



# 32 Count spaces in string

text = "hello world python"

print(text.count(" "))

# count finds spaces.

# Output - 2

# Two spaces exist.



# 33 Extract digits from string

text = "a1b2c3"

digits = ""

for char in text:
    if char.isdigit():
        digits += char

print(digits)

# Extract numeric characters.

# Output - 123

# Only digits retained.



# 34 Remove vowels from string

text = "hello world"

vowels = "aeiou"

result = ""

for char in text:
    if char not in vowels:
        result += char

print(result)

# Filter vowels.

# Output - hll wrld

# Only consonants remain.



# 35 Find index of first vowel

text = "python"

vowels = "aeiou"

for i,char in enumerate(text):
    if char in vowels:
        print(i)
        break

# enumerate gives index and character.

# Output - 4

# 'o' is first vowel.



# 36 Check if all characters are unique

text = "abcde"

print(len(text) == len(set(text)))

# Compare length with set length.

# Output - True

# No duplicates exist.



# 37 Count number of digits

text = "abc123"

count = 0

for char in text:
    if char.isdigit():
        count += 1

print(count)

# Count digit characters.

# Output - 3

# Three digits exist.



# 38 Reverse each word in sentence

text = "hello world"

words = text.split()

result = " ".join(word[::-1] for word in words)

print(result)

# Reverse each word individually.

# Output - olleh dlrow

# Words remain in same order.



# 39 Find length of longest word

text = "Python programming is powerful"

words = text.split()

print(len(max(words, key=len)))

# max with key=len finds longest word.

# Output - 11

# 'programming' length returned.



# 40 Remove duplicate words in sentence

text = "this is is a test test"

words = text.split()

unique = list(set(words))

print(" ".join(unique))

# Convert words to set.

# Output - order may vary

# Duplicate words removed.