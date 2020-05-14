# Solution to Project Euler - Problem 10
# Summation of Primes by MaxxHolmes

# Find the sum of all the primes below two million
#_____________________________________________________________________

import time
start = time.time()

# We can use the ancient algorithm the "Sieve of Eratosthenes"
# Just like in question 7. This time we are given the upper limit 2000000

def SumOfSieveOfEratosthenes(n):

	# Create a boolean array from 2 to n with all entries being true.
	# Update all multiples of any prime found as False, and identify
	# the rest as true!
	
	answer = 0
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
			answer += p

	return answer

print(SumOfSieveOfEratosthenes(2000000))
print(time.time() - start)