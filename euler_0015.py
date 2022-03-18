"""
Problem 15: Lattice paths
-------------------------

Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?

"""

memo = {}

def solve(m,n):
    if m==1 and n==1:
        return 0
    elif m==1 or n==1:
        return 1
    if (m,n) in memo or (n,m) in memo:
        return memo[(m,n)]
    memo[(m,n)] = solve(m-1, n) + solve(m, n-1)
    memo[(n,m)] = memo[(m,n)]
    return memo[(m,n)]
    

def compute():
    m,n = 20,20
    return solve(m+1, n+1)