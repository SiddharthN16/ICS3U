# Notes (Documentation)

*"Code is more often read than written."* -- Guido van Rossum (creator of Python).

Programmers rarely work alone - they work as a team, fix each other's code etc.  It's important to make sure that the purpose of your code can be understood by someone else.  So far we have used comments (`#`) to explain the purpose of our code.

On your next assignment, you'll be assessed on how clearly your comments explain your code.

## Function Documentation

A good function is one that you could copy into another program and be able to use.  The `saleCalc()` function could be implemented into your previous assignment easily.

Because of this, we want to make sure that anyone looking at (or using) our functions can clearly see what it requires, what it returns and what could go wrong.  We will be using the following standard documentation for our functions:

```python
'''
  Short summary of the use of the function
  
  Longer description of the use of the function.  This is an area where you can 
  expand on the short summary.

  Parameters
  ----------
  parameter1 : type
    description of parameter1
  parameter2 : type
    description of parameter2
  (as many as needed)
  
  Returns
  -------
  type
    description of what's being returned
  
  Warnings (this section is optional)
  --------
  This is a free-text area that describes any warnings that could propogate
  in this program

  Raises (this section is only applicable if your function raises an exception)
  ------
  ExceptionType
    Describe why/how this exception gets raised
  '''
```

This will be placed immediately after we define our functions, before the actual code.

We will now modify the previous lesson's code to include proper documentation.





