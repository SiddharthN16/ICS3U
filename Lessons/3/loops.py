#----------------------------------------------------------------
# Name:        Lesson 4 (loops.py)
# Purpose:     Loops (while and for)
#
# Author:      Mr. Kowalczewski
# Created:     27-Feb-2019
# Updated:     11-May-2021
#----------------------------------------------------------------

# basic use of while loop

count = 1
while count < 10:
	print(str(count))
	count = count + 1

print("The Loop is over")
		


# while loops are good when you don't know how many times the code
# should be repeated

# A 'while True' loop that breaks (with an if statement) should NOT be used.
# This is bad form - why not put that condition as the loop condition??

'''
while True:
	siblings = int(input("How many siblings do you have? "))

	if siblings > 0 and siblings < 10:
		break
 
print("You have " + str(siblings) + " siblings.  I only have one!")
'''


# This is better form:
siblings = -5000
while siblings < 0 or siblings > 10:
	siblings = int(input("How many siblings do you have? "))
	
	# break out of loop early if 100 is entered
	if siblings == 100:
		print("I don't believe you")
		break

# this condition only runs when the loop exits naturally
else:
	print("You have " + str(siblings) + " siblings.  I only have one!")


	


# 'for' loops are good for when you know exactly
# how many times the loop should run (or there is a # pattern).

for count in range(1,11,1):
	print("The current count is: " + str(count))


# the variables 'i', 'j' and 'k' are typically used for loops even though they're not descriptive
for i in range(100, 20,-5):
	print("The current count is: " + str(i))


# Calculate average. For loops are good when we KNOW how many times it should run

total = 0

for course in range(1, 5, 1):
	grade = int(input("Input your grade for course #" + str(course)+ ": "))
	total = total + grade

average = total / 4
print("Your average is: " + str(average) + "%")








	

	
	