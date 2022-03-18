"""

All the utility functions that will be required in solving all the questions. They include Fibonacci numbers, prime numbers etc.

"""

import math


PI = 3.1415
E = 2.71828


def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans


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


def triangular_sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


def get_prime_divisors(n):
    if n==0:
        return set()
    elif n==1:
        return {1}
    ans = {1,n}
    i = 2
    while n>1:
        if n%i==0:
            n = n/i
            ans.add(i)
        else:
            i += 1
    return ans


def get_divisors_num(n):
    if n==1:
        return 1
    ans = 2
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            if i**2==0:
                ans += 1
            else:
                ans += 2
    return ans


def get_divisors(n):
    if n==1:
        return [1]
    ans = [1,n]
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            if i**2==0:
                ans.append(i)
            else:
                ans.append(i)
                ans.append(n//i)
    return ans


def numbers_to_words(n):
    memo = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fitty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"
    }
    if n==100 or n==1000:
        return "one" + memo[n]
    if n in memo:
        return memo[n]
    if n>99:
        if n%100==0:
            return memo[n//100] + memo[100]
        return memo[n//100] + memo[100] + "and" + numbers_to_words(n%100)
    return memo[n - (n%10)] + memo[n%10]

    