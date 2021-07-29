#-----------------------------------------------------------------------------
# Name:        Lesson 1 - Basics (main.py)
# Purpose:     Our first lesson, learning the basics
#
# Author:      Siddharth Nema
# Created:     05-May-2021
# Updated:     05-May-2021
#-----------------------------------------------------------------------------

# This line will run the basics.py file (my example).
# You can comment this out when starting your exercise.
# All of your assignments/exercises should be written in main.py - you won't have to worry about this.
# import basics

# Start writing your code here! (and make sure to modify the header above!)

# Ask user for a speed in KMH
kmhSpeed = int(input("Enter your Speed in Km/H:\n"))

# Converts the KMH value to MPH and prints to Console
mphSpeed = round(kmhSpeed * 0.621371,2)
print("Your Speed in Miles is about: " + str(mphSpeed) + " MPH")

# Enter what your current mark is and what mark you want to get in percentages
currentMark = float(input("\nEnter your current mark(%):\n"))
wantedMark = float(input("Enter the mark you want to achieve(%):\n"))

# Calculates mark required on the next test and prints to Console
markRequired = int(wantedMark*2 - currentMark)
print("To get your desired mark, you will need to get " + str(markRequired) + "% on the next test.\n")

# Enter a phrase to be converted to Hexadecimal
phrase = input("Enter your phrase to be converted to Hexadecimal:\n")
# Encodes the string into hexadecimal and prints it to console
hexValue = phrase.encode().hex()
print("Your text in Hexadecimal is: " + str(hexValue))

# Converts the hexaadecimal back to text to confirm it worked
hexCheckValue = input("Enter the Hexadecimal value to check if it is correct:\n")
stringConvert = bytes.fromhex(hexCheckValue).decode("ascii")
print("The hexadecimal converted back to a string is: '" + stringConvert + "'\n")

# Asking the user to input the dimensions of the rectangle
rectLength = float(input("Enter the length of the rectangle\n"))
rectWidth = float(input("Enter the width of the rectangle\n"))
# Calculate the area of the rectangle and print to console
rectArea = rectLength * rectWidth
print("The area of the rectangle is " + str(round(rectArea,2)) + " square units\n")

# Enter the number of people playing the game
totalPlayerCount = int(input("Enter the number of people playing the game:\n"))

# Determine the max group size, the number of groups formed & how many people are leftover if any
maxGroup = 4
groupCount = int(totalPlayerCount/maxGroup)
leftOver = totalPlayerCount % maxGroup

# Print statement to the console
print("There will be " + str(groupCount) + " groups of " + str(maxGroup) + " with " + str(leftOver) + " player(s) leftover.")