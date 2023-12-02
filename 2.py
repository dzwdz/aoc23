from sys import stdin

lines = stdin.readlines()

def isSubset(a, b):
	for k, v in b.items():
		if k in a:
			if a[k] > b[k]:
				return False
	return True

tally1 = 0

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
print(tally1)
