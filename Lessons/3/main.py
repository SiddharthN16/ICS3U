#-----------------------------------------------------------------------------
# Name:        Factorial and Adding Calculator (main.py)
# Purpose:     While & For loop practice
#
# Author:      Siddharth Nema
# Created:     11-May-2021
# Updated:     11-May-2021
#-----------------------------------------------------------------------------

# Comment out the line below when you're done with the lesson code.
# import loops

# Variables required for program
number = int(input())
count = 0
factorial = number

# Check if the number will cause an error or not
if number < 1:
    print("Error.")
else:
    # Keep looping until the count is greater than the number
    while count < number - 1:  # subtracted by one to prevent an extra multiplication of the number
        count += 1  # count is increased every loop
        factorial *= count  # the input number value is multiplied by all its previous integers calculated by the count variable
    print(str(factorial))

# variables required for program
begin = int(input())
end = int(input())
count = 0

# Checks if the inputted numbers will cause an error or not
if begin > end:
    print("Error.")
else:
    # for loop which loops from the beginning number to the end number
    for i in range(begin, end + 1):
        count += i  # adds the value of the numbers betweeen beginning and end together
    print(count)
