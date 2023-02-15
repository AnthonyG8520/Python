# common useful string methods in python

string = "    hello from outer space    "

print(string.capitalize())
# converts the first character to upper case

print(string.count("o"))
# returns the number of times a specified value occurs in a string

print(string.endswith("e"))
# returns if the string ends with a specified value

print(string.index("o"))  # could also use .find()
# searches the string for a specified value and returns the position of where it was found

print(string.isalpha())
# returns True if all characters in the string are in the alphabet

print(string.lower())
# converts a string to lowercase

print(string.upper())
# converts a string to uppercase

print(string.swapcase())
# swaps cases - lowercase becomes uppercase and upper becomes lower

print(string.replace(" ", ""))
# use replace to get rid of white space or remove / replace other characters

print(string.strip())
# removes leading and trailing whitespace in a string - can strip certain values - whitespace being the default

print(string.split())
# this will split the string into a list separating by
# whitespace at default and can input other separators
# but will not split all single characters into list

# to split all characters into a list separately we can use unpack(*) method
char_list = [*string.replace(" ", "")]
print(char_list)








