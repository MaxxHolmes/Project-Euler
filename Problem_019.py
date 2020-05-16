# Solution to Project Euler - Problem 19
# Counting Sundays by MaxxHolmes

# 1 Jan 1900 was a Monday
# How many sundays fell on the first of the month during the 20th century?
#______________________________________________________________________________

import time

start = time.time()

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year_check(year):
	leap = True
	if year % 4 != 0:
		leap = False
	elif year % 100 != 0:
		leap = True
	elif year % 400 != 0:
		leap = False
	return leap

def sunday_counter():
	day = 2
	sunday_count = 0

	for year in range(1901, 2001):
		for m in range(len(months)):
			day += months[m]
			if leap_year_check(year) and m == 1:
				day += 1
			if day % 7 == 0:
				sunday_count += 1
	return sunday_count

print(sunday_counter())
print(time.time() - start)