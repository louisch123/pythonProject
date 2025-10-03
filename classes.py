#Class - Groping data and information like variables and functions into a single
# organized unit. Defines a new type of object that can hold its own data, called
# attributes, and perform its own actions, called methods
"""
Class features
inheritance: child class  can use attributes and methods from parent class
Multi-inheritance: Child class  can inherit attributes and methods from more
than one class
Polymorphism: cheld classes can orride clas methods of parent class
{All classes are objects}
Statements are info inside of a class are usually functions
Class variables - Used by methods in a class
Instance Variables - Used by specific methods to declare  or create a variable
"""

#_init_method - allows every instance of a class to be created or
# initialized with specific parameters pre-determined at the creation of that Object.

# self variable - Makes available all of the attributes to the methods throughout the class

class Person:
    def __int__(self, firstname, lastname, health, status):
        "initialize attributes to be used in/available for all \
    class methods in this class, and for class Objects created \
    by this class."
# attrubutes - self makes the  class mehtodes available to every object in the entire class
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introdue themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname, self.health, self.status))

    def emote(self):
        emotion = random.randrange(1, 3)

        if emotion == 1:
            print("{} is happy today".format(self.firstname))

        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))

        elif self.health >= 76:
            print("{} is a little tired today".format(self.firstname))

        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))

        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))

        else:
            print("{} is unconscious.".format(self.firstname))

    #Maria = Person("Maria", "Guiterrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname,Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))
print("{} is my friend? {}".format(Lee.firstname, Lee.status))