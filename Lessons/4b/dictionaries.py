#---------------------------------------------------------------------------
# Name:        Lesson 5b (dictionaries.py)
# Purpose:     Using Dictionaries
#              				
#
# Author:      Mr. Kowalczewski
# Created:     7-May-2019
# Updated:     17-May-2021
#---------------------------------------------------------------------------

# # Using lists for student grades
# studentNames = ['Aaron', 'Billy', 'David', 'Evan', 'Charlie']
# studentGrades = [80, 62, 95, 78, 50]

# del studentNames[1]
# studentGrades.sort()

# # Printing student name with grade
# for i in range(0, len(studentNames)):
# 	print(studentNames[i] + " is earning a grade of: " + str(studentGrades[i]) + "%.")
# print()

# # This may work for now, but what if we start adding/removing/sorting items?  A dictionary may be more useful than a list.

# # The 'key' can be a string, float or integer with no duplicates.

# # The 'value' can be anything, including a list (or another dictionary!)

gradeDict = {'Aaron':80, 'Billy':62, 'David':95,'Evan':76,'Charlie':50,'George':41}

print(gradeDict)
print("The length of this dictionary is: "+ str(len(gradeDict)))


# accessing / adding / deleting data
print(gradeDict['Aaron'])
print(gradeDict['Charlie'])
print(gradeDict['George'])


# Adding new key/value
gradeDict['Frank'] = 88
gradeDict['Aaron'] = 70 # Aaron already exists, so his value is modified
gradeDict['Terry'] = 40
gradeDict['Claire'] = 67

del gradeDict['Billy']

print(gradeDict)
print()

# dictionaries are UNORDERED.  This means that you can't sort them.

# accessing certain parts of the dictionary

print("The ITEMS in the dictionary: ")
for items in gradeDict.items():
	print(items)

print()

print("The KEYS in the dictionary: ")
for keys in gradeDict.keys():
	print(keys)

print()

print("The VALUES in the dictionary: ")
for values in gradeDict.values():
	print(values)

print()


# finding things in the dictionary

if 'Evan' in gradeDict.keys():
	print('Evan is a KEY')

if 50 in gradeDict.values():
	print('That grade is a VALUE')

