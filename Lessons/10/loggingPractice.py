#-----------------------------------------------------------------------------
# Name:        Logging Practice (loggingPractice.py)
# Purpose:     Adding Logging to previous code
#
# Author:      
# Created:     6-Jan-2020
# Updated:     7-Jun-2021
#-----------------------------------------------------------------------------
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITCAL)
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
	logging.info("feetToCm() function beginning with feet of: "+ str(feet) + " and inches of: " +str(inches))
	# Checks if parameters are correct types, raise TypeError
	if not isinstance(feet,int) or not isinstance(inches,(int,float)):
		logging.error("One of the parameters is not a correct type.")
		raise TypeError('An incorrect parameter type was given.')
	# Checks if parameters are correct values, raise ValueError
	if feet <= 0 or inches < 0 or inches > 11:
		logging.error("One of the parameters is negative or invalid.")
		raise ValueError('An incorrect parameter value was given.')
	# Otherwise, proceed with calculation + return result rounded to nearest whole number
	else:
		cm = (feet * 12 + inches) * 2.54
		logging.info("The number of centimetres is: " + str(cm))
		return round(cm)

#Function #2 would be here






# Test Cases
assert feetToCm(5,8) == 173, "5 feet 8 inches should be 173cm"
assert feetToCm(4,9) == 145, "4 feet 9 inches should be 145cm"
assert feetToCm(5,11) == 180, "5 feet 11 inches should be 180cm"

# Main code from last lesson - we will modify to use try/except

try:
# Taking user's height first in feet, then in inches
	logging.debug("Gathering user's information.")
	userFeet = int(input('Input your height in feet: '))
	userInches = int(input('Input the remaining inches: '))

	logging.info("Calling feetToCm() function with feet of: "+str(userFeet) + " and inches of: " + str(userInches))
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

#print(type(userHeight))

try:
	# Taking friend's height first in feet, then in inches
	logging.debug("Gathering friend's information.")
	friendFeet = int(input("Input your friend's height in feet: "))
	friendInches = int(input('Input the remaining inches: '))

	logging.info("Calling feetToCm() function with feet of: "+str(userFeet) + " and inches of: " + str(userInches))
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

logging.debug("Information is gathered, about to compare heights.")
# Figures out which person is taller, prints difference in height
if userHeight > friendHeight:
	diff = userHeight - friendHeight
	logging.info("The user is: " + str(diff) + "cm taller than their friend.")
	print("The user is " + str(diff) + "cm taller than their friend.")
elif userHeight == friendHeight:
	logging.info("The user and friend are the same height!")
	print("The user and friend are the same height!")
else:
	diff = friendHeight - userHeight
	logging.info("The friend is: " + str(diff) + "cm taller than the user.")
	print("The friend is " + str(diff) + "cm taller than their friend.")
