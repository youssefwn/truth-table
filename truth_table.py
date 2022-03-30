from tabulate import tabulate

vars = list(filter(lambda x: x.isalpha(), input("Enter variables: ")))
n = len(vars)
ns = 2**n
table = [[] for _ in range(ns)]

for i in range(n):
	j = 0
	current = False
	for k in table:
		if j < ns/(2**(i+1)): k.append(int(current))
		else:
			current = not current
			k.append(int(current))
			j = 0
		j += 1

table.insert(0, vars)
print(tabulate(table))