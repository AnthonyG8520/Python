# ----------Formatted String Literals--------------
# Formatted string literals (also called f-strings for short) let you include the
# value of python expressions inside a string by prefixing the string with
# f or F and writing expressions inside curly brackets as {expression}

num = 27
print(f'The value of num is {num}.')

# passing an integer after the ':' will cause that field to be a minimum
# number of characters wide
# This is useful for making columns line up

table = {'Ant': 4127, 'Anthony': 4098, 'Tony': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# the = specifier can be used to expand an expression to the text of the expression
# an equal sign, then the representation of the evaluated expression

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging --> {bugs=} {count=} {area=}')

# ---------------The String format() Method--------------
# basic usage of the str.format() looks like this
# the brackets and characters withing them (called format fields)
# are replaced with the objects passed into the str.format() method
print('We are the {} who say "{}"!'.format('knights', 'Ni'))

# a number in the brackets can be used to refer to the position
# of the object passed in the format() method
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# --------------reading and writing files------------
# open() return a file object, and is most commonly used with 2 positional
# arguments and one keyword argument: open(filename, mode, encoding)

# Warning: Calling f.write() without using the with keyword or calling f.close()
# might result in the arguments of f.write()
# not being completely written to the disk, even if the program exits successfully.

f = open('IO/test.txt', 'r')
f.close()

# the first argument is a string containing the filename
# the second argument is another string containing a few characters
# describing the way the file will be used mode can be
# 'r' when the file will only be read
# 'w' for only writing (an existing file with the same name will be erased)
# 'a' opens the file for appending - any data written to the file is
# automatically added to the end
# 'r+' opens the file for reading and writing

# the third argument is the encoding - some files need a specific encoding
# if no encoding is specified UTF-8 is used since it is most common

# it's good practice to use the 'with' keyword when dealing with file objects
# the advantage is that the file is properly closed after its suite is finished
# even if an exception is raised at some point

words = ['bonk', 'bee', 'bug', 'wood']

f = open('IO/test.txt', 'a')
for w in words:
    f.write('\n' + w)
f.close()

with open('IO/test.txt', 'r') as f:
    print(f.read())

# ---------------Methods of File Objects-------------
# to read a files contents, call f.read(size)
# the optional size argument is the amount of characters read if in text mode
# or the amount of bytes read if in binary mode
# if no argument is entered then the entire file will be read

# f.readline() reads a single line from the file
# however you can loop over the lines and work with them that way

with open('IO/test.txt', 'r') as f:
    f.readline()
    for line in f:
        print(line)

# if you want to read all the lines from a file
# you can use f.readlines()

with open('IO/test.txt', 'r') as f:
    print(f.readlines())






