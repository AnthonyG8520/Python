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










