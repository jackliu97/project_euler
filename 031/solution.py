#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# a = 1p 	0 - 200
# b = 2p 	0 - 100
# c = 5p 	0 - 40
# d = 10p	0 - 20
# e = 20p   0 - 10
# f = 50p	0 - 4
# g = 100p	0 - 2
# h = 200p  0 - 1
import math
x = 0
mx = 200
for h in range(0, 2):
	_g = (mx - 200*h)/100
	for g in range(0, math.ceil(_g) + 1):
		_f = (mx - 200* h - 100*g)/50
		for f in range(0, math.ceil(_f) + 1):
			_e = (mx - 200* h - 100*g - 50*f)/20
			for e in range(0, math.ceil(_e) + 1):
				_d = (mx - 200* h - 100*g - 50*f - 20*e)/10
				for d in range(0, math.ceil(_d) + 1):
					_c = (mx - 200* h - 100*g - 50*f - 20*e - 10*d)/5
					for c in range(0, math.ceil(_c) + 1):
						_b = (mx - 200* h - 100*g - 50*f - 20*e - 10*d - 5*c)/2
						for b in range(0, math.ceil(_b) + 1):
							_a = mx - 200* h - 100*g - 50*f - 20*e - 10*d - 5*c - 2*b + 1
							for a in range(0, _a):
								if (a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h) == mx:
									x += 1

print(x)
