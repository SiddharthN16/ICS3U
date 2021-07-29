#-----------------------------------------------------------------------------
# Name:        Exceptions (exceptions.py)
# Purpose:     Learning how to use Try/Except/Raise
#
# Author:      Mr. Kowalczewski
# Created:     30-Dec-2020
# Updated:     6-Jan-2021
#-----------------------------------------------------------------------------


# We will modify this function to raise exceptions.

def feetToCm(feet,inches):
	# Converts a measurement in feet + inches to cm
	if not isinstance(feet,int) or not isinstance(inches,(int,float)):
		raise TypeError('An incorrect parameter type was given.')
	# Checks if parameters are correct values
	if feet <= 0 or inches < 0 or inches > 11:
		raise ValueError('An incorrect parameter value was given.')
	# Otherwise, proceed with calculation + return
	else:
		cm = (feet * 12 + inches) * 2.54
		return round(cm)

	

# Main code from last lesson - we will modify to use try/except

try:
# Taking user's height
	userFeet = int(input('Input your height in feet: '))
	userInches = int(input('Input the remaining inches: '))

# Calling feetToCm() function with user's value, printing result
	userHeight = feetToCm(userFeet,userInches)

except TypeError as e:
	print("A TypeError occurred: "+ str(e))
except ValueError as e:
	print("A ValueError occurred: "+ str(e))
else:
	print("The user's height in cm is: " + str(userHeight) + "cm.")


try:
	# Taking friend's height
	friendFeet = int(input("Input your friend's height in feet: "))
	friendInches = int(input('Input the remaining inches: '))

	# Calling feetToCm() function with friend's value, printing result
	friendHeight = feetToCm(friendFeet,friendInches)
except TypeError as e:
	print("A TypeError occurred: "+ str(e))
except ValueError as e:
	print("A ValueError occurred: "+ str(e))
else:
	print("The friend's height in cm is: " + str(friendHeight) + "cm.")

# Calculate the difference in height
# How do we get this to run, only if everything went well???

if userHeight > friendHeight:
	diff = userHeight - friendHeight
	print("The user is " + str(diff) + "cm taller than their friend.")
elif userHeight == friendHeight:
	print("The user and friend are the same height!")
else:
	diff = friendHeight - userHeight
	print("The friend is " + str(diff) + "cm taller than their friend.")


















