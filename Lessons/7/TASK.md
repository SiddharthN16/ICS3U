# TASK

Make a copy of your previous exercise (`milesToKm()` / `saleCalc()` functions and main code) and make the following modifications:

## raise

Modify both functions (even if you didn't use both) to `raise` appropriate exceptions:

- parameters are not correct type (`TypeError`).  This should happen *first*.
- parameters are incorrect values (`ValueError`).

You should only have one `return` type now - the calculation.

## try/except

Modify your main code to make use of `try` and `except`:

- when you call the function(s) (that now raise exceptions)
- whenever another exception could occur that crashes your program (converting an input to int for example)

Previously I told you that I would input a number if that's what you asked for - not anymore!  We can use `try` and `except` to deal with that!

**Note:** we want to use `try` *any time* we run some code that *has the possibility* of raising an exception - even if we account for it in the main code.


