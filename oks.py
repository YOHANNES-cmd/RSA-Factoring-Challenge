"""lp = []
with open('2T_part1.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        for j in list(i.split()):
            lp.append(int(j))
with open("prime.txt", "w") as file:
    for i in lp:
        if i < 10000000:
            file.write(str(i)+",")
from functools import reduce
from math import sqrt
def factors_1(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
print(factors_1(2497885147362973))"""
import sys
def gen_primes(n):
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 9999991
    
    while q<n**.5:
        if q not in D:
                # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            #yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        if n % int(q) == 0:
                yield q
        q += 1

for i in gen_primes(2497885147362973):
    print(i)
    break
