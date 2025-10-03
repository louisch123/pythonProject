#Loop- a control flow statement that allows a block of code to be
# executed repeatedly. This repetition can occur either a specific
# number of times or as long as a certain condition remains true
# TWO TYPES OF LOOPS: for loop and while loop

# for loop - iterating over a a sequence(List, tuple, string, or range).
# Block of code is executed each item in the sequence, suitable for a number
# of interations is known or determined by the length of the iterable.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
        print("Would like you like {} ? " .format(fruit))

#using for loop over a range, using the range()
for number in range(1,11):
    print("Number {}".format(number))

#While Loop -  Will repeatedly execute a block of code
# as long as as a given condition is true. Useful when a number of iterations is not known
temp = 37
while temp > 32:
    print("the water is not frozen")
    temp -= 1 #using the decrement operator '-=' decreaes item
print("water becomes ice at 32 degrees")

temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1

# loop controls -  Controlling the flow of a loop using Break, Continue, Pass
#BREAK - immediately terminates the loop it is within
temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break

#CONTINUE - Skips the remainder of the current iteration of the loop and proceeds to the nxt
# iteration
for number in range(1,11):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}".format(number))

#PASS - is a null operation, it does nothing. Used as a placeholder
# when a statment is syntactically required but no action needs to be performed.
for number in range(1,11):
    if number == 3:
        pass
    else:
        print("Then number is {}".format(number))


