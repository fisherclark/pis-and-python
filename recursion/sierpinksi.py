def sierpinski(n):
	if n == 0:
		return "#"
	blank = ""
	for i in range(3**(n-1)):
		blank += " "
	final = ""
	for row in range(3**(n)):
		if row//(3**(n-1)) == 1:
			final += sierpinski(n-1).splitlines()[row % (3**(n-1))] + blank + sierpinski(n-1).splitlines()[row % (3**(n-1))]
		else:
			final += sierpinski(n-1).splitlines()[row % (3**(n-1))] + sierpinski(n-1).splitlines()[row % (3**(n-1))] + sierpinski(n-1).splitlines()[row % (3**(n-1))]
		final += "\n"
	return final


print(sierpinski(4))
