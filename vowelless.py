#Takes a word or list of words as input
#Removes all the vowels
#Returns the word/sentence

print("Give me a word and I'll remove the vowels!")

def removeVowels(word):
	wordList = list(word)
	for item in wordList:
		if item == 'a' or item == 'e' or item == 'i' or item == 'o' or item == 'u':
			wordList.remove(item)	
	return wordList

def returnList(noVowelList):
	print(''.join(noVowelList))

word = raw_input("> ")
returnList(removeVowels(word))


