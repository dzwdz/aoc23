from sys import stdin

tally = 0
lines = stdin.readlines()
for line in lines:
	digits = [c for c in line.strip() if c.isdigit()]
	if len(digits):
		cur = digits[0] + digits[-1]
		tally += int(cur)
print(tally)

english = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def findFirst(s):
	if s[0].isdigit():
		return int(s[0])
	for k, v in enumerate(english):
		k+=1
		if s[:len(v)] == v:
			return k
	return findFirst(s[1:])
def findLast(s):
	if s[-1].isdigit():
		return int(s[-1])
	for k, v in enumerate(english):
		k+=1
		if s[-len(v):] == v:
			return k
	return findLast(s[:-1])
tally = 0
for line in lines:
	tally += findFirst(line) * 10 + findLast(line)
print(tally)
