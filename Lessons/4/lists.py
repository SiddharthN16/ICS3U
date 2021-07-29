#-----------------------------------------------------------------------------
# Name:        Lesson 5 - Lists (lists.py)
# Purpose:     An introduction to using lists in Python
#
# Author:      Mr. Kowalczewski
# Created:     26-Apr-2019
# Updated:     13-May-2021
#-----------------------------------------------------------------------------

# We could create separate variables to store student names.
# What if I want to search for a student? Delete one? etc
studentOne = 'Alvin'
studentTwo = 'Billy'
studentThree = 'Chris'
studentFour = 'David'


# We can generate a list instead
studentList = ['Alvin', 'Billy', 'Chris', 'David', 'Eric']
emptyList = [] # can add to this later!
integerList = [10, 5, 8]
floatList = [2.7, 8.1]

print("What a list looks like when you print: ")
print(studentList)
print()

# A list could include multiple types of information, but try to avoid for now
# (could lead to problems)

mixedList = ["Hello World", 18, True, 19.6]

# Accessing individual (or sequences of) elements (index starts at ZERO)
print("Accessing individual elements:")
print(studentList[1])

myInteger = integerList[2] * 10
print(myInteger)

# Index of -1 is the last element (negative indexes go BACKWARDS)
# This is handy because you may not know how long your list is (without using len())
print(studentList[-3])

# Slice - starting at first index, going UP TO NOT INCLUDING last index
# Add a 3rd number if you want to go backwards or use a different pattern
print(studentList[-1:-3:-1])
print()

# Two methods of using a FOR loop to go through a list.
# There is an important difference!  (Explanation in LESSON.md)
# len() returns the length of the list

# This method allows you to directly access and modify the elements.
print("Using for loop to print all elements:")
'''
for i in range(0, len(studentList), 1):
	studentList[i] = studentList[i] + '!'
	print(studentList[i])

print(studentList)
'''
# for 'each' name (item) in studentList
# This method stores each element one at a time in a SEPARATE VARIABLE, and the original list is not affected.

for name in studentList:
	name = name + '!'
	print(name)

print(studentList)


print()
# There are numerous things we can do with a list - here
# are some of the most important ones.

# You can find even more by searching "Python List Methods".

fruit = ['pineapple', 'apple', 'pear', '1peach', 'banana', '3pineapple',]
numbers = [5, 3, 2, 7, 8, 10]

# Append - adding to a list, where does it go? (to the end)
print("After appending:")
numbers.append(22)
numbers.append(100)
print(numbers)
print()

# Insert - adding to a list at a specific index (first value is index)
print("After inserting:")
numbers.insert(5, 475665756)
print(numbers)
print()

# Two methods to remove items.
# The first method makes use of the index.

del fruit[2]
del numbers[-1]

print("After deleting:")
print(fruit)
print(numbers)
print()

# The second will remove an actual value.  Note that this
# will only remove the first instance.

fruit.remove('pineapple')

print("After removing:")
print(fruit)
print()

# Sorting
fruit.sort() # this sorts the list in lexicographical order
numbers.sort() # this sorts the list in ascending numerical order

print('After sorting:')
print(fruit)
print(numbers)
print()

# You can easily turn a string into a list of the
# individual characters.

message = "Hello there"
chars = list(message)

print("Showing a string variable, and then converting it to a list:")
print(message)
print(chars)
print()
print(chars[4])

# You can also turn a list into a string! (in the quotes is the separator if you want)
print("Joining a list of letters ['a', 'b', 'c', 'd', 'e']")
letters = ['a', 'b', 'c', 'd', 'e']
word = ''.join(letters)
print(word)
print()

# Checking if something is in the list
print("Using the keywords 'in' and 'not' for lists:")
if 'apple' in fruit:
    print('apple is in the fruit list!')
if 2 not in numbers:
    print('2 is not in the numbers list')
print()

# List of lists
listOfLists = [     [1,2,3]      ,     [4,5,6,8,10]      ]
print("Accessing elements in a list of lists:")
print(listOfLists[0][1])
print()

# Watch what happens when I try to duplicate a list - it doesn't work the way you think!

# Setting one list equal to another, simply points the new list at the previous one in the memory.

# Use .copy() to produce an actual copy that won't be modified
newList = numbers.copy()
numbers.append(222222222)
numbers.append(1000000000000)


print(newList)

# You can 'access' individual characters in a string like a list -  but you can't modify!

myString = "I don't like sand."
print(len(myString))
#myString[0] = "!"
print(myString[5:8])










