#Argument_Pytest_Selenium
def user_info(name, age, city):
    '''This function prints name, age, and city from an argument to the function.
    Positional arguement name, age, city are read in the postion they are in'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info("Louis", 40, "Las Vegas")

#keyWordArguements
#Key Word Arguements pass values to a function by naming the parameter to which each value
#correponds.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
'''using a f-string is way to insert variables and expressions directly into strings
in python'''

greet(name="Louis", greeting="Hi")
greet(greeting="Good morning", name="Louis")
greet("Louis", greeting="Hey")
greet("Louis")

# *args
# allows for unlimited variables to be passed into a function without defining
# them ahead of time=

def add(*args):
    print(sum(args))

# **kwargs
# allows for unlimeited keyword arguments to be passed into a function
# without defining them ahead of time
def application(**kwargs):
    print(**kwargs)

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))
application("Louis", "Lita", "mail@mail.com", "Triple Ten", 75000, hire_date="September 2025")

