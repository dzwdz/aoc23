import sys

lines = [s.strip() for s in sys.stdin.readlines()]
def getbounds(x, y):
	if 0 <= x < len(lines) and 0 <= y < len(lines[x]):
		return lines[x][y]
	return '.'
syms = set()
def issymbol(c):
	global syms
	b = not c.isdigit() and c != '.'
	return b

tally1 = 0
for x, line in enumerate(lines):
	num = 0
	adj = False
	mid = False
	for y, c in enumerate(line):
		if c.isdigit():
			mid = True
			num = num * 10 + int(c)
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					adj = adj or issymbol(getbounds(x+dx, y+dy))
		elif mid:
			if adj: tally1 += num
			num = 0
			adj = False
			mid = False
	if adj: tally1 += num
print(tally1)
