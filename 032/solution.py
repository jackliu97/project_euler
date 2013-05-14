x = []
for i in range(1, 100):
	for j in range(100, int(9999/i)):
		k = i*j
		if sorted([int(i) for i in '%s%s%s'%(i,j,k)]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
			x.append(k)

print(sum(set(x)))