numbers = [3, 7, 2, 9, 5, 20]

largest = numbers[0]
# Assume the first element is the largest.
for num in numbers:
# Iterate through every element
    if num > largest:
# Check if the current number is larger.
        largest = num

print(largest)


## REVERSE
numbers1 = [1, 2, 3, 4, 5]

numbers1.reverse()

print(numbers1)