# Notes (Basics)

### Comments / Header

When we begin writing code, it's important to write *comments* throughout to explain what your code is doing.  This is both for you and for anybody that is trying to read your code!

In Python we use the ```#``` sign at the beginning of a line to tell the intrepeter to ignore it.

```python
# This is a comment!
This is not a comment!
```

At the top of each program we'll include a *header* - same idea as having a title page (name, date, etc).

### Printing to console

When printing strings (text), there are 3 different "quote" levels that you can use.  The most used are single-quotes (apostrophes); however, the other two do have their place.  The double-quotes are mainly used if you have an apostrophe within the string itself (i.e. "What's going on?").  The triple-quote (three apostrophes) is mainly used when you have both a double-quote and apostrophes in it (i.e. ('''Mr. Seidel said, "Who's there?"''')

```python
print('Hello world!')
print("Hello world!")
print('''Hello World!''')
```

It is possible to print a number on it's own, but you will run into problems when trying to combine the number with some text (called string concatenation).

You can solve this problem by wrapping the number with a `str()` function.

```python
print(str(22))
# The following will cause a problem
print('The value of x is: ' + 5.5)
# But this won't!
print('The value of x is: ' + str(5.5))
```

### Variables and printing

Variables are used to temporarily store information, and can be manipulated in multiple ways.  

Variables should be named so that it is easy to tell what the value held by the variable is.

There are two naming conventions for variables to make them easily readable.  Either is fine as long as you're consistent.

```python
# camelCase
myFirstInteger = 22

# pot_hole_case
my_first_integer = 22
```

Variables can be of different types such as:
* integers (whole number values)
* floats (can include decimal values)
* strings (text)
* Boolean values (True or False)
* and more!

In Python we don't have to declare what type the variable is - the intrepeter will figure that out from what you assign it.

```python
integerOne = 15
myFloat = 18.6
greeting = 'Hello'
myBool = False
```

When printing out variables, you will want to wrap the text with a ```str()``` function if you know that the values might be numeric.  If you know they are strings you can print out the information directly to the ```print()``` function.

```python
result = 80
print("The result of the calculation is: " + str(result))

message = "There"
print("Hello " + message)
```

### Mathematical Operations

You can use the standard mathematical operators ```+```, ```-```, ```*```, ```/``` as well as some other ones that you might not be used to using such as:
* ```//``` - This is used to do integer division (see below)
* ```%``` - This is used to find the remainder after a division (see below)
* ```**``` - This is used for a power (see below)

```python
integerDivisionOfFloats = 5.5 // 2
print(integerDivisionOfFloats)	#  Should be 2

moduloOfIntegers = 5 % 2
print(moduloOfIntegers)  # Should be 1

powerOfIntegers = 2 ** 3
print(powerOfIntegers)   # Should be 8
```

Make sure that you are doing math with integers or floats only - weird things happen when you do "math" with strings!  

### Converting between types

You can convert between different data types by using functions such as:
* ```int()``` - Will convert to an integer
* ```float()``` - Will convert to a float value
* ```str()``` - Will convert to a string
* and more!

```python
integerConversion = int(5.5)
print(str(integerConversion))

floatConversion = float(2)
print(str(floatConversion))
```

### Receiving input from the user

Sometimes you will want to ask someone to enter information for you so that you can process that information and print it back out.  This is useful if you are, for example, receiving information to create a database, or to calculate the hypotenuse of a right-angle triangle, etc.

To do so, we use the ```input()``` function.  The ```input()``` function takes one argument (information in the parentheses) which is typically the question that we would ask the user to help guide them, as a string.  For example:

```python
name = input('Enter your name: ')
print(name)
```

The above program prompts the user with ```Enter your name: ``` and waits for the user to enter information to continue.  Afterwards, it will then just print out the name entered.

When using the ```input()``` function, it will *always* return a string type variable (text).
Even if a number is entered, it will be the "text" of that number.  If you wish to use the user's input for any calculations, you'll have to convert it to an integer or float.
