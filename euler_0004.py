"""

Problem 4: Largest palindrome product
-------------------------------------

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""


from euler_util import check_palindrome_int


def solve(n):
    p = (10**n) - 1
    q = 10**(n-1)
    ans = 1
    for i in range(p, p-q, -1):
        for j in range(p, p-q, -1):
            if check_palindrome_int(i*j):
                ans = max(ans, i*j)
    return ans


def compute():
    n = 3
    return solve(n)