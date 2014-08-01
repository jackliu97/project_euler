from sets import Set

def is_trivial(num, dem):

	if num == dem:
		return False


	num = Set(list(str(num)))
	dem = Set(list(str(dem)))

	print(num)
	print(dem)

	print(num.intersection(dem))



is_trivial(34, 54)