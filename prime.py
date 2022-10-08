#!/usr/bin/python3


from functools import reduce
from math import sqrt
def factors_1(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

import itertools
def isprime(n,lp):
    for i in lp:
        j = int(i)
        if n % j == 0:
            if j == n:
                return 1
            return j
    divs = range(1000001, int(n ** 0.5) + 1, 2)
    return [d for d in itertools.chain(divs[::3], divs[1::3]) if n % d == 0][0]


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
    q = 2
    
    while q<n:
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
            break
        
        
        q += 1



def factor(n, lp):
    if n in lp:
        return 1
    for j in lp:
        if n % j == 0:
            return j
    #lpi = [i for i in range (100001, int(n ** .5)+1) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]
    """for i in range (100000001, int(n ** .5)+1,2):
        if n % i == 0:
            return i
    divs = range(10000000, int(n ** 0.5) + 1, 2)
    l = [d for d in itertools.chain(divs[::3], divs[1::3]) if n % d == 0]
    if l != []:
        return l[0]
    k = 1666660
    while 6*k+1 <= int(n**0.5) + 1:
        if n % (6*k+1) == 0:
            return 6*k+1
        if n % (6*k-1) == 0:
            return 6*k-1
    
    if n > 10000000:
        #li=[(6*i+1, 6*i-1) for i in range(1666660, int((int(n**.5) + 1)/6) + 1) if (n % (6*i+1) == 0 or n % (6*i-1) == 0)]
        li = set(reduce(list.__add__,
                ((6*i+1, 6*i-1) for i in range(1666660, int((int(n**.5) + 1)/6) + 1) if (n % (6*i+1) == 0 or n % (6*i-1) == 0))))
        if li != {}:
            for i in li:
                if n % i == 0:
                    return i
    
    
    for i in range(1666660, int((int(n**.5) + 1)/6) + 1):
            if n % (6*i+1) == 0:
                return 6*i+1
            if n % (6*i-1) == 0:
                return 6*i-1
    """    
    return 1
def primef(n):
    if n <= 3:
        return int(n)
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    else:
        for i in range(5, int((n)**0.5) + 1, 6):
            if n % i == 0:
                return int(i)
            if n % (i + 2) == 0:
                return primef(n/(i+2))
    return int(n)
