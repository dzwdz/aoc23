import sys
import collections

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

adjs = collections.defaultdict(list)
tally1 = 0
for x, line in enumerate(lines):
	num = 0
	mid = False
	close = set()
	for y, c in enumerate(line + "."):
		if c.isdigit():
			mid = True
			num = num * 10 + int(c)
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					co = (x+dx, y+dy)
					if issymbol(getbounds(*co)):
						close.add(co)
		elif mid:
			if len(close) != 0: tally1 += num
			for point in close:
				adjs[point].append(num)
			num = 0
			mid = False
			close = set()
print(tally1)
print(sum([v[0] * v[1] for k, v in adjs.items() if len(v) == 2]))
