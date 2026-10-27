def collatz(n):
	if n == 1:
		return 0
	else:
		if n % 2 == 0:
			return collatz(n//2)+1
		else:
			return collatz(3*n+1)+1
n = "0"
while n.isnumeric():
	n = input("Number: ")
	if n.isnumeric():
		print(f"{collatz(int(n))} steps")
