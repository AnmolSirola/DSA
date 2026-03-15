#Multiply a list
numbers = [1, 2, 3]

result = numbers * 3

print(result)

#Output - [1,2,3,1,2,3,1,2,3]

#Multipy each element
numbers = [1, 2, 3]

result = [n * 3 for n in numbers]

print(result)  # [3, 6, 9]


numbers = [1, 2, 3]
result = []

for n in numbers:
    result.append(n * 3)

print(result)  # [3, 6, 9]