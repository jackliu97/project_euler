
def process(n):
	if(n%2 == 0):
		return int(n/2)
	else:
		return int((3*n)+1)

def chain(num):
	count = 1
	while num !=1:
		num = process(num)
		count += 1
	return count

max_c = 0
max_starting = 0
for i in range(1, 1000001):
	x = chain(i)
	if(max_c < x):
		max_c = x
		max_starting = i

print(max_starting)