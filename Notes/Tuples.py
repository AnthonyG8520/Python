# -------------------------Tuples-----------------
# tuples are ordered and immutable
# empty tuples are constructed by an empty pair of parentheses
# a tuple with only one item is constructed by following a value with a comma
# it is not sufficient to enclose a single value in parentheses

empty = ()
single = (4,)
nums = (4, 5, 6)

# to access an element in a tuple use []
# use negative indexes to start from end

print(nums[2])
print(nums[-1])

# you can also use a range of indexes like in lists

print(nums[1:-2])

# tuples are immutable but if you want to change the elements
# there is a workaround - convert to list - change elements - convert to tuple

nums_list = list(nums)
nums_list[0] = 3
nums = tuple(nums_list)

print(nums)

# ---------tuple unpacking----------
# we can use unpacking to multi assign variables
# there must be as many assignment variable as there are elements

fourth, fifth, sixth = nums

print(fourth)
print(fifth)
print(sixth)

# if the number of variables is less than the number of elements
# you can add an * to the variable and the remaining values
# will be assigned to the variable as a list

letters = ('a', 'b', 'c', 'd', 'e')

a, b, c, *remaining = letters

print(a)
print(b)
print(c)
print(remaining)

# if the * is added to a variable other than the last
# python will assign to that lust until the number of
# elements left matches the number of variables left

a, *many, e = letters
print(a)
print(many)
print(e)








