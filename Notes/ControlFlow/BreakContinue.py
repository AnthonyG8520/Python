# -------------break and continue Statements, and else Clauses on Loops-----------
# The break statement breaks out of the innermost enclosing 'for' or 'while' loop
# Loop statements may have an else clause;
# it is executed when the loop terminates through exhaustion of the iterable (with for)
# or when the condition becomes false (with while), but not when the loop is terminated by a break statement.
# This is exemplified by the following loop, which searches for prime numbers

for n in range(2, 10):
    print('n = ', n)
    for x in range(2, n):
        print('x = ', x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# the continue statement continues with the next iteration of the loop
for num in range(2,10):
    if num % 2 == 0:
        print('found an even number', num)
        continue
    print('found an odd number', num)

# -----------------Pass Statements----------------
# The pass statement does nothing.
# It can be used when a statement is required syntactically but the program requires no action.
    # while True:
    #     pass

# Another place pass can be used is as a place-holder
# for a function or conditional body when you are working on new code,
# allowing you to keep thinking at a more abstract level. The pass is silently ignored:
def initlog(*args):
    pass   # Remember to implement this!
























