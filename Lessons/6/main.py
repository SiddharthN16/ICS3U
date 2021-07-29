#-----------------------------------------------------------------------------
# Name:        Using Functions (main.py)
# Purpose:     Practice Using Functions Multiple Times
#
# Author:      Siddharth Nema
# Created:     27-May-2021
# Updated:     27-May-2021
#-----------------------------------------------------------------------------

# Convert Miles into Kilometres
def milesToKm(distance):
	# Error if number of miles is negative
	if distance < 0:
		return "Error."
	else:
		conversion = round(distance * 1.60934, 2)
		return conversion

# Calculate the Discounted Price of an Item
def saleCalc(price, discount):
	# Error if Item Price or Discount is negative or more than 100%
	if price < 0 or discount < 0 or discount >= 100:
		return "Error."
	else:
		# Calculate Final Price and Return
		finalPrice = round(price * (1-(discount/100)), 2)
		return finalPrice

print("YOU LIVE IN CANADA, BUT YOUR GPS IS FROM USA & ONLY USES MILES\n")

print("STORE ONE:")
# Enter Price, Discount & Distance for Store Two
storeOnePrice = int(input("Enter the Price of the Item: "))
storeOneDiscount = int(input("Enter the Discount off the Item: "))
storeOneMiles = int(input("Enter the Store One's Distance from your Home in Miles: "))

# Use both Functions to Find Discounted Price & Km Distance for Store One, & Print
storeOneFinal = saleCalc(storeOnePrice, storeOneDiscount)
storeOneKm = milesToKm(storeOneMiles)
print(f"The Item's Final Price from Store One is ${storeOneFinal} and is {storeOneKm} Km from your Home.")

print("\nSTORE TWO:")
# Enter Price, Discount & Distance for Store Two
storeTwoPrice = int(input("Enter the Price of the Item: "))
storeTwoDiscount = int(input("Enter the Discount off the Item: "))
storeTwoMiles = int(input("Enter the Store's Distance from your Home in Miles: "))

# Use both Functions to Find Discounted Price & Km Distance for Store Two, & Print
storeTwoFinal = saleCalc(storeTwoPrice, storeTwoDiscount)
storeTwoKm = milesToKm(storeTwoMiles)
print(f"The Item's Final Price from Store One is ${storeTwoFinal} and is {storeTwoKm} Km from your Home.")

# Calcaulate the Difference in Price & Distance
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