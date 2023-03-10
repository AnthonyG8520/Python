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


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# This function can be called in several ways:
# This example also introduces the in keyword. This tests whether or not a sequence contains a certain value.

# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


# Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# accepts one required argument (voltage) and three optional arguments (state, action, and type).
# This function can be called in any of the following ways


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# but all the following calls would be invalid:

# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument keyword arguments must follow positional arguments
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


# By default, arguments may be passed to a Python function either by position or explicitly by keyword.
# For readability and performance, it makes sense to restrict the way arguments
# can be passed so that a developer need only look at the function definition
# to determine if items are passed by position, by position or keyword, or by keyword.
# If / and * are not present in the function definition,
# arguments may be passed to a function by position or by keyword.

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#     -----------    ----------     ----------
#     |             |                  |
#     |        Positional or keyword   |
#     |                                - Keyword only
#     -- Positional only

# ----------Positional only parameters-------------

# it is possible to mark certain parameters as positional-only.
# If positional-only, the parameters’ order matters,
# and the parameters cannot be passed by keyword. Positional-only parameters are placed before a / (forward-slash)

# ------------keyword only arguments--------------------
# To mark parameters as keyword-only, indicating the
# parameters must be passed by keyword argument, place an * in the arguments
# list just before the first keyword-only parameter.

def standard_arg(arg):
    print(arg)  # will work as positional or keyword


def pos_only_arg(arg, /):
    print(arg)  # restricted to positional only


def kwd_only_arg(*, arg):
    print(arg)  # restricted to keyword only


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg(2)
standard_arg(arg=2)

pos_only_arg(1)
# pos_only_arg(arg=1)  # will result in error - can only call arg positionally

# kwd_only_arg(1)  # will result in error - can only call arg by keyword
kwd_only_arg(arg=1)

# combined_example(1, 2, 3)  # will error due to third keyword only argument being called without keyword
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)  # will work since second argument does not have a restriction
# combined_example(pos_only=1, standard=2, kwd_only=3)  # will error for first positionally only argument being called by keyword


# -------------------unpacking list arguments--------------------

# The reverse situation occurs when the arguments are already in a list or tuple
# but need to be unpacked for a function call requiring separate positional arguments.
# For instance, the built-in range() function expects separate start and stop arguments.
# If they are not available separately, write the function call
# with the *-operator to unpack the arguments out of a list or tuple:


list(range(3, 6))  # normal call with separate arguments
# above call will print -> [3, 4, 5]

args = [3, 6]
list(range(*args))  # call with arguments unpacked from a list
# above call also prints this [3, 4, 5]

# list(range(args))  # this will result in an error because the list isnt being unpacked before the range function is called


# In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


# when using a dictionary the arguments are input by keyword so the order of the arguments in the dictionary dont matter
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
d = {"state": "bleedin' demised", "voltage": "four million", "action": "VOOM"}

parrot(**d)
# --result -> This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

# -----------------lambda functions---------------------
# Small anonymous functions can be created with the lambda keyword.
# Lambda functions can be used wherever function objects are required.
# They are syntactically restricted to a single expression.


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(1))
print(make_incrementor(42)(1))
# 43
# the function works either way shown and return the same result

# ---------------------function annotations-----------------
# Annotations are stored in the __annotations__ attribute of the function as a dictionary
# and have no effect on any other part of the function.
# Parameter annotations are defined by a colon after the parameter name,
# followed by an expression evaluating to the value of the annotation.
# Return annotations are defined by a literal ->, followed by an expression,
# between the parameter list and the colon denoting the end of the def statement.


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')

# result below:
# Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
# Arguments: spam eggs
# 'spam and eggs'








