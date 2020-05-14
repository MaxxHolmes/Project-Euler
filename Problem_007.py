# Solution to Project Euler - Problem 7
# 10001st Prime by MaxxHolmes

# The first 6 prime numbers are 2, 3, 5, 7, 11 and 13.
# What is the 10001st prime?
#_____________________________________________________________________

import time
start = time.time()

# We can use the ancient algorithm the "Sieve of Eratosthenes"
# This marks all multiples of primes as composite, to find all primes
# up to some upper limit m.

# We need the math library for the math.log function, the natural log
# and math.ceil, which rounds up to the next integer
import math

def upper_bound_for_nth_prime(n):
	return (n * (math.log(n) + math.log(math.log(n))))

def SieveOfEratosthenes(n):

	# Create a boolean array from 2 to n with all entries being true.
	# Update all multiples of any prime found as False, and identify
	# the rest as true!
	sieve = []
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):

		if (prime[p] == True):
			for i in range(p * 2, n + 1, p):
				prime[i] = False

		p += 1
	prime[0] = False
	prime[1] = False
	# Add all primes to array
	for p in range(n+1):
		if prime[p]:
			sieve.append(p)

	return sieve

upper_bound = math.ceil(upper_bound_for_nth_prime(10001))
primes = SieveOfEratosthenes(upper_bound)
print(primes[10000])
print(time.time() - start)
