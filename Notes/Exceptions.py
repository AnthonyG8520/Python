# ----------------Handling Exceptions-----------------
# It is possible to write programs that handle selected exceptions

while True:
    try:
        x = int(input("Please enter a valid number: "))
        break
    except ValueError:
        print("Number not valid. Try again...")

# The try statement works as follows:
# first the try clause (the statement between the try and except keywords) is executed
# if no exception occurs, the except clause is skipped and execution of the try statement is finished
# if an exception occurs during the execution of the try clause, the rest of the clause is skipped
# then if it's type matches the exception named after the except keyword, the except clause is executed
# then execution continues after the try except block
# if an exception occurs which does not match the exception named in the except clause
# it is passed on to outer try statements; if no handler is found, it's an unhandled exception
# and execution stops with a message shown

# A try statement may have more than one except clause, to specify handlers for different exceptions
# At most one handler will be executed. Handlers only handle exceptions that occur in the
# corresponding try clause, not in other handlers of the same try statement
# An except clause may name multiple exceptions as a parenthesized tuple, for example:

except (RuntimeError, TypeError, NameError)

# ---------------------Raising Exceptions---------------------------
# the raise statement allows the programmer to force a specified exception to occur

# For example:
raise NameError('Wrong name')

# shorthand for 'raise ValueError()'
raise ValueError

# If you need to determine whether an exception was raised but don’t intend to handle it,
# a simpler form of the raise statement allows you to re-raise the exception:

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by')
    raise

# ---------------- Defining Clean-Up Actions ---------------------------

# The try statement has another optional clause which is intended to
# define clean-up actions that must be executed under all circumstances.
# For example:

try:
    raise KeyboardInterrupt
finally:
    print("Goodbye, World")

# If the finally clause executes a break, continue or return statement, exceptions are not re-raised.
while True:
    try:
        raise KeyboardInterrupt
    finally:
        print("Goodbye, World")
        break

# If the try statement reaches a break, continue or return statement,
# the finally clause will execute just prior to the break, continue or return statement’s execution.

while True:
    try:
        raise KeyboardInterrupt
        break
    finally:
        print("Goodbye, World")

# Another simple example of how the finally statement is executed

def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())

