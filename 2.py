from sys import stdin

lines = stdin.readlines()

def isSubset(a, b):
	for k, v in b.items():
		if k in a:
			if a[k] > b[k]:
				return False
	return True

def union(sets):
	res = dict()
	for s in sets:
		for k,v in s.items():
			if k not in res:
				res[k] = v
			else:
				res[k] = max(res[k], v)
	return res

def power(d):
	p = 1
	for k in ['red', 'green', 'blue']:
		if k not in d:
			return 0
		p *= d[k]
	return p

tally1 = 0
tally2 = 0

for line in lines:
	gid, line = line[5:].split(':')
	gid = int(gid)
	rounds = []
	for s in line.split(';'):
		amts = dict()
		for ent in s.split(','):
			amt, color = ent.split()
			assert color not in amts
			amts[color] = int(amt)
		rounds.append(amts)
	
	possible = True
	for roun in rounds:
		if not isSubset(roun, {'red': 12, 'green': 13, 'blue': 14}):
			possible = False
	if possible:
		tally1 += gid

	tally2 += power(union(rounds))
print(tally1)
print(tally2)
