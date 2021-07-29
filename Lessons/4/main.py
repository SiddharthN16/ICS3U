#-----------------------------------------------------------------------------
# Name:        Grocery List Task (main.py)
# Purpose:     Understand and manipulate Lists
#
# Author:      Siddharth Nema
# Created:     13-May-2021
# Updated:     13-May-2021
#-----------------------------------------------------------------------------

# Lesson files
# import lists

groceryList = []

# Initial input for the program
groceryItems = input()

# Use while loop to use input() to fill list
# Items are added only if not already in list
# Loop should stop when '!' is entered

# Loop runs as long as the input is not "!"
while groceryItems != "!":

    # Checks if inputted item is in list, if it is not, item is added to list
    if groceryItems not in groceryList:
        groceryList.append(groceryItems)

    # Repeated inputs for the loop
    groceryItems = input()

# Sort and print the list
groceryList.sort()
print(groceryList)

# Print 3rd item, then 3rd LAST item
print(groceryList[2])
print(groceryList[-3])

# Print slice of 4th through 6th item
print(groceryList[3:6])

# Print same slice BACKWARDS
print(groceryList[5:2:-1])

# Remove last item
groceryList.remove(groceryList[-1])

# Take input(), remove that item if it exists
itemRemover = input()
if itemRemover in groceryList:
    groceryList.remove(itemRemover)

# Print List
print(groceryList)

# DO NOT CHANGE THIS LIST
intList = [5, 8, -10, 3, 18, 22, 1, 71]

# If item in list is odd, multiply by 2
# Checks the whole list for numbers that are not divisble by 2 and multiplies them by 2
for i in range(len(intList)):
    if intList[i] % 2 != 0:
        intList[i] *= 2

# Print List
print(intList)
