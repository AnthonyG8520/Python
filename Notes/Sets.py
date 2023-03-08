# ------------------------Sets------------------------
# sets are used to store multiple items in a single variable
# set items are unchangeable, but you can remove and add new items
# sets are unchangeable, unordered, and unindexed

# curly braces or the set() function can be used to create sets
# to create an empty set you have to use set() not {} (this will create an empty dictionary)


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # shows duplicated being removed when printing

print('orange' in basket)  # fast membership testing

print('crabgrass' in basket)

# using the set function will iterate over the input argument and separate it as single elements
words = set(('hello', 'there'))
print(words)

a = set('abracadabra')
print(a)
b = set('alacazam')
print(b)

# demonstrate set operations on unique letters from two words

print(a-b)  # letters in a but not in b

print(a | b)  # letters in a or b or both

print(a & b)  # letters in both a and b

print(a ^ b)  # letters in a or b but not both

# similar to list comprehension, set comprehension is supported as well

d = {x for x in 'hello' if x not in 'l'}
print(d)











