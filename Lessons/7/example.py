#-----------------------------------------------------------------------------
# Name:        Basic Example (example.py)
# Purpose:     A basic example of try/except
#
# Author:      Mr. Kowalczewski
# Created:     30-Dec-2020
# Updated:     6-Jan-2021
#-----------------------------------------------------------------------------

def areaRect(length, width):
		if not isinstance(length, int) or not isinstance(width, int):
			raise TypeError('Side lengths must be an integer')
		if length <= 0 or width <= 0:
			raise ValueError('Side lengths cannot be zero or negative.')
		else:
			area = length * width
			return area


try:
		areaRect("a",10)
		result = areaRect(10,5)
except ValueError as e:
    print("An ValueError occured: " + str(e))
except TypeError as e:
		print("A TypeError occured: " + str(e))
else:
    print("The area of the rectangle is: " + str(result))


'''
myList = [10,5,2]

# both of these would crash your program!

try:
	myVariable = int(input("Input a number: "))
	print(myList[10])
except Exception as e:
    print("An error has occured: " + str(e))
'''





