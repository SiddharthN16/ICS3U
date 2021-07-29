#-----------------------------------------------------------------------------
# Name:        Lesson 5 - Functions (functions.py)
# Purpose:     An introduction writing Functions
#
# Author:      Mr. Kowalczewski
# Created:     26-Apr-2019
# Updated:     26-May-2021
#-----------------------------------------------------------------------------

# Functions should always be written at the top of the program, so they are accessible throughout.

def menu():
  '''Displays a basic menu of options.
		 Requires no parameters, doesn't return any values.

  '''

  print('Menu')
  print('Vegetables')
  print('Fruit')
  return

def linearRelation(xValue):
	# Calculates y = 5x - 3 given an xValue

	yValue = 5 * xValue - 3
	return yValue


def hypotenuse(sideA, sideB):
	'''Calculates the hypotenuse and returns it to the sender based on sideA and sideB given.  Returns the hypotenuse value if sideA and sideB are valid, otherwise returns 'Error.'

	'''
	if sideA <= 0 or sideB <= 0:
		return 'Error.'
	else:
		hyp = (sideA ** 2 + sideB ** 2) ** 0.5
		return hyp




# Program runs starting here.  Above this line, the functions are just defined.

# We must 'call' our functions (with required parameters) to make them run.  Similar to when you type print() - you have to give the required parameter (string) for it to work!



# What happens when we 'call' the hypotenuse function?  Nothing - unless you do something with the result! (print, store in a variable etc)

# "calls" the menu() function
menu()
menu()
menu()

# calling linearRelation() function
# linearRelation(10) calls the function with an xValue of 10
# it then 'returns' the yValue - but we have to do something with it!
print(linearRelation(10))

# stores the result of linearRelation(-5) into a new variable
newYValue = linearRelation(-5)

# calling hypotenuse() with side lengths of 3 and 5

print(hypotenuse(3,5))
c = hypotenuse(5,10)
print("The hypotenuse with side lengths of 5 and 10 would be: " + str(c))