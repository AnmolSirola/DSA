# 1 Create a string

text = "Hello World"

print(text)

# A string is a sequence of characters.

# Output - Hello World

# Strings are used to store textual data.



# 2 Find length of a string

text = "Python"

print(len(text))

# len() returns number of characters.

# Output - 6

# I used the built-in len() function to count characters.



# 3 Access character using index

text = "Python"

print(text[2])

# Strings use zero-based indexing.

# Output - t

# Index 2 refers to the third character.



# 4 Access last character

text = "Python"

print(text[-1])

# Negative indexing accesses characters from the end.

# Output - n

# -1 represents the last character.



# 5 Slice a string

text = "Python"

print(text[1:4])

# Slicing extracts part of the string.

# Output - yth

# Characters from index 1 to 3 are returned.



# 6 Convert string to uppercase

text = "python"

print(text.upper())

# upper() converts characters to uppercase.

# Output - PYTHON

# It returns a new uppercase string.



# 7 Convert string to lowercase

text = "PYTHON"

print(text.lower())

# lower() converts characters to lowercase.

# Output - python

# Useful for case-insensitive comparison.



# 8 Remove whitespace

text = "  hello  "

print(text.strip())

# strip() removes spaces from both ends.

# Output - hello

# Leading and trailing spaces are removed.



# 9 Replace characters

text = "hello world"

result = text.replace("world", "python")

print(result)

# replace() substitutes text.

# Output - hello python

# It replaces the specified substring.



# 10 Split string into list

text = "apple banana orange"

words = text.split()

print(words)

# split() separates words by space.

# Output - ['apple', 'banana', 'orange']

# Returns a list of substrings.



# 11 Join list into string

words = ["hello", "world"]

text = " ".join(words)

print(text)

# join() combines list elements into a string.

# Output - hello world

# Elements are joined using space.



# 12 Check if substring exists

text = "hello world"

print("world" in text)

# 'in' checks membership.

# Output - True

# It verifies if substring exists.



# 13 Find index of substring

text = "hello world"

print(text.index("world"))

# index() returns position of substring.

# Output - 6

# It finds where substring starts.



# 14 Count occurrences of substring

text = "banana"

print(text.count("a"))

# count() counts occurrences.

# Output - 3

# Character 'a' appears three times.



# 15 Check if string starts with substring

text = "python programming"

print(text.startswith("python"))

# startswith() checks prefix.

# Output - True

# Verifies starting characters.



# 16 Check if string ends with substring

text = "python programming"

print(text.endswith("programming"))

# endswith() checks suffix.

# Output - True

# Verifies ending characters.



# 17 Reverse a string

text = "python"

print(text[::-1])

# Slicing with step -1 reverses string.

# Output - nohtyp

# I reverse the string using slicing.



# 18 Convert string to list

text = "hello"

letters = list(text)

print(letters)

# list() converts characters into list.

# Output - ['h','e','l','l','o']

# Each character becomes list element.



# 19 Remove a character

text = "banana"

result = text.replace("a","")

print(result)

# replace() removes characters.

# Output - bnn

# All 'a' characters removed.



# 20 Capitalize first letter

text = "python"

print(text.capitalize())

# capitalize() makes first letter uppercase.

# Output - Python

# Only the first character becomes uppercase.



# 21 Title case string

text = "hello world"

print(text.title())

# title() capitalizes each word.

# Output - Hello World

# Useful for formatting titles.



# 22 Swap case

text = "PyThOn"

print(text.swapcase())

# swapcase() switches upper/lower case.

# Output - pYtHoN

# Upper becomes lower and vice versa.



# 23 Check if string is numeric

text = "12345"

print(text.isdigit())

# isdigit() checks numeric characters.

# Output - True

# All characters are digits.



# 24 Check if string is alphabetic

text = "Python"

print(text.isalpha())

# isalpha() checks alphabet characters.

# Output - True

# Only letters present.



# 25 Check if string is alphanumeric

text = "Python123"

print(text.isalnum())

# isalnum() checks letters and digits.

# Output - True

# Contains only letters and numbers.



# 26 Find maximum character

text = "python"

print(max(text))

# max() returns character with highest ASCII value.

# Output - y

# ASCII comparison determines result.



# 27 Find minimum character

text = "python"

print(min(text))

# min() returns smallest ASCII character.

# Output - h

# ASCII comparison determines result.



# 28 Repeat string

text = "hi"

print(text * 3)

# '*' repeats string multiple times.

# Output - hihihi

# Multiplication duplicates string.



# 29 Convert string to tuple

text = "hello"

t = tuple(text)

print(t)

# tuple() converts characters into tuple.

# Output - ('h','e','l','l','o')

# Each character becomes tuple element.



# 30 Convert string to set

text = "banana"

s = set(text)

print(s)

# set() stores unique characters.

# Output - {'b','a','n'}

# Duplicate characters are removed.