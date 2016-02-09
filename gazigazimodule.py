import random
def PronounceName():
	FirstName = ""
	Question1 = input("Do you have a First name?\n(No? Just say No)\n")
	if Question1 == "No":
		pass
	else:
		FirstName = Question1
	LastName = ""
	Question2 = input("Do you have a Middle or Last name?\n(No? Just say No)\n")
	if Question2 == "No":
		pass
	else:
		LastName = Question2
	IsITRightQ = input("Hmm...\nYour name is %s %s\nIs it Right? [YES OR NO]\n" % (LastName, FirstName))
	if IsITRightQ == "YES":
		print("SAVED")
	else:
		print("DENIED")

def YES_OR_NO():
	YES_OR_NO = ['YES', 'NO']
	print(random.choice(YES_OR_NO))

def Roll_A_Dice():
	dice = range(1, 7)
	print(random.choice(dice))

def FliP_A_COiN():
	coin_flipping = ['Head', 'Tail']
	print("It's %s" % (random.choice(coin_flipping)))
