import sys
from math import inf

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

def part2():
	# (start, end)
	cur = []
	for i in range(0, len(seeds), 2):
		cur.append((seeds[i], seeds[i]+seeds[i+1]))
	def overlap(a, b):
		r = (max(a[0], b[0]), min(a[1], b[1]))
		if r[0] < r[1]: return r
		return None
	def subtract(a, b):
		r = (a[0], min(a[1], b[0]))
		if r[0] < r[1]: yield r
		r = (max(a[0], b[1]), a[1])
		if r[0] < r[1]: yield r
	def trans(r, m):
		remainder = [r]
		for src, dst, size in m:
			# U
			rr = overlap(r, (dst, dst+size))
			if rr:
				off = src-dst
				rr = (rr[0]+off, rr[1]+off)
				yield rr

			# \
			oldrem = remainder
			remainder = []
			for rem in oldrem:
				remainder += subtract(rem, (dst, dst+size))
		for rem in remainder:
			yield rem
	
	def simplify(a):
		a.sort()
		res = []
		i = 0
		while i < len(a):
			r = a[i]
			i += 1
			while i < len(a) and r[1] >= a[i][0]:
				r = (r[0], max(r[1], a[i][1]))
				i += 1
			res.append(r)
		return res
	
	for m in maps:
		last = cur
		cur = []
		for r in last:
			for out in trans(r, m):
				cur.append(out)
		cur = simplify(cur)
	return cur[0][0]

print(part1())
print(part2())
