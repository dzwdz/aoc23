# part 1:
# could be done much faster by solving a quadratic equation
# i could also just use python's builtin binary search
# but where's the fun in that?

import sys
from math import *
lines = sys.stdin.readlines()

races = list(zip(*[[int(n) for n in line.split()[1:]] for line in lines]))

def binsearch(lim, pred):
	i = 0   # i   is false
	j = lim # j   is true
	if pred(0): return 0
	if not pred(lim-1): return lim
	while i + 1 < j:
		assert not pred(i)
		assert j == lim or pred(j)
		mid = (i+j)//2
		assert mid < lim
		if pred(mid):
			j = mid
		else:
		 	i = mid
	assert not pred(i)
	assert i + 1 == j
	assert pred(j)
	return j

def count(total, best):
	smallest = binsearch(total//2, lambda x: best < (total-x)*x)
	upper = total - smallest
	#print(total, best, smallest, upper)
	return upper - smallest + 1

tally1 = 1
for race in races:
	tally1 *= count(*race)
print(tally1)

race = [
	int(''.join([c for c in line.split(maxsplit=1)[1] if c.isdigit()]))
	for line in lines
]
print(count(*race))
