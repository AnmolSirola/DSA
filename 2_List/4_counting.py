
# Count occurrences of an element
numbers = [1,2,3,2,4,2,5]

counting = numbers.count(2)

print(counting)


# Find the length of a list
numbers = [1, 2, 3, 4, 5]

length = len(numbers)

print(length)

# Add an element to the end of a list
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)

#Insert an element at a specific index
numbers = [1, 2, 4]

numbers.insert(2, 3)

print(numbers)

#Remove an element by value
numbers = [1, 2, 3, 4]

numbers.remove(3)

print(numbers)

#Remove the last element
numbers = [1, 2, 3, 4]

numbers.pop()

print(numbers)

#Remove an element using index
numbers = [10, 20, 30, 40]

numbers.pop(1)

print(numbers)

#Find index of an element
numbers = [10, 20, 30, 40]

index = numbers.index(30)

print(index)


#Find the minimum and maximum element in a list

numbers = [5, 2, 9, 1, 7]

minimum = min(numbers)
maximum = max(numbers)

print(minimum)