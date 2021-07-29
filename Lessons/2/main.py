#-----------------------------------------------------------------------------
# Name:        Grade Input/Output Test (main.py)
# Purpose:     Check if Inputted grade Matches Given Standards
#
# Author:      Siddharth Nema
# Created:     07-May-2021
# Updated:     07-May-2021
#-----------------------------------------------------------------------------

# Comment out the line below when you're done with the lesson code.
#import conditionals

# You will check the 'grade' variable using if/elif/else statements.
# Your output must EXACTLY MATCH what is requested in TASK.md

# Enter a grade value
grade = int(input())

# Check if grade is between 80 and 100 & print evaluation
if grade >= 80 and grade <= 100:
	print("Exceeding Expectations.")

# Otherwise check if grade is between 70 and 79 & print evaluation
elif grade >= 70 and grade <= 79:
  print("Meeting Expectations.")

# Otherwise check if grade is between 50 and 69 & print evaluation
elif grade >= 50 and grade <= 69:
  print("Needs Improvement.")

# Otherwise check if grade is between 0 and 50 & print evaluation
elif grade >= 0 and grade <= 50:
  print("Not Passing.")

# Otherwise the grade is not valid
else:
  print("Invalid Grade.")