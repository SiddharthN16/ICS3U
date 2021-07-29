# TASK

Make a copy of your previous exercise and add appropriate logging throughout your code (function and main code).

Try to make use of different levels, in the following places:

- When variables change value
- When exceptions occur
- When significant events happen (function beginning/ending, loop exiting etc)
- Anywhere problems can occur!

Messages should be descriptive, such as:

```python

logging.info("Result is: " + str(result) + " after multiplying by: " + str(value))

```

not:

```python

logging.info(str(result))

```

You can either disable all logging OR log to a file.