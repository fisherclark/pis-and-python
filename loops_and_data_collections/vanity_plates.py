def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid, enter valid plate")
        main()


def is_valid(s):
	if not (len(s) <= 6 and len(s) >= 2):
		return False
	if not s.isalnum():
		return False
	if not s[0:2].isalpha():
		return False
	numyet = False
	for i in s:
		if i.isnumeric() and not numyet:
			if i == "0":
				return False
			numyet = True
		if i.isalpha() and numyet:
			return False
	return True

main()
