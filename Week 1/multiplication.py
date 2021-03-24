"""Implementation of two multiplication algorithms"""
"""As of now, they only multiply two numbers of the same (even) length"""


def recursive(x, y):

	n = len(str(x))
	if n == 1:
		return x * y

	else:
		half = n//2
		str_x = str(x)
		str_y = str(y)

		n = len(str_x)

		a = int(str_x[:half])
		b = int(str_x[half:])

		c = int(str_y[:half])
		d = int(str_y[half:])

		ac = recursive(a, c)
		ad = recursive(a, d)
		bc = recursive(b, c)
		bd = recursive(b, d)

		xy = 10 ** n * ac + 10 ** half * (ad + bc) + bd

		return xy

def karatsuba(x, y):
	n = len(str(x))
	if n == 1:
		return x * y

	else:
		half = n//2
		str_x = str(x)
		str_y = str(y)

		n = len(str_x)

		a = int(str_x[:half])
		b = int(str_x[half:])

		c = int(str_y[:half])
		d = int(str_y[half:])

		ac = karatsuba(a, c)
		bd = karatsuba(b, d)
	
		apb = a + b
		cpd = c + d
		temp = karatsuba(apb, cpd)
		adpbc = temp - ac - bd

		xy = 10 ** n * ac + 10 ** half * adpbc + bd

		return xy

