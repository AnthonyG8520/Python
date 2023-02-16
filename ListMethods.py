fruits = ['apple', 'banana', 'orange', 'mango', 'watermelon']


# adds an element at the end of a list
fruits.append('strawberry')
print(fruits)

# returns the number of elements with the specified value in the list
print(fruits.count('apple'))

# returns the index of the first element with the specified value
print(fruits.index('mango'))

# adds an element at the specified position
fruits.insert(1, 'peach')
print(fruits)

# removes the element at a specified position but default is the last item
fruits.pop()
print(fruits)

# in addition to pop() there is popleft() which will remove an element from the front of the list
# however you need to import the collection.deque package and use different syntax for list
# this method is not efficient due to speed
    # from collections import deque
    # queue = deque(["Eric", "John", "Michael"])
    # queue.popleft()

# removes the first item with the specified value
fruits.remove('orange')
print(fruits)

# reverses the order of the list
fruits.reverse()
print(fruits)

# add the elements of a list or any iterable to the end of current list
more_fruits = ['strawberry', 'peach']
fruits.extend(more_fruits)
print(fruits)

# removes all the elements from the list
fruits.clear()
print(fruits)

# --------------------List Comprehension---------------------
# List comprehensions provide a concise way to create lists.
# Common applications are to make new lists where each element is the result of some operations
# applied to each member of another sequence or iterable, or to create a subsequence
# of those elements that satisfy a certain condition.

squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# instead we could use
squares = [x**2 for x in range(10)]
print(squares)

# list comprehension can contain multiple for clauses as well as if clauses

combs = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)

# instead we could use
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)
# If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.

# we could use list comprehension to quickly double all the numbers in a list
nums = [-4, -2, 0, 2, 4]
doubled = [x*2 for x in nums]
print(doubled)

# we could even use it to filter out certain values
positives = [x for x in nums if x >= 0]
print(positives)

# also used for running methods on each element
vegetables = ['   carrot  ', '    brocolli   ']

vegetables = [vegetable.strip() for vegetable in vegetables]
print(vegetables)







