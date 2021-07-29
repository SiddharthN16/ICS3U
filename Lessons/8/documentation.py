#-----------------------------------------------------------------------------
# Name:        Documentation (documentation.py)
# Purpose:     Practice writing proper function documentation
#
# Author:      Mr. Kowalczewski
# Created:     4-Jan-2020
# Updated:     23-Mar-2021
#-----------------------------------------------------------------------------

# We will add proper documentation to the function, and add more comments throughout.

def feetToCm(feet,inches):
	'''
  Converts feet and inches to centimetres.
  
  Receives measurement in feet and inches.  If the parameters are valid (correct type and positive for example), proceeds with conversion and returns a rounded result.
 
  Parameters
  ----------
  feet : int
    Measurement in feet
  inches : int or float
    Remaining measurement in inches
  
  Returns
  -------
  int
    The feet + inches converted into centimetres
   
  Raises
  ------
  TypeError
    If feet is not an integer, or if inches is not an integer or float
	ValueError
    If feet or inches is negative, or if inches is larger than 11
  '''

	# Checks if parameters are correct types, raise TypeError
	if not isinstance(feet,int) or not isinstance(inches,(int,float)):
		raise TypeError('An incorrect parameter type was given.')
	# Checks if parameters are correct values, raise ValueError
	if feet <= 0 or inches < 0 or inches > 11:
		raise ValueError('An incorrect parameter value was given.')
	# Otherwise, proceed with calculation + return result rounded to nearest whole number
	else:
		cm = (feet * 12 + inches) * 2.54
		return round(cm)

	

# Main code from last lesson - we will modify to use try/except

try:
# Taking user's height first in feet, then in inches
	userFeet = int(input('Input your height in feet: '))
	userInches = int(input('Input the remaining inches: '))

# Calling feetToCm() function with user's values
	userHeight = feetToCm(userFeet,userInches)

# Catching exceptions
except TypeError as e:
	print("A TypeError occurred: "+ str(e))
except ValueError as e:
	print("A ValueError occurred: "+ str(e))
else:
	# If try block completes, print result
	print("The user's height in cm is: " + str(userHeight) + "cm.")

print(type(userHeight))

try:
	# Taking friend's height first in feet, then in inches
	friendFeet = int(input("Input your friend's height in feet: "))
	friendInches = int(input('Input the remaining inches: '))

	# Calling feetToCm() function with friend's value
	friendHeight = feetToCm(friendFeet,friendInches)
# Catching exceptions
except TypeError as e:
	print("A TypeError occurred: "+ str(e))
except ValueError as e:
	print("A ValueError occurred: "+ str(e))
else:
	# If try block completes, print results
	print("The friend's height in cm is: " + str(friendHeight) + "cm.")

# Figures out which person is taller, prints difference in height
if userHeight > friendHeight:
	diff = userHeight - friendHeight
	print("The user is " + str(diff) + "cm taller than their friend.")
elif userHeight == friendHeight:
	print("The user and friend are the same height!")
else:
	diff = friendHeight - userHeight
	print("The friend is " + str(diff) + "cm taller than their friend.")

	