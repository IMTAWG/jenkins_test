#!/usr/bin/env python2.7
# Program to calculate a random number of prime numbers in the range of 1000th prime to 10000th prime
# Andrew Ginns for Cathay Pacific
# 28.06.2017


import time
from random import randint

now = time.strftime("%Y-%m-%d-%H-%M")
start = time.time()
n = randint(1000, 10000)
f1 = open("out-%s.txt" % now, "w")

for p in range(2, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print '\n%s' % p,
        l = p

end = time.time()
total = end - start

print '\nTotal time taken is %s seconds\n' % total
f1.write('\nThe file was created at %s in the format Year-Month-Day-Hour-Minute' % now)
f1.write('\nThe prime number closest to %s is %s\nTotal time taken is %s seconds\n' % (n, l, total))
f1.close()

f2 = open("out-%s.txt" % now)
print f2.read()
