"""
Problem 21: Amicable numbers
----------------------------


Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

from euler_util import get_divisors


def solve(n):
    memo = {}
    for i in range(1, n+1):
        memo[i] = sum(get_divisors(i))-i
    ans = 0
    for i in range(1, n+1):
        if memo[i] in memo and i!=memo[i] and i==memo[memo[i]]:
            ans += i
    return ans


def compute():
    n = 10000
    return solve(n)