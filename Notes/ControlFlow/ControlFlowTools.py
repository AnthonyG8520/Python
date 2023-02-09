# -----------------While loop example----------------
# The body of the loop is indented, indentation is pythons way of grouping statements

a = 0
while a <= 5:
    print(a)
    a += 1

# -------------if statements-------------

# the input keyword shown is used to take input from the console
# x = int(input('Please input a number:'))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Your number was zero')
# elif x == 1:
#     print('Your number was one')
# else:
#     print('Your number was: ' + str(x))

# ----------------for statements--------------
# the for statement is used for iterating over things like lists and other collections
# - similar to java's enhanced forEach loop

words = ['cat', 'window', 'defenstrate']
for w in words:
    print(w, 'The word is ' + str(len(w)) + ' characters long')

# Code that modifies a collection while iterating over that same collection can be tricky to get right.
# Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection

# the values shown in this collection are known as a dictionary and are used to map one value to another
# - similar to java's hashmaps
users = {'Hans': 'active', 'Ant': 'inactive', 'Meee': 'active'}

# iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

# create a new collection
activeUsers = {}
for user, status in users.items():
    if status == 'active':
        # below are two ways to add key value pairs to a dictionary
        # activeUsers[user] = status
        activeUsers.update({user: status})

print(activeUsers)

# -----------The range() function--------------
# If you do need to iterate over a sequence of numbers,
# the built-in function range() comes in handy. It generates arithmetic progressions

for i in range(5):
    print(i)

# The given end point is never part of the generated sequence;
# range(10) generates 10 values, the legal indices for items of a sequence of length 10.
for x in range(5, 10):
    print(x)

# It is possible to let the range start at another number,
# or to specify a different increment (even negative; sometimes this is called the ‘step’):
for y in range(0, 10, 3):
    print(y)

# To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
# In most such cases, however, it is convenient to use the enumerate() function










