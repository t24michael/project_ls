from app_functions import functions

func = functions("swedish.txt","en", "swedish", 170)

x = int(input("What do you want to do today? 1-Listening, 2-Writing"))

if x == 1:
	func.reader()
elif x == 2:
	func.writing_exercise()

