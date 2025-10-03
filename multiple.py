"""
Multiple inheritance is when one class inherits from multiple classes and is able to use attributes and methods from both classes.
There are pros and cons to using multiple inheritance.
Pros include the ability to reuse small amounts of code in multiple classes and mix-ins.
Cons include the order of inheritance matters. Inheriting from multiple classes can become quite complicated depending on the number of classes, the names of class methods and other factors, including common attributes shared among multiple parent classes.
There can be more maintenance involved when refactoring code that is using multiple inheritance.
"""
#2 ways to do multiple inheritance in Python: The super() methodIn a child class, super() is a
# function that provides a proxy object, allowing you to
# access methods of the parent or "next" class in the MRO.
#The MRO is the order in which Python searches for a method or
# attribute in a class hierarchy. Python uses an algorithm called C3 linearization
# to create a predictable MRO that respects two main rules:

# Parent class 1
class Item():

    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

# Parent class 2
class Garment():

    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.type))

# First, we'll define the attributes that are specific to the child's class.
#
# Now, we'll initialize the attributes from parent class 1, the Item class.
#
# Next, we'll initialize the attributes from parent class 2, the Garment class.

# Child Class
class Shirts(Item, Garment):

    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color

        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))
        Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

        Blouse.print_sku()
        Blouse.print_garment()
        Blouse.print_shirt()