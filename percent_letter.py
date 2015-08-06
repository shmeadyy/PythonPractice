user_string = raw_input("What's your word?")
user_num = raw_input("What's your number?")

#try tells python to try the following code in the block
try:
	our_num = int(user_num)
#but if that code fails to make the string into an integer (because it's a float, for example), then run the following block of code
except:
	our_num = float(user_num)

#in wants python to check to see if the '.' is in the user_num (checking for a float)
if not '.' in user_num:
	print(user_string[our_num])
else:
	#len is getting the length of the string
	ratio = round(len(user_string)*our_num)
	#user_string[ratio] is getting the index from user_string
	print(user_string[ratio])

	