# Day One

You cannot pipe Python programs with `head` or `tail` without getting a nasty error. You can avoid this by requiring: 

```python
from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE, SIG_DFL)
```

You can make sublists with a nice range syntax:

```python

INPUT = [1, 2, 3]

# get tail of list [2, 3]
INPUT[1:]

# get first two items [1, 2]
INPUT[0:2]
```

# Day Two

tuples are quite nice for a simple data structure which you can destructure:

```python
input = [("forward", 5), ("down", 5)]
for direction, amount in input:
    print(direction)

```

lambdas cannot be multiline: https://stackoverflow.com/questions/1233448/no-multiline-lambda-in-python-why-not