# ----------------------Dictionaries----------------
# dictionaries are used to store data values in key:value pairs
# a dictionary is a collection which is ordered, changeable and does not allow duplicates
# similar to java hashmaps
# indexed by keys of any immutable type : strings, numbers, or tuples
# (if a tuple contains any mutable object it cannot be used as a key)

# a pair of braces creates an empty dictionary
empty_dict = {}

# placing a comma seperated list of key:value pairs within the braces adds initial values
new_dict = {'name': 'Anthony', 'age': 23}
print(new_dict)

# it's possible to delete a pair with the del statement
del(new_dict['name'])
print(new_dict)

# if you store using a key that is already in use
# the old value associated with that key is forgotten
new_dict['age'] = 25
print(new_dict.get('age'))

# attempting to extract a value using a non-existent key
# will result in an error
print(new_dict.get('name'))
# returns none

# -------------adding items to dictionary---------------
new_dict['name'] = 'Anthony'
new_dict.update({'fav-color': 'blue'})
print(new_dict)


# -------------accessing dictionary values--------------------
# you can access items of a dictionary by referring to its key name
# in square brackets or by using the get() method on a dictionary

print(new_dict['name'])
print(new_dict.get('name'))

# the keys method will return all the keys in the dictionary
print(new_dict.keys())

# ------------changing values---------------
# you can use the square bracket method or use the update() method

new_dict['fav-color'] = 'red'
new_dict.update({'fav-color': 'red'})
print(new_dict)

# ----------------removing items---------------------

# the pop() method removes the item with the specified key name

new_dict.pop('fav-color')
print(new_dict)

# it's possible to delete a pair with the del statement
del(new_dict['name'])
print(new_dict)

# the clear() method empties the dictionary

new_dict.clear()
print(new_dict)
# ----------------------------

# you can check if a single key is in the dictionary using the in keyword
print('name' in new_dict)

# you can build dictionaries using the dict() constructor directly from sequences of key:val pairs

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))







