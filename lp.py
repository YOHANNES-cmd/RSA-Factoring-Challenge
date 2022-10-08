#!/usr/bin/python3
from random import randint
import sys
from prime import factor, isprime

lp = []
with open("prime.txt", 'r') as file:
        for line in file:
            lp=line[:-1].split(",")
            break
lp = list(map(int, lp))
def gcd(a, b):
    """ Returns the greatest common divisor of the two numbers
    """
    while b:
        a, b = b, a % b
    return a


def _pollard_brent_func(c, n, x):
    """ Return f(x) = (x^2 + c) % n
        Assume c < n
    """
    y = (x ** 2) % n + c
    if y >= n:
        y -= n

    assert 0 <= y < n
    return y


def brent_factorise(n, iterations=None):
    """ Perform Brent's variant of Pollard's rho factorization algorithm to
        attempt to find a non-trivial factor of the given number number, n.
        If iterations > 0, return None if no factors are found within its range
    """
    y, c, m = (randint(1, n - 1) for _ in range(3))
    r, q, g = 1, 1, 1
    i = 0
    while g == 1:
        x = y
        for _ in range(r):
            y = _pollard_brent_func(c, n, y)
        k = 0
        while k < r and g == 1:
            ys = y
            for _ in range(min(m, r - k)):
                y = _pollard_brent_func(c, n, y)
                q = (q * abs(x - y)) %  n
            g = gcd(q, n)
            k += m
        r *= 2
        if iterations:
            i += 1
            if i == iterations:
                return None

    if g == n:
        while True:
            ys = _pollard_brent_func(c, n, ys)
            g = gcd(abs(x - ys), n)
            if g > 1:
                break
    return g

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)
    lpi = []
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        for line in lines:
            lpi.append(int(line))
    for i in lpi:
        j = factor(i, lp)
        print("{}={:d}*{}".format(i,i//j,j))
