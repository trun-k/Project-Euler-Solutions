"""

Problem 10: Summation of primes
-------------------------------

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from euler_util import get_primes


def solve(n):
    primes = get_primes(n)
    sum = 0
    for i in primes:
        sum += i
    return sum


def compute():
    n = 2000000
    return solve(n)