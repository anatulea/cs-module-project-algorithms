"""
We'll say that a positive int divides itself if every digit in the number
divides into the number evenly. So for example 128 divides itself since 1, 2,
and 8 all divide into 128 evenly. 
​
And we'll say that 0 does not divide into anything evenly, so no number with a
0 digit divides itself. 
​
Write a function to determine if a number divides itself.
​
Single integers only, no floating point or strings
Numbers can be negative or positive
​
Input: Single integer argument 
Return: Boolean, True if the number divides itself
​
"""


def divides_self(n):
    digits = list(str(n))
    for d in digits:
        if d == '0' or n % int(d) != 0:
            return False
# If we get to this line, the number is good:
    return True
print(divides_self(244))
print(divides_self(634))
