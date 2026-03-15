list1 = [1, 2, 3]
list2 = [4, 5, 6]

## output [5, 7, 9]


#Pairs elements by index:
#(1, 4), (2, 5), (3, 6)

result = [a + b for a, b in zip(list1, list2)]
 
print(result)

# result = []
# for i in range(len(list1)):
#     result.append(list1[i] + list2[i])


## MERGING TWO LISTS
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)

#Find Avg of list
numbers = [2,4,6,8]

average = sum(numbers) / len(numbers)

print(average)

#Count even numbers of list
numbers = [1,2,3,4,5,6]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(count)
#3

#List to string
words = ["hello","world"]

result = " ".join(words)

print(result)
# hello world

#String to list
text = "hello"

letters = list(text)

print(letters)

#Output ['h','e','l','l','o']

#Remove all occurrences of an element
numbers = [1,2,2,3,2,4]

numbers = [x for x in numbers if x != 2]

print(numbers)
#Output [1,3,4]