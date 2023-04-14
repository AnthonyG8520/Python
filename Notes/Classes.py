# A Class is like an object constructor, or a "blueprint" for creating objects.
# In practice, the statements inside a class definition will usually be function definitions,
# but other statements are allowed, and sometimes useful — we’ll come back to this later.


class Person:
    say_hello = "Hello"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Attribute references use the standard syntax used for all attribute references in
# Python: obj.name. Valid attribute names are all the names that were
# in the class’s namespace when the class object was created.


print(Person.say_hello)  # This is an attribute reference

ant = Person('anthony', 23)  # This is an instantiation of a class

# obj = Person()  # This is also a class instantiation that is valid when no init definition is present

