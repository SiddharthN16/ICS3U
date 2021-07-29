# Notes (Exceptions)

You have likely encountered several "red text" error messages.  The first few lines will tell you where the error is occuring, but usually the last line or two tells you what the problem is.

Consider trying this:

```python
myVariable = int("Hello There")
```

It's not possible to convert that message into an integer, so you get a message that starts with: `ValueError:`.

And if you try this: 

```python
myList = [10,5,2]
print(myList[5])
```

It's not possible to access an item that doesn't exist, so you get a message that starts with: `IndexError:`.

Those are called **Exceptions** in Python.  The code is syntactically correct, but the usage is causing problems.  Luckily we have a way to catch these exceptions before they crash our programs!

## try / except

* `try:` is used when we want to "try" running some code that could potentially cause an exception
* `except Exception:` must follow the try block, to give the instructions if `Exception` occurs.  Note that `Exception` will apply to *any* exception.  We could use the names of the exceptions (`ValueError`, `IndexError` etc) if we want to be more specific.

This is what the above examples would look like:

```python
myList = [10,5,2]

try:
	myVariable = int("Hello There")
	print(myList[5])
except Exception as e:
	print("An error has occured: " + str(e))
else:
	print("All went well!")
```

To run through what happens:
1. The first line in the `try:` block gets run.  If an exception occurs, the program will jump to the appropriate `except:` block.
2. In this case we just have the general `Exception`, that code will be run and the rest of the `try` code gets skipped.
3. If the first line in the `try:` block is successful, it will move onto the next.
4. If all code in the `try:` block runs successfully, the `else` block is run (similar to when a loop exits naturally)

`except Exception as e:` is if *any* errors occur - the error message will get stored in the variable `e`.

We can add as many `except:` blocks as needed for specific exceptions if we wish:
```python
try:
	myVariable = int("Hello There")
	print(myList[5])
except ValueError:
	print("An incorrect value has been given.")
except IndexError:
	print("You've tried access an item that doesn't exist.")
except Exception as e:
	print("An unknown error has occured: " + str(e))
else:
	print("All went well!")
```

This is good if you want different messages or different code run depending on the error.

You can see a long list of exceptions [here](https://docs.python.org/3/library/exceptions.html).

## raise

We can "raise" our own exceptions if parameters / variables don't look the way we want them to.  This will be especially handy to clean up our functions, as proper Python convention only wants *one `return` type*.

This is what we may have done in the past.  Note that there are 2 `return` types (string and int/float), we want to avoid this:

```python
def areaRect(length, width):

	if length <= 0 or width <= 0:
		return "Error: side lengths cannot be zero or negative."
	else:
		area = length * width
		return area		

result = areaRect(10,5)

if result == "Error: side lengths cannot be zero or negative.":
	print("Something went wrong.")
else:
	print("The area of the rectangle is: " + str(result))

```

Rather than `return` the error message (which can cause problems when calling the function), we will `raise` an exception and give our own custom message.

```python
def areaRect(length, width):

	if length <= 0 or width <= 0:
		raise ValueError('Side lengths cannot be zero or negative.')
	else:
		area = length * width
		return area

try:
	result = areaRect(10,5)
except ValueError as e:
	print("An error occured: " + str(e))
else:
	print("The area of the rectangle is: " + str(result))
```

This may seem more challenging than what we were doing before - but remember that functions should be re-usable in other programs or by other people.  It will be easier for others to understand that a `TypeError` occurs, rather than some random error message that you produce.

## isinstance()

We can also make use of the `isinstance()` function to test whether a variable/parameter is a certain **type**.  For example, you wouldn't want the `areaRect()` function to receive string parameters.

```python

# This will evaluate to False
isinstance("Hello There", int)
```

In `exceptions.py` I will lead you through how to modify a function/main code to make use of `try/except/raise`.