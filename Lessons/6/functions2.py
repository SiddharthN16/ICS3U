#-----------------------------------------------------------------------------
# Name:        Lesson 6 - Functions part 2 (functions2.py)
# Purpose:     Practicing the calling of functions
#
# Author:      Mr. Kowalczewski
# Created:     26-Apr-2019
# Updated:     18-Mar-2021
#-----------------------------------------------------------------------------

# When you are writing a program, ALL FUNCTIONS should be at the VERY TOP of our code.  There should be no code in between.

# This allows your functions to be accessible throughout your program.


def feetToCm(feet,inches):
	# Converts a measurement in feet + inches to cm

	if feet < 0 or feet > 8 or inches < 0 or inches > 11:
		return 'Error.'
	else:
		cm = (feet * 12 + inches) * 2.54
		return round(cm)

	

# Main code goes here (code that runs)
# How can we make multiple uses of this function, that produce different results?
# Writing a function and calling it ONCE doesn't make it worthwhile!

# Taking user's height
userFeet = int(input('Input your height in feet: '))
userInches = int(input('Input the remaining inches: '))

# Calling feetToCm() function with user's value, printing result
userHeight = feetToCm(userFeet,userInches)
print("The user's height in cm is: " + str(userHeight) + "cm.")

# Taking friend's height
friendFeet = int(input("Input your friend's height in feet: "))
friendInches = int(input('Input the remaining inches: '))

# Calling feetToCm() function with friend's value, printing result
friendHeight = feetToCm(friendFeet,friendInches)
print("The friend's height in cm is: " + str(friendHeight) + "cm.")

# Calculate the difference in height
if userHeight > friendHeight:
	diff = userHeight - friendHeight
	print("The user is " + str(diff) + "cm taller than their friend.")
elif userHeight == friendHeight:
	print("The user and friend are the same height!")
else:
	diff = friendHeight - userHeight
	print("The friend is " + str(diff) + "cm taller than their friend.")