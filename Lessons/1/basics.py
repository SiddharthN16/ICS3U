#-------------------------------------------------------------------
# Name:        Lesson 1 - Basics (basics.py)
# Purpose:     Our first lesson, learning the basics
#
# Author:      Mr. Kowalczewski
# Created:     13-Feb-2019
# Updated:     05-May-2021
#----------------------------------------------------------------

# Comments should describe what the code is doing!

# Printing using ', " , '''
print("Hello There!")

print('General Kenobi,')

print('''You are a bold one!''')

# Why use each one?
print('''"You miss 100% of the shots you don't take." - Wayne Gretzky''')

# camelCase variables
myIntegerThatICreated = -25 # integer
myFloat = 5034759.8 # float
myString = "Hello World" # string
myBoolean = False # boolean

# pot_hole_case
my_string = "I don't think the system works"
another_example_of_pot_hole_case = 8


# don't do this
thisisafloat = 5.2
a = 85

# printing variables - always convert integers/floats to string before printing
print(myString)
print(str(myIntegerThatICreated))
print("The value of the float is: " + str(myFloat))


# Showing some Math and storing in variables
# Dividing will always give a float result
myAnswer = 23 / 4
print("The answer to 23 / 4 is: " + str(myAnswer))

# Whenever you divide you'll end up with a float (decimal) answer
myAnswer = int(myAnswer)
print("The answer with no decimals is: " + str(myAnswer))

myNewAnswer = 5 - 9


# Trying some integer divison (//) and modulo (%)
integerDiv = 20 // 3
myModulo = 20 % 3
print("The integer division of 20 by 3 is: " + str(integerDiv) + ", and the remainder would be: " + str(myModulo))

# Doing "math" with a string
numberString = "52"
newString = numberString * 10
print(newString)


# Taking input from the user for a calculation
# The input() function gives you a STRING
userInput = int(input("Please enter your age: "))

# Convert the input into an integer
#userInput = int(userInput)

# Adds 10 years to the age and prints a message
newAge = userInput + 10
print("You will be " + str(newAge) + " in 10 years.")

# Quicker way to increment your variables

myInt = 10
myInt = myInt + 3
print(myInt)

myNewInt = 10
myNewInt += 3
print(myNewInt)

