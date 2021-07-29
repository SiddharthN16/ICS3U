# This is an attempt at the loops exercise (factorial)

# We can't "see" the calculations that are happening, so how do we diagnose the issue?

# You may have used some print() lines in the past:

value = 5
result = 1
while value > 0:
		result *= value
		#print("The new result is " + str(result) + " after multiplying by " + str(value))
		value -= 1
		#print("The new value to multiply by is " + str(value))
 
print(result)