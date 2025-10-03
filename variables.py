# python practice
cars = 23
car_ = 24
CARS = 25
cars = 456684 # if the are two of the same variable, python will
# use the most recent of the made variables when printing the statemens
number_of_cars = 23
kind_of_cars = "Mazda"

print(car_)
print(cars)
print(CARS)
print(number_of_cars)
print(kind_of_cars)

""" 
Multi-line comment for for doc-string for large line of code
"""
#String Formating - Controlling how output appears
name = "Louis H"
type_of_car = "Toyota"
school = "UNLV"
# concatenate the variables in the print statement
print(name + " attends school at " + school)
# python string format() function
#uses curly braces in place of the variables to insert the variable argument
# in the .format() function for cleaner code

print("{} attends school at {}.".format(name, school))

"""
Functions - Unit of code can be reused through out a program, 
Parts of a Function

def uniqueFunctionName():
    Body is indented four spaces
remove_the_spaces_when_calling_a_function()
            
Examples:
"""
def setUp(self):
    self.browser = webdriver.Firefox()
    self.addCleanup(self.browser.quit)

def testPageTitle(self):
    self.browser.get('http://www.google.com')
    self.assertIn('Google', self.browser.title)

def addition():
    a = 10 #hard coded
    b = 30 #hard coded
    print(a+b)
#calling the function
addition()
#Getting user input for the addtion function
#Built in Python input method
# input("user prompt is always a string")
# covert string data into an integer by using the int() within the body of function

def addtion():
    a = int(input("Enter a number. "))
    b = int(input("Enter another number. "))
    print(a + b)

    #place two lines between end of function and call function
addtion()




