# Solution to Project Euler - Problem 17
# Power Digit Sum by MaxxHolmes

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
#______________________________________________________________________________

def number_in_english(n, ones, tens):
	if 0 <= n < 20:
		return ones[n]
	elif 20 <= n < 100:
		return tens[n // 10] + (ones[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return ones[n // 100] + "hundred" + (("and" + number_in_english((n % 100), ones, tens)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return number_in_english((n // 1000), ones, tens) + "thousand" + (number_in_english((n % 1000), ones, tens) if (n % 1000 != 0) else "")
	else:
		raise ValueError()

def solution(ones, tens):
	answer = sum(len(number_in_english(i, ones, tens)) for i in range(1, 1001))
	return answer


ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


print(solution(ones, tens))