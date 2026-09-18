import re
input = input("Input: ")
emails = re.findall(r'[a-zA-Z!#\\$%&\'*+-/=?^_{|}~`]+@[a-zA-Z\-.]+\.(?:com|net|org)', input)
print(f"\nThis paragraph contains {len(emails)} emails:")
for i in emails:
	print(f"- {i}")
