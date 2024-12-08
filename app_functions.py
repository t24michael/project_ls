from translator import translator


def levenshteinRecursive(str1, str2, m, n):
	# str1 is empty
	if m == 0:
		return n
	# str2 is empty
	if n == 0:
		return m
	if str1[m - 1] == str2[n - 1]:
		return levenshteinRecursive(str1, str2, m - 1, n - 1)
	return 1 + min(
		# Insert
		levenshteinRecursive(str1, str2, m, n - 1),
		min(
			# Remove
			levenshteinRecursive(str1, str2, m - 1, n),
			# Replace
			levenshteinRecursive(str1, str2, m - 1, n - 1))
	)


class functions(translator):
	def __init__(self, file, lang, voice, wpm):
		super().__init__(voice, wpm)
		self.file = file
		self.lang = lang
		self.input_line = None
		self.text_line_list = None
		self.translation_table = str.maketrans("äåö", "aao")
		self.properties()

	def reader(self):
		with open(self.file, 'r') as file:
			line_sv = file.read().replace("\n", ". ").split(". ")
			print(line_sv)
			count = 0
			for i in line_sv:
				count += 1
				try:
					x = self.trans.translate(i, dest=self.lang)

					print(f"{count} {self.voice}: {i}")
					print(f"{count} {self.lang}: {x.text}\n")

					self.engine.say(i)
					self.engine.runAndWait()
				except Exception as e:
					pass

	def compare(self, a, b, line):
		# you can implement a scoring system based on typos
		# and missing diacritics

		# you can add padding to sentences to make them equal
		# in length, but you need to be careful because
		# the sentences can be in equal in length
		# but the words different
		if len(a) == len(b):
			for i in range(len(a)):
				if len(a[i]) != len(b[i]):
					# checks for typos
					distance = levenshteinRecursive(a[i], b[i], len(a[i]), len(b[i]))
					if distance <= 2 <= len(a[i]):
						# if it's just a typo point it out then continue
						print(f"You have a typo: {b[i]} => {a[i]} ")
					else:
						# if the word is just wrong, restart the sentence
						# maybe store the wrong words in an array instead
						# idk, think more about this
						print(f"The word is wrong. {b[i]} != {a[i]}")
						return False
				elif a[i] != b[i]:
					#check for diacritics, show the mistake then proceed
					initial_word = a[i]
					a[i] = a[i].translate(self.translation_table)
					print(f"Pay attention to diacritics! {a[i]} => {initial_word}")
			print(f"Correct sentence: {line}")
			return True
		else:
			print("You did not type the same sentence!")
			return False

	def writing_exercise(self):
		with open(self.file, 'r') as file:
			self.text_line_list = file.read().split(". ")
			count = 0

			for line in self.text_line_list:
				line_list = line.split(" ")
				count += 1
				print(line)

				while True:
					try:
						self.engine.say(line)
						self.engine.runAndWait()
					except Exception as e:
						pass

					self.input_line = input("Type what you heard: ")
					input_line_list = self.input_line.split(" ")

					if self.compare(line_list, input_line_list, line):
						print("Correct!")
						break
