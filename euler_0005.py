"""

Problem 5: Smallest multiple
----------------------------

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

from euler_util import get_lcm


def solve(n):
    ans = 1
    for i in range(1, n+1):
        ans = get_lcm(ans, i)
    return ans



def compute():
    n = 20
    return solve(n)