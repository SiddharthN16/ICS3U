#-----------------------------------------------------------------------------
# Name:        Creating Two Functions (main.py)
# Purpose:     Practice Creating Functions
#
# Author:      Siddharth Nema
# Created:     26-May-2021
# Updated:     26-May-2021
#-----------------------------------------------------------------------------

# Comment this out
# import functions

# Convert Miles into Kilometres
def milesToKm(distance):
	# Error if number of miles is negative
	if distance < 0:
		return "Error."
	else:
		conversion = round(distance * 1.60934, 2)
		return conversion

# You write the second function saleCalc()!

# Calculate the Discounted Price of an Item
def saleCalc(price, discount):
	# Error if Item Price or Discount is negative or more than 100%
	if price < 0 or discount < 0 or discount >= 100:
		return "Error."
	else:
		# Calculate Final Price and Return
		finalPrice = round(price * (1-(discount/100)), 2)
		return finalPrice










