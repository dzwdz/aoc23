import sys
lines = sys.stdin.readlines()

tally1 = 0
counts = [1] * len(lines)
for i, line in enumerate(lines):
	_, line = line.split(': ')
	#i = int(i.split()[-1])
	wins, mine = line.split('|')
	wins = [int(n) for n in wins.split()]
	mine = [int(n) for n in mine.split()]
	matches = [n for n in mine if n in wins]
	if matches:
		tally1 += 2 ** (len(matches) - 1)
	for j in range(len(matches)):
		if i+j+1 < len(counts):
			counts[i+j+1] += counts[i]
print(tally1)
print(sum(counts))
