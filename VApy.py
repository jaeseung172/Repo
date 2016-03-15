import re
from gazigazimodule import *
from BoxOfficeParser import * 
#from TodaySomething import * 
#from notesaver import *
string = input("How may I help you sir?\n(Nothing? Please Type exit)\n")
if 'note' in string:
	if bool(re.findall(r"myself (\D+)", string)) == True:
		Confirm = input("Note is %s \nRight?\n[Yes Or No]\n"% re.findall(r"myself (\D+)", string)[0])
		if Confirm == 'Yes':
			NoteSave(re.findall(r"myself (\D+)", string)[0])
		else:
			pass
	else:
		Confirm = input("Note is %s \nRight?\n[Yes Or No]\n" % re.findall(r"note about (\D+)", string)[0])
		if Confirm == 'Yes':
			NoteSave(re.findall(r"note about (\D+)", string)[0])
		else:
			pass
elif 'weather' in string:
	if 'tomorrow' in string:
		print("hmm...It'll be cold tomorrow\nYou Know Why? It's winter Season!")
	else:
		print("now you are asking about weather..")
elif 'show' in string:
	if 'rank' in string:
		if 'movie' in string:
			MovieSuggest()
#elif 'good' in string:
	#if indian in string:
elif 'Read' in string:
	if 'email' in string:
		# Four Function
		if 'about' in string:
			# Read_About_Module()
			print("Read Mail about....") 
		if 'from' in string:
			# It needs to find who.
			print("Read Mail from.....")
		if 'latest' in string:
			# It needs to find latest email
			print("Read Latest mail")
	if 'text' in string:
		# Two Function
		if 'from' in string:
			#Detect Using RE Module. 
			print("OK, I'll read text from whom")	
elif 'Call' in string:
	if 'taxi' in string:
		#CallTaxi()
		print("OK, I'll Call a taxi")
elif 'Flip' in string:
	if 'coin' in string:
		FliP_A_COiN()
elif 'yes' in string:
	if 'no' in string:
		YES_OR_NO()
	else:
		print("For What?")
elif 'Read' in string:
	if 'haiku' in string:
		print("It's Funny Haiku!")
	if 'news' in string:
		#NEWSDiGEST
		print("Nothing....\nWaiting for Next Update!")
elif 'Roll' in string:
	if 'dice' in string:
		Roll_A_Dice()
elif 'Learn' and 'pronounce' in string:
	PronounceName()
elif 'Happy' in string:
	if 'holiday' or 'christmas' or 'chuseok' or 'seollal' in string:
		#HoliDayCheck()
		print("Happy!")
elif 'schedule' and 'years' or 'month' or 'days' in string:
	Scheduler(string)
elif string == 'exit':
	exit()
else:
	print("Sorry, I didn't Recognize your Command\nDo you want to Search?")
