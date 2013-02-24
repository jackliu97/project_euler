seq = [1, 1,2];
while  len(str(seq[-1])) < 1000:
	i = seq[-1] + seq[-2]
	seq.append(i)
print(len(seq))