# Solution to Project Euler - Problem 16
# Power Digit Sum by MaxxHolmes

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
#______________________________________________________________________________

# Calculate 2^1000, turn it into a string and sum the digits.

import time

start = time.time()

number = 2**1000
answer = sum(int(digit) for digit in str(number))

print(answer)
print(time.time() - start)