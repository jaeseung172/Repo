# -*- coding: cp949 -*-
import re
from gazigazimodule import *
from BoxOfficeParser import *
#from TodaySomething import *
string = input("How may I help you sir?\n(Nothing? Please Type exit)\n")
if 'note' in string:
	if 'myself' in string:
		print("Yes! I Already Taken!")
elif 'weather' in string:
	if 'tomorrow' in string:
		print("hmm...It'll be cold tomorrow\nYou Know Why? It's winter Season!")
	else:
		print("now you are asking about weather..")
elif 'show' in string:
	if 'rank' in string:
		if 'movie' in string:
			MovieSuggestion()
		if 'music' in string:
			print("hmm... i don't Know!! Sorry!\n(But You don't like nowaday's music!)")
elif 'flip' in string:
	if 'coin' in string:
		FliP_A_COiN()
elif 'yes' in string:
	if 'no' in string:
		YES_OR_NO()
	else:
		print("For What?")
elif 'read' in string:
	if 'haiku' in string:
		print("It's Funny Haiku!")
	if 'news' in string:
		#NEWSDiGEST
		print("Nothing....\nWaiting for Next Update!")
elif 'roll' in string:
	if 'dice' in string:
		Roll_A_Dice()
elif 'learn' and 'pronounce' in string:
	PronounceName()
elif string == 'exit':
	exit()
else:
	print("")