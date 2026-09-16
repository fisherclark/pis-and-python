target_words = ["james", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]

text = input("Text: ")
word = ""
classified = ""
word_endings = [" ",".","?","!",","]
for i in range(len(text)):
	word += text[i]
	if text[i] in word_endings or i == len(text)-1:
		wordin = False
		for j in word_endings:
			if word.lower().strip(j) in target_words:
				classified += "[REDACTED]" + j
				wordin = True
				break
		if not wordin:
			classified += word
		word = ""
print(classified)
