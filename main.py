# must install tabulate with pip or this won't work
from tabulate import tabulate
from itertools import tee, islice, chain

def seq(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

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

full_table = list(table)
function = choice = None

while choice != 4:
	print("\n1 - Print truth table (vars only)\
		\n2 - Add or change function\
		\n3 - Print full truth table\
		\n4 - Exit")
	
	while True:
		try:
			choice = int(input(""))
			if choice < 1 or choice > 4: print("ERROR: Invalid option")
			else: break
		except: print("ERROR: Enter a number")

	if choice == 1: print("\n" + tabulate(table))

	elif choice == 2:
		print("\nEnter a function in SoP form only.\
			\nUse ! to indicate a bar.\
			\nExample format: F(x,y,z) = xy + y!z + !x!z")
		function = input(f"F{vars} = ")
		terms = function.split(" + ")
		good_input = True
		for term in terms:
			for char in term:
				if (not char.isalpha() and char != "!") or (not char in vars and char != "!" or (char == "!" and term.index(char) == len(term)-1)):
					print("ERROR: Invalid function")
					function = None
					good_input = False
					break
				else: continue
				break
		if good_input:
			filtered_list = list(terms)
			for term in filtered_list:
				if not term.isalpha():
					filtered_list[filtered_list.index(term)] = "".join(list(filter(lambda x: x.isalpha(), term)))
			value = [[True] * len(term) for term in filtered_list]

			for term in terms:
				for p, char, n in seq(term):
					if char == "!":
						i = terms.index(term)
						value[i][filtered_list[i].index(n)] = False

			full_table[0] += terms
			# wip

	elif choice == 3:
		if function == None: print("\nERROR: Enter a function first")
		else: print(tabulate(full_table))