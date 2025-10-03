on = True # Creating an 'on' key variable
def add():
    a = float(input("Enter a number."))
    b = float(input("Enter another number."))
    print(a + b)

def subtraction():
    a = float(input("Enter a number."))
    b = float(input("Enter another number."))
    print( a - b)

def multipy():
    a = float(input("Enter a number."))
    b = float(input("Enter another number."))
    print( a * b)

def divide():
    a = float(input("Enter a number."))
    b = float(input("Enter another number."))
    print( a / b )

#Adding a while loop to allow the caluclator to calculate
while on:
# Use if/else statements to provide the user options to choose.
# use the input() prompt
    operation = input("Please type +, -, *, /, or q ")
    if operation == '+':
         add()
    elif operation == '-':
         subtraction()
    elif operation == '*':
         multipy()
    elif operation == '/':
        divide()
    elif operation() == 'q':
        on = False
    else:
        print('That operation is not available.')