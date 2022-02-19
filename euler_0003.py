"""

Problem 3: Largest prime factor
-------------------------------

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def solve(n):
    i = 2
    while n>1:
        if n%i==0:
            n = n//i
        i += 1
    return i-1


def compute():
    n = 600851475143
    return solve(n)