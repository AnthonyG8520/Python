# A Class is like an object constructor, or a "blueprint" for creating objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ant = Person('anthony', 23)

print('My name is ' + ant.name + ' and I\'m ' + str(ant.age))
