# ------------------Functions---------------------
# for some reason function definitions and calls should have 2 empty line above and below
# The keyword def introduces a function definition.
# It must be followed by the function name and the parenthesized list of formal parameters.
def greeting(name):
    return "Hello " + name


def sayhello():
    return "Hello"


print(sayhello())
print(greeting("Anthony"))

# It is also possible to define functions with a variable number of arguments.
# There are three forms, which can be combined.

# The most useful form is to specify a default value for one or more arguments.
# This creates a function that can be called with fewer arguments than it is defined to allow


def hello_there(name=""):
    if name != "":
        return "Hello " + name
    else:
        return "hello"


print(hello_there())
print(hello_there("Antohny"))

# We can create a function that writes the fibonacci series to a certain boundary
# The first statement of the function body can optionally be a string literal;
# this string literal is the function’s documentation string, or docstring.

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(2000)




















