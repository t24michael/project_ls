from pypdf import PdfReader
import os
location = os.path.abspath("PDFs/1984.pdf")
print(location)
reader = PdfReader(location)


# for page in reader.pages:
# 	x = page.extract_text()
# 	with open("1984.txt", "a") as file:
# 		file.writelines(x)

with open("1984.txt", 'r') as file:
	lines = file.readlines()
	print(lines)
	for i,line in enumerate(lines):
		if line.find("Free eBooks at Planet eBook.com") != -1:
			lines[i] = line.replace("Free eBooks at Planet eBook.com", "")
		elif line.find("Free eBooks at Planet eBook.com") != -1:
			lines[i] = line.replace("Free eBooks at Planet eBook.com", "")
		elif line.find("") != -1:
			lines[i] = line.replace("", "")
	with open("1984.txt", "w") as file:
		file.writelines(lines)

