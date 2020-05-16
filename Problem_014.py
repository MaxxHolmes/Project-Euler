# Solution to Project Euler - Problem 14
# Longest Collatz Sequence by MaxxHolmes

# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest Collatz chain?
#______________________________________________________________________________

import time
start = time.time()

# First, define a function to find the Collatz Chain length.
# This can be done using a loop that ends when x becomes 1, and a counter

def collatz_chain_length(x):
	cc_len = 1
	while x != 1:
		if x % 2 == 0:
			x = x // 2
		else:
			x = x * 3 + 1
		cc_len += 1
	return cc_len

# Definine an answer parameter, and a chain length parameter allows us to keep track
# of the current highest solution without needing to store other chain lengths.

def solution():
	answer = 0
	chain_max = -1
	for i in range(1, 999992):
		chain = collatz_chain_length(i)
		if chain > chain_max:
			chain_max = chain
			answer = i

	return answer

print(solution())
print(start = time.time())