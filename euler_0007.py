"""

Problem 7: 10001st prime
------------------------

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""

from euler_util import get_nth_prime


def solve(n):
    return get_nth_prime(n)


def compute():
    n = 10001
    return solve(n)