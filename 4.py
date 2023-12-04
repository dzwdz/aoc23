import sys
lines = sys.stdin.readlines()

tally1 = 0
for line in lines:
	i, line = line.split(': ')
	i = int(i.split()[-1])
	wins, mine = line.split('|')
	wins = [int(n) for n in wins.split()]
	mine = [int(n) for n in mine.split()]
	matches = [n for n in mine if n in wins]
	if matches:
		tally1 += 2 ** (len(matches) - 1)
print(tally1)
