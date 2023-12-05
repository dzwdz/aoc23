import sys

def listsplit(a, pred):
	res = [[]]
	for el in a:
		if pred(el):
			if res[-1] != []:
				res.append([])
		else:
			res[-1].append(el)
	if res[-1] == []:
		res = res[:-1]
	return res

lines = [s.strip() for s in sys.stdin.readlines()]
seeds, *maps = listsplit(lines, lambda x: x == '')
assert len(seeds) == 1
assert len(maps)  == 7
seeds = [int(n) for n in seeds[0].split()[1:]]
maps = [
	[
		[int(n) for n in ent.split()]
		for ent in m[1:]
	]
	for m in maps
]

def part1():
	def trans(n, m):
		for src, dst, size in m:
			idx = n - dst
			if 0 <= idx < size:
				return src + idx
		return n
	ns = seeds
	for m in maps:
		ns = [trans(n, m) for n in ns]
	return min(ns)

print(part1())
