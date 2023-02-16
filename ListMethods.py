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












