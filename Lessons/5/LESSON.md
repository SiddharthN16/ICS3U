# Notes (Functions)

Functions are used to encapsulate and organize reusable code that is used to perform a single action.  You have been using a function quite often throughout previous work: ```print()```.

Functions have a different structure from anything you've done previously, and we'll take this on step-by-step.  The basic setup of a function is as follows:

```python
def functionName( parameter1, parameter2, ... ):
    '''Description of what the function does

    '''
    # body of the function
    return expression
```

The above concepts break down as follows:
* ```def``` - Is required for you to **define** a function
* ```functionName``` - Is the name of the function.  The name of the function should be clear on its purpose.
* ```parameter#``` - Are different parameters that the function accepts.  These parameters are used inside the function, just as you would use variables.  This section can be left blank as well (i.e. ```def functionName():```).
* ```'''Description'''``` - This area is used to describe the purpose of the function.  We will go further in-depth on this in the future; however, for now you will only place a description in this section.
* ```body``` - This area is where the function does whatever the function is supposed to do (ideally a short task)
* ```return``` - This line will return back to where you called the function, or return a value to wherever the function is called.

Before being able to use a function, it must be defined.  As such, you will need to define functions at the top of a file, and then you can use them later.  `functions.py` will have some basic functions and usage.



**Notes:** 

- Any variables that are *created* inside a function **only exist inside that function.**
- functions should only use parameters to receive information (`input()` can be used to gather information prior to calling the function, but not *inside* the function)



