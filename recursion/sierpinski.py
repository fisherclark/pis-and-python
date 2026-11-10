def sierpinski(n, char):
	if n == 0:
		return char
	blank = " " * len(char) * (3**(n-1))
	final = ""
	for row in range(3**(n)):
		if row//(3**(n-1)) == 1:
			final += sierpinski(n-1, char).splitlines()[row % (3**(n-1))] + blank + sierpinski(n-1, char).splitlines()[row % (3**(n-1))]
		else:
			final += sierpinski(n-1, char).splitlines()[row % (3**(n-1))] * 3
		final += "\n"
	return final


print(sierpinski(3, "██"))
