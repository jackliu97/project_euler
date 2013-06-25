inp_str = open("triangle.txt","r")

inp_list = []

for x in inp_str:
	inp_list.append([int(y) for y in x.split()])

ps = inp_list.pop() #previous sums
def process(prev, curr):
	new_sum = []
	ind = 0
	curr.reverse()
	while len(curr):
		new_sum.append(curr.pop() + max(prev[ind], prev[ind+1]))
		ind += 1
	return new_sum

for i in reversed(inp_list):
	ps = process(ps, i)
print(ps.pop())