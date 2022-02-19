"""

All the utility functions that will be required in solving all the questions. They include Fibonacci numbers, prime numbers etc.

"""

import math


def get_lcm(a, b):
    return (a*b)//(math.gcd(a,b))


def check_palindrome(s):
    for i in range(len(s)):
        if s[i]!=s[-i-1]:
            return False
    return True


def check_palindrome_int(n):
    a = str(n)
    return check_palindrome(a)