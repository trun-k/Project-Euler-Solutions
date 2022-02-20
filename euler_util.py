"""

All the utility functions that will be required in solving all the questions. They include Fibonacci numbers, prime numbers etc.

"""

import math


PI = 3.1415
E = 2.71828


def ln(n):
    return math.log(n)/math.log(E)


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


def get_primes(n):
    sieve = []
    for i in range(n+1):
        sieve.append(True)
    sieve[0] = False
    sieve[1] = False
    for i in range(2,int(math.sqrt(n))+1):
        for j in range(i*i, n+1, i):
            sieve[j] = False
    primes = []
    for i in range(n+1):
        if sieve[i]:
            primes.append(i)
    return primes


def get_nth_prime(n):
    p = math.ceil(n*(ln(n) + ln(ln(n))))
    primes = get_primes(p)
    return primes[n-1]