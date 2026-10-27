def draw_pattern(n):
	if n == 1:
		print("*")
		return
	row = ""
	for i in range(n):
		row += "*"
	print(row)
	draw_pattern(n-1)
	print(row)

draw_pattern(94)
