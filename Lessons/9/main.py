#-----------------------------------------------------------------------------
# Name:        Assertations (main.py)
# Purpose:     Adding Assertations to Program
#
# Author:      Siddharth Nema
# Created:     03-June-2021
# Updated:     03-June-2021
#-----------------------------------------------------------------------------
# Your program should look like this:
# Both Functions
# Assertions (for both)
# Main Code

def milesToKm(distance):
	'''
  Converts Miles to Kilometres.
  
  Receives Distance in Miles.  If the parameters are valid (correct type and positive), proceeds with conversion and returns result rounded to two decimals.
 
  Parameters
  ----------
  distance : int or float
    Distance in Miles

  Returns
  -------
  float
    The distance in miles converted into kilometres
   
  Raises
  ------
  TypeError
    If distance is not an integer or float
	ValueError
    if distance is a negative number
  '''

	# Checks is Parameters are Correct Type, Raises TypeError
	if not isinstance(distance, (int,float)):
		raise TypeError("Invalid Parameter Type")
	# Checks if Parameters are Correct Values, Raises ValueError
	if distance < 0:
		raise ValueError("The Distance must be a Positive Value.")
	# Otherwise, Proceeds with Calculation & Returns Result to 2 Decimal Places
	else:
		conversion = round(distance * 1.60934, 2)
		return conversion


def saleCalc(price, discount):
	'''
  Calculates the Discounted Price of an Item.
  
  Receives item cost and discount to be applied.  If the parameters are valid (correct type and positive), proceeds with calculation of final price and returns the cost rounded to two decimals.
 
  Parameters
  ----------
  price : int or float
    Price of the Item 
  discount : int
    Discount to be applied to item
  
  Returns
  -------
  float
    The final price of the item after discount
   
  Raises
  ------
  TypeError
    If price is not a float or integer, or if the discount is not an integer
	ValueError
    If the price or discount is negative, or if discount is greater than 100
  '''

	# Checks is Parameters are Correct Type, Raises TypeError
	if not isinstance(price,(int, float)) or not isinstance(discount,int):
		raise TypeError("Incorrect Paramter Type")
		print("Works")
		
	# Checks if Parameters are Correct Values, Raises ValueError
	if price < 0 or discount < 0 or discount >= 100:
		raise ValueError("Discount & Price must be a Positive Value.")
	# Otherwise, Proceeds with Calculation & Returns Result to 2 Decimal Places
	else:
		finalPrice = round(price * (1-(discount/100)), 2)
		return finalPrice

# milesToKm() Test Cases
assert milesToKm(10) == 16.09, "10 Miles should be 16.09 Kilometres"
assert milesToKm(4) == 6.44, "4 Miles should be 6.44 Kilometres"
assert milesToKm(23) == 37.01, "23 Miles should be 37.01 Kilometres"

# saleCalc() Test Cases
assert saleCalc(50.99,50) == 25.5, "50% Discount off $50.99 should be $25.5"
assert saleCalc(99.99,35) == 64.99, "35% Discount off $99.99 should be $64.99"
assert saleCalc(65,75) == 16.25, "75% Discount off $65 should be $16.25"

# MAIN CODE
print("YOU LIVE IN CANADA, BUT YOUR GPS IS FROM USA & ONLY USES MILES\n")

storeOneKm = None
print("STORE ONE:")
# Loops variable is empty; only happens if error occurs
while bool(storeOneKm) == False:
	try:
		# Enter Price, Discount & Distance for Store One
		storeOnePrice = float(input("Enter the Price of the Item: "))
		storeOneDiscount = int(input("Enter the Discount off the Item: "))
		storeOneMiles = float(input("Enter the Store One's Distance from your Home in Miles: "))
		# Use both Functions to Find Discounted Price & Km Distance for Store One
		storeOneFinal = saleCalc(storeOnePrice, storeOneDiscount)
		storeOneKm = milesToKm(storeOneMiles)
	# Catching Exceptions
	except TypeError as e:
		print(f"A TypeError has occured: {e}")
	except ValueError as e:
		print(f"A ValueError has occured: {e}")
	# If try Block Completes, Print Result
	else:
		print(f"The Item's Final Price from Store One is ${storeOneFinal} and is {storeOneKm} Km from your Home.")
		

storeTwoKm = None
print("\nSTORE TWO:")
# Loops variable is empty; only happens if error occurs
while bool(storeTwoKm) == False:
	try:
	# Enter Price, Discount & Distance for Store Two
		storeTwoPrice = float(input("Enter the Price of the Item: "))
		storeTwoDiscount = int(input("Enter the Discount off the Item: "))
		storeTwoMiles = float(input("Enter the Store's Distance from your Home in Miles: "))

		# Use both Functions to Find Discounted Price & Km Distance for Store Two
		storeTwoFinal = saleCalc(storeTwoPrice, storeTwoDiscount)
		storeTwoKm = milesToKm(storeTwoMiles)
	# Catching Exceptions
	except TypeError as e:
		print(f"A TypeError has occured: {e}")
	except ValueError as e:
		print(f"A ValueError has occured: {e}")
	# If try Block Completes, Print Result
	else:
		print(f"The Item's Final Price from Store One is ${storeTwoFinal} and is {storeTwoKm} Km from your Home.")
		
# Calculates which Store Costs Less & Which Store is Closer
if storeOneFinal > storeTwoFinal:
	priceDiff = storeOneFinal - storeTwoFinal
	print(f"Store One is cheaper by ${priceDiff}, buy the item from Store One")
elif storeTwoFinal > storeOneFinal:
	priceDiff = storeTwoFinal - storeOneFinal
	print(f"Store Two is cheaper by ${priceDiff}, buy the item from Store Two")
else:
	if storeOneKm > storeTwoKm:
		distDiff = storeOneKm - storeTwoKm
		print(f"Both Store's have the Same Price, But storeOneKm is closer by {distDiff} Km.")
	elif storeOneKm > storeTwoKm:
		distDiff = storeOneKm - storeTwoKm
		print(f"Both Store's have the Same Price, But storeTwoKm is closer by {distDiff} Km.")
	else:
		print("Both Store's have the Same Price & are Equally Far from your Home!")