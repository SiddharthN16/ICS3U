# Notes (Logging)

When trying to figure out what's wrong with your program, you may have intuitively added a bunch of `print()` statements throughout to diagnose the problem.  Here's an example:

```python

# calculate a factorial

value = 5
result = 1
while value >= 0:
	result *= value
	value -= 1

print(result)
```

This doesn't produce the result I want (120).  To diagnose the problem, I can add a couple of `print()` statements so I can "see" what's happening in the loop.

```python

# calculate a factorial

value = 5
result = 1
while value >= 0:
	result *= value
	print("Result is: " + str(result) + " after multiplying by: " + str(value))
	value -= 1
	print("Next value will be: " + str(value))

print(result)
```

After running this, you can see that I didn't stop the loop when `value = 0` (OOPS).

This method of debugging works for now, but we don't want this sort of output in our final product.  We could delete all of the `print()` statements, but that won't help us solve future problems if they occur.

## Logging

To make use of the debugging and logging features in Python, we will need to import a library to help us out.  A library is a set of tools that someone else wrote that we will be making use of.

Anytime we go to use the logging features we will need to use the two lines of code below at the beginning of our programs.  Don't worry about understanding how these lines work, you will just copy/paste them for now.

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```
or

depending on whether we will want to have our debug information sent to a log file, or sent to the console. 

We'll add some basic logging to our previous lesson code in `loggingPractice.py`, by using the code `logging.debug()`.  These messages (like comments) should be descriptive - not just a number for example.

But where should we add it? How often? There's no standard, but you should add logging for the following:

- When variables change value (like in the above example)
- When exceptions occur
- When significant events happen (function beginning/ending, loop exiting etc)
- Anywhere problems can occur!


By placing logging messages at these points, you'll be able to easily identify issues when they appear.  But you'll notice that we're still getting things printed to the console - we'll deal with that soon,

### Logging Levels
There are five logging levels, as shown below, where the least important is at the top, and the most important is at the bottom of the table.  This table was source from [here](https://automatetheboringstuff.com/chapter10/#calibre_link-2862).

| Level | Logging Function | Description |
| ----- | ---------------- | ----------- |
| DEBUG | ```logging.debug()``` | The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems. |
| INFO | ```logging.info()``` | Used to record information on general events in your program or confirm that things are working at their point in the program. | 
| WARNING | ```logging.warning()``` | Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future. |
| ERROR | ```logging.error()``` | Used to record an error that caused the program to fail to do something.|
| CRITICAL | ```logging.critical()``` | The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely. |

We'll make some changes to `loggingPractice.py` to make use of these different levels.


### Logging to a file
We don't always want the program to display information to the console.  In a scenario where your program gets released to the public, you won't want your program randomly displaying debug information all over the place.  Instead, the majority of program use logs and logging functions to output their work to a specific log file.  For u to do the same, we will want to change our first 2 lines to something like below instead.  Note that the only change is the addition of **```filename='log.txt',```**.

```python
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

This will cause all of the debug information to be sent to the ```log.txt``` file instead of being displayed to the console.

*Repl.it is sometimes weird about logging to a file, so this may not always work.  But as long as you have the addition above, you've done it correctly!*


### Disabling Logging Quickly
Unlike when you place ```print()``` statements everywhere in your program, you do **not** have to delete all of your ```logging.debug()``` statements.  Instead, you can add a single line to disable **all** of your ```logging.``` statements.  Depending on which ```logging.``` statements you want to disable, you would put in different options as below:

| Level | Disabling Function | What is disables |
| ----- | ------------------ | ---------------- |
| DEBUG | ```logging.disable(logging.DEBUG)``` | Only ```logging.debug()``` statements |
| INFO  | ```logging.disable(logging.INFO)``` | As above, and ```logging.info()``` statements |
| WARNING | ```logging.disable(logging.WARNING)``` | As above, and ```logging.warning()``` statements |
| ERROR | ```logging.disable(logging.ERROR)``` | As above, and ```logging.error()``` statements |
| CRITICAL | ```logging.disable(logging.CRITICAL)``` | Disables logging entirely |
