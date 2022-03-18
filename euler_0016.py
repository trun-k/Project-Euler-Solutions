"""
Problem 16: Power digit sum
---------------------------

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""


def solve(n):
    num = 2**n
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum


def compute():
    n = 1000
    return solve(n)