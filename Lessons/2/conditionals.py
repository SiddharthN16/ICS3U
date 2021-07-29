#-------------------------------------------------------------------
# Name:        Lesson 2 - If Statements (conditionals.py)
# Purpose:     To Learn If / Else If / Else statements
#
# Author:      Mr. Kowalczewski
# Created:     22-Feb-2019
# Updated:     07-May-2021
#----------------------------------------------------------------

# Showing the usage of if/elif/else.
# Try changing the value variable to see how this works.
# What is different if you change the elifs to if?

value = -1000

if value == 15:
	print("The value is 15")
	print("We can put as many lines as we want under the if statements")
	print("Even additional if statements")
	print("Provided that they are all indented")
	
elif value < 100 and value > 0:
	print("The number is less than 100")
	print("Please note that after 'and' you have to state the variable again.")
	
elif value > 0:
	print("The value is positive.")

else:
	print("The number is negative")

print()

# You can check for equality (or inequality) with strings as well
# What do >, < signs do?? (position in alphabet)

name = '1Bob'

if name > 'Mr.Kowalczewski':
	print('You do not have authorization.')
else:
	print('Hello Mr.Kowalczewski!')


# Showing the use of and (both) / or (one of)

myNumber = 150
yourNumber = -20


if myNumber < 0 or yourNumber < 0:
	print("At least one of the numbers is less than 0")
else:
	print("Both numbers are positive.")


if myNumber >= 100 and yourNumber >= 100:
	print("Both numbers are greater than or equal to 100")
else:
	print("At least one number is less than 100")
























