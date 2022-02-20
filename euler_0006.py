"""

Problem 5: Sum square difference
--------------------------------

The sum of the squares of the first ten natural numbers is, 
        (1^2) + (2^2) + (3^2)... + (10^2) = 385

The square of the sum of the first ten natural numbers is,
        (1 + 2 + 3.... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
        3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""


def solve(n):
    a = 0
    b = 0
    for i in range(1, n+1):
        a += (i*i)
        b += i
    return abs(a - (b*b))


def compute():
    n = 100
    return solve(n)
