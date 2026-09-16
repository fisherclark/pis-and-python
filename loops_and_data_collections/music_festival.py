musicians = []
musician_numbers = []
entered = ""

try:
	while entered != "Done":
		entered = input("Enter a musician: ").strip().title()
		if not entered == "Done":
			if entered in musicians:
				musician_numbers[musicians.index(entered)] += 1
			else:
				musicians.append(entered)
				musician_numbers.append(1)
except EOFError:
	print("")

print("")

for musician in sorted(musicians):
	votes = musician_numbers[musicians.index(musician)]
	if votes == 1:
		print(f"{musician}: 1 vote")
	else:
		print(f"{musician}: {votes} votes")

