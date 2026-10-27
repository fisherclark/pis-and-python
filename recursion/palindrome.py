def is_palindrome(text):
	text = text.strip(" !@#$%^&*()_+-=~`{}[]|\\:;\"'<>,.?/").lower()
	if len(text) < 2:
		return True
	if text[0] == text[-1]:
		return is_palindrome(text[1:-1])
	else:
		return False

try:
	while True:
		text = input("Text: ")
		print(is_palindrome(text))
except KeyboardInterrupt:
	print("\n")
