#Condtional statements - Allow for the execution of specific code blocks
#based on whether a given codition evaluates to True or False
#Comparison Operatiors allow for a comparison between two values
print(1 < 1)
print( 1 > 1)
print( 1 <= 1)
print( 1 >= 1)
print( 1 == 1)
print( 1 != 1)

#if, else, elif ( Logical Operators Use )
#if - Shows code only if its conditions is Ture
age = 20
if age >= 18:
    print("You are an adult")

name = input("What's your name?")
if name == "Jessica":
    print("Hello, nic to see you {}".format(name))
print("Have a nice day!")

# else - Code executes if the if condition evaluates to False
name = input("What is you name?")
if name == "louis":
    print("Hi, Louis!")
else:
    print("Thanks for entering your name," + name)

score = 75
if score >= 90:
    print("Excellent!")
else:
    print("Good effort, keep practicing.")

#elif - Allows for checking multiple conditions in sequence. Evaluates only if
#the prededing if or elif conditions were False
temperature = 10
if temperature < 19:
    print("It's chilly outside.")
elif temperature > 25:
    print("It's pleasant outside.")
else:
    print("It's a bit chilly.")

#more practice
name = input("What's your name? ")

if name == "Jessica":
    print("Hello, nice to see you {}".format(name))

elif name == "Danielle":
    print("Hello, you are a great person!")

elif name == "Kingston":
    print("Hi, {}, let's have lunch soon!".format(name))

print("Have a nice day!")

#Once a condition is meet, the other conditions become void


