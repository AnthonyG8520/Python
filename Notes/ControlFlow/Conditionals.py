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

# ------------------Match Statements--------------------
# A match statement takes an expression and compares its value to successive patterns given as one or more case blocks
# similar to switch case statement

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
# Note the last block: the “variable name” _ acts as a wildcard and
# never fails to match. If no case matches, none of the branches is executed.


print(http_error(404))


# you can combine literals is a single case statement using a single pipe '|' known as "or"
# case 401 | 403 | 404:
#     return "not allowed"




