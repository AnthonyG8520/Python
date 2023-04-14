# A Class is like an object constructor, or a "blueprint" for creating objects.
# In practice, the statements inside a class definition will usually be function definitions,
# but other statements are allowed, and sometimes useful — we’ll come back to this later.


class Person:
    say_hello = "Hello"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myname(self):
        return "My name is " + self.name

# Attribute references use the standard syntax used for all attribute references in
# Python: obj.name. Valid attribute names are all the names that were
# in the class’s namespace when the class object was created.


# similar to a static java method the say_hello attribute can be called
# without having to instantiate the class

print(Person.say_hello)  # This is an attribute reference - similar to calling a static java method

ant = Person('anthony', 23)  # This is an instantiation of a class

# obj = Person()  # This is also a class instantiation that is valid when no init definition is present

# the special thing about methods is that the instance object is passed as the first argument of the function
# the argument does not need to be specified because the 'self' simply calls the object
# that it is being used on therefore the next two lines of code are the same

print(ant.myname())
print(Person.myname(ant))


# Generally speaking, instance variables are for data unique to each instance
# and class variables are for attributes and methods shared by all instances of the class:
class Dog:
    # this would be a mistaken use of a class variable
    # this would provide a single shared list for all Dog objects instantiated
    # tricks = []
    # instead, you would add the empty list to the __init__ definition(constructor) of the object

    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance
        self.tricks = []  # creates a new empty list for each dog(instance variable)

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
d.add_trick('roll over')

e = Dog('Buddy')
e.add_trick('play dead')

print(d.kind)  # shared by all dogs
print(e.kind)  # shared by all dogs
print(d.name)  # unique to d
print(e.name)  # unique to e

print(d.tricks)
print(e.tricks)

# had we used a class variable instead of an instance variable
# the outcome would look like the following

# >>> d.add_trick('roll over')
# >>> e.add_trick('play dead')
# >>> d.tricks                # unexpectedly shared by all dogs
# ['roll over', 'play dead']




