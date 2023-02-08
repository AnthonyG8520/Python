# ------------------Numbers----------------

# python contains numbers and floats as opposed to javascript where every number is a number

add = 2 + 2
print(add)

subtract = 50 - 10
print(subtract)

multiply = 5 * 5
print(multiply)

# with python it is possible to use the ** operator to calculate powers
toPower = 5 ** 2
print(toPower)

# division will always return a floating point - use // to floor the number returned from division
divide = 10 / 4
print(divide)

floorDivide = 10 // 4
print(floorDivide)

remainder = 3 % 2
print(remainder)

# ------------------Strings--------------------

# strings can be expressed with single or double quotes and can use \ to escape quotes
breakfast = 'spam eggs'

#example escaping quote - could use double quote instea
string = 'doesn\'t' + "doesn't"

# \n means new line
twoLines = 'First line\nSecond line'
print(twoLines)

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
concat = 'un' + 'ium'
print(concat)

repeat = 3 * 'cheeseburger\n'
print(repeat)

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
# This only works with two literals though, not with variables or expressions
print('Py' 'thon')

# This feature is particularly useful when you want to break long strings:
print('hello'
      'there')

#Strings can be indexed (subscripted), with the first character having index 0.
# There is no separate character type; a character is simply a string of size one
# Indices may also be negative numbers, to start counting from the right:
word = 'Python'
print(word[4])
print(word[-1])

# In addition to indexing, slicing is also supported.
# While indexing is used to obtain individual characters, slicing allows you to obtain substring
print(word[0:3])

# Slice indices have useful defaults;
# an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
print(word[:3])
print(word[3:])
print(word[-2:])

# built in function len() returns the length of a string
print(len(word))

# -----------------------Lists------------------------
# Python knows a number of compound data types, used to group together other values.
# The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets.
# Lists might contain items of different types, but usually the items all have the same type.
squares = [1, 4, 9, 16, 25]
print(squares)

# Like strings (and all other built-in sequence types), lists can be indexed and sliced
print(squares[0])
print(squares[-1])
print(squares[2:])

# Lists also support operations like concatenation
newSquaresList = squares + [36, 49]
print(newSquaresList)

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)

# You can also add new items at the end of the list, by using the append() method
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)
# The built-in function len() also applies to lists
listOfNums = [1, 3, 5, 7]
print(len(listOfNums))





