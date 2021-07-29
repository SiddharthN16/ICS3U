# Notes (Looping Structures (while and for))

Most programming languages run instructions one at a time until the end of the code.

We can use "loops" to repeat sections of code however many times we want.

In this course we'll focus on two different types of looping structures: ```while``` and ```for```.


## While Loops

This looping structure will continue doing something **while** a condition is ```True```, like the structure below.

```python
count = 1
while count < 10:
  print(str(count))
  count = count + 1
```

The structure of a ```while``` loop is very similar to an ```if``` statement as shown above.  You can use anything that you can with an ```if``` to check whether the condition is ```True``` or ```False```.

Note that the condition is only checked once the loop has reached the end.

Another option that open up with a ```while``` loop is the ```else``` option, just like an ```if``` statement.  The ```else``` is what happens the moment the ```while``` loop becomes ```False```

The while loop is mostly used for when you are not sure exactly how many times you need to run through a loop, whereas the ```for``` loop is only run when you know how many times to loop. 

## For Loops
This looping structure will count from one value to another by a particular increment structured as below.

```python
for iterator in range(start, stop, step):
  pass
```

The above has some new concepts such as:
* ```iterator``` - Is a variable that is created on the spot and can be used inside the ```for``` loop.  This value changes every time the loop starts over.
* ```range()``` - This creates a list of values for the ```iterator``` to be while inside the ```for``` loop.
* ```start``` - Is an integer value to start the range.
* ```stop``` - Is an integer value to end the range.  Python will not include that particular value itself (see examples).
* ```step``` - Is the value that the ```iterator``` changes by each time the loop restarts.

```python
# Count up
for count in range(0, 5, 1):
  print(str(count))

# Output
# 0
# 1
# 2
# 3
# 4


# Count down
for count in range(5, 0, -1):
  print(str(count))

# Output
# 5
# 4
# 3
# 2
# 1
```

There are advanced uses of for loops.  These will be pointed out when we get to those concepts in the future.


## Loops in general

A few of the commands and options that open up with a ```while``` or ```for``` loop is:
* ```break``` - To break out of a loop early.  This should only be used in special circumstances and *not* as the only exit condition.
* ```continue``` - To jump back to the beginning of the loop early.  This should be **rarely** used.
* ```pass``` - This is something to be used either (a) temporarily, or (b) to ensure your program runs properly
