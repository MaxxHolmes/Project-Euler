# Solution to Project Euler - Problem 21
# Amicable Numbers by MaxxHolmes

# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

# Evaluate the sum of all the amicable numbers under 10000.
#______________________________________________________________________________

import time

start = time.time()

def solution():

	# First we create a table of the sum of proper divisors.
	# We compute this for each number 1 -> 10000 using the Sieve of Eratosthenes
	sums_of_divisors = [0] * 10000
	for i in range(1, len(sums_of_divisors)):
		for j in range(i*2, len(sums_of_divisors), i):
			sums_of_divisors[j] += i

	answer = 0
	for i in range(1, len(sums_of_divisors)):
		j = sums_of_divisors[i]
		if j != i and j < len(sums_of_divisors) and sums_of_divisors[j] == i:
			answer += i

	return answer

print(solution())
print(time.time() - start)