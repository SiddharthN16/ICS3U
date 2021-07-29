# Notes (Assertions)

In programming an *assertion* is something that should evaluate to `True` at a particular moment.  We will be using assertions to test that our functions work the way we want them to.

```python

assert (some sort of statement), (some sort of error message)
```

For example:

```python

assert 1 + 1 == 2, "1 + 1 should equal 2"
```

If we were to run the above code - nothing happens because it's true!  It's only if the assertion is *false* that the error message will display.

Here's an example of how to use assertions to test our functions:

```python
def areaRect(length, width):
	if not isinstance(length,(float,int)) or not isinstance(width,(float,int)):
		raise TypeError("Length and width must be int/float")
    if length <= 0 or width <= 0:
        raise ValueError('Side lengths cannot be zero or negative.')
    else:
        area = length * width
        return area

assert areaRect(10,2) == 20, "10 by 2 should be an area of 20"
assert areaRect(5,8) == 40, "5 by 8 should be an area of 40"
assert areaRect(100,3) == 300, "100 by 3 should be an area of 300"
```

In `assertions.py` we will add assertions to the previous lesson code.




