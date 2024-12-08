
with open("carolus_rex_album.txt", 'r') as file:
	lines = file.read().split("\n")
	count = lines.count("")
	words = []
	check = 0
	unique_words = set()
	word_dict = {}
	translation_tab = str.maketrans("()", "  ")
	for i in range(count):
		lines.remove("")
	for line in lines:
		words = line.split(" ")
		check += len(words)
		# print(words)
		for word in words:
			word = word.lower().translate(translation_tab).replace(" ", "")
			if not word in unique_words:
				unique_words.add(word)
				word_dict[word] = 1
			else:
				word_dict[word] += 1

		# words.append(line.split(" "))
	print(check)
	print(len(unique_words))
	print(sorted(word_dict.items(), key=lambda x:x[1], reverse = True))