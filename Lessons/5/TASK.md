# TASK

You will be writing the functions below.  **No input() or main code is needed - testing of functions will be done automatically (see below). **

Functions should be named *exactly* as given below.

## def milesToKm(distance):

Convert the given `distance` in miles to kilometres and `return` the result, rounded to two decimal places.  If the `distance` is a negative value, `return 'Error.'`.

- Use `1.60934` as the conversion factor
- Use `round(variable,2)` to round to 2 decimal places.  For example, `answer = round(answer,2)`.

## def saleCalc(price,discount):

Reduce the given `price` by the `discount` (given as a percentage like 20) and `return` the result, rounded to two decimal places.  If either parameter is negative, `return 'Error.'`.  If the discount is equal to or greater than 100, `return 'Error.'`



## Testing

When you run the test, each function is tested separately.  It should be clear in the console which function passed/failed the test.

If you failed, look closely at the last line (example):

`
AssertionError: 16 != 16.09
`

We will learn more about this error in a few days but the *left side* is what you returned, and the *right side* is what should have been returned.  In this case, you didn't round correctly!
