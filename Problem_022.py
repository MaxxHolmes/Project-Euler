# Solution to Project Euler - Problem 22
# Names Scores by MaxxHolmes

# Using p022_names.txt, a text file containing over 5000 first names,
# begin by sorting them into alphabetical order and then work out the alphabetical
# value for each name. Multiply these values by its alphabetical position and then
# sum the name scores for each name.
#______________________________________________________________________________

import time
start = time.time()

with open('p022_names.txt') as file: names = [x[1:-1] for x in file.read().strip().split(',')]
print(sum((i + 1) * (ord(c) - 64) for (i, name) in enumerate(sorted(names)) for c in name))

print(time.time() - start)