# 1 Create a dictionary

person = {"name": "Anmol", "age": 22, "city": "Delhi"}

print(person)

# A dictionary stores data as key-value pairs.

# Output - {'name': 'Anmol', 'age': 22, 'city': 'Delhi'}

# A dictionary allows storing related data using keys and values.



# 2 Access value using key

person = {"name": "Anmol", "age": 22}

print(person["name"])

# We access dictionary values using their keys.

# Output - Anmol

# I accessed the value associated with the key "name".



# 3 Access value using get()

person = {"name": "Anmol", "age": 22}

print(person.get("age"))

# get() retrieves the value of a key safely.

# Output - 22

# get() returns the value of the key without raising an error if it does not exist.



# 4 Add a new key-value pair

person = {"name": "Anmol", "age": 22}

person["city"] = "Delhi"

print(person)

# Assigning a value to a new key adds it to the dictionary.

# Output - {'name': 'Anmol', 'age': 22, 'city': 'Delhi'}

# I added a new key-value pair to the dictionary.



# 5 Update a value

person = {"name": "Anmol", "age": 22}

person["age"] = 23

print(person)

# Assigning a new value to an existing key updates it.

# Output - {'name': 'Anmol', 'age': 23}

# I updated the value associated with the key "age".



# 6 Remove a key-value pair using pop()

person = {"name": "Anmol", "age": 22}

person.pop("age")

print(person)

# pop() removes a key and returns its value.

# Output - {'name': 'Anmol'}

# pop() removes the specified key from the dictionary.



# 7 Remove last inserted item

person = {"name": "Anmol", "age": 22, "city": "Delhi"}

person.popitem()

print(person)

# popitem() removes the last inserted key-value pair.

# Output - {'name': 'Anmol', 'age': 22}

# popitem() removes items in LIFO order.



# 8 Check if a key exists

person = {"name": "Anmol", "age": 22}

print("name" in person)

# The 'in' operator checks if a key exists.

# Output - True

# I used the membership operator to check if the key exists.



# 9 Get all keys

person = {"name": "Anmol", "age": 22}

print(person.keys())

# keys() returns all keys in the dictionary.

# Output - dict_keys(['name', 'age'])

# keys() allows us to view all dictionary keys.



# 10 Get all values

person = {"name": "Anmol", "age": 22}

print(person.values())

# values() returns all values in the dictionary.

# Output - dict_values(['Anmol', 22])

# values() retrieves all stored values.



# 11 Get all key-value pairs

person = {"name": "Anmol", "age": 22}

print(person.items())

# items() returns key-value pairs as tuples.

# Output - dict_items([('name', 'Anmol'), ('age', 22)])

# items() is useful for iterating through keys and values.



# 12 Iterate through keys

person = {"name": "Anmol", "age": 22}

for key in person:
    print(key)

# Looping over a dictionary iterates through keys.

# Output - name age

# A dictionary loop returns keys by default.



# 13 Iterate through values

person = {"name": "Anmol", "age": 22}

for value in person.values():
    print(value)

# values() allows iteration over values.

# Output - Anmol 22

# I used values() to iterate through all values.



# 14 Iterate through key-value pairs

person = {"name": "Anmol", "age": 22}

for key, value in person.items():
    print(key, value)

# items() returns key-value pairs for iteration.

# Output - name Anmol / age 22

# items() allows unpacking key and value in loops.



# 15 Find length of dictionary

person = {"name": "Anmol", "age": 22}

print(len(person))

# len() returns the number of key-value pairs.

# Output - 2

# len() counts the number of entries in the dictionary.



# 16 Clear a dictionary

person = {"name": "Anmol", "age": 22}

person.clear()

print(person)

# clear() removes all elements.

# Output - {}

# clear() empties the dictionary.



# 17 Copy a dictionary

person = {"name": "Anmol", "age": 22}

person_copy = person.copy()

print(person_copy)

# copy() creates a new dictionary.

# Output - {'name': 'Anmol', 'age': 22}

# copy() prevents modifications affecting the original dictionary.



# 18 Create dictionary using dict()

person = dict(name="Anmol", age=22)

print(person)

# dict() is another way to create dictionaries.

# Output - {'name': 'Anmol', 'age': 22}

# dict() constructs a dictionary using keyword arguments.



# 19 Get value with default

person = {"name": "Anmol"}

print(person.get("age", "Not Found"))

# get() allows setting a default value.

# Output - Not Found

# If the key does not exist, get() returns the default value.



# 20 Update dictionary

person = {"name": "Anmol"}

person.update({"age": 22})

print(person)

# update() merges another dictionary.

# Output - {'name': 'Anmol', 'age': 22}

# update() adds or modifies key-value pairs.



# 21 Create dictionary from two lists

keys = ["name", "age"]
values = ["Anmol", 22]

person = dict(zip(keys, values))

print(person)

# zip() combines keys and values.

# Output - {'name': 'Anmol', 'age': 22}

# zip() pairs elements to form dictionary entries.



# 22 Check if dictionary is empty

person = {}

if not person:
    print("Dictionary is empty")

# An empty dictionary evaluates to False.

# Output - Dictionary is empty

# I check emptiness using a boolean condition.



# 23 Access nested dictionary

person = {"user": {"name": "Anmol", "age": 22}}

print(person["user"]["name"])

# Nested dictionaries store dictionaries inside dictionaries.

# Output - Anmol

# I accessed the nested key by chaining keys.



# 24 Convert dictionary keys to list

person = {"name": "Anmol", "age": 22}

keys = list(person.keys())

print(keys)

# list() converts dict_keys into a list.

# Output - ['name', 'age']

# I converted the dictionary keys into a list.



# 25 Convert dictionary values to list

person = {"name": "Anmol", "age": 22}

values = list(person.values())

print(values)

# list() converts dict_values into a list.

# Output - ['Anmol', 22]

# I converted dictionary values into a list.