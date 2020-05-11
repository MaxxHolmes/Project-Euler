# Solution to Project Euler - Problem 2
# MaxxHolmes

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
#___________________________________________________________________________

# We can use the Fundamental Theorem of Numbers.
# Check out #WebsiteLinkHere for the full explanation for this solution!

import numpy as np

def smallest_prime(n):

	square_root = int(np.sqrt(n))
	for i in range(3, square_root + 1):
		if n % i == 0:
			return i
	return n

def solution():
	p = 3
	n = 600851475143
	while p < n:
		p = smallest_prime(int(n))
		if p < n:
			n = n // p
	else:
		return str(n)

print(solution())