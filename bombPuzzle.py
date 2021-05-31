import json

possibilities = [
["a","b","d","q","r","e"],
["s","w","h","x","i","l"],
["u","w","z","t","g","l"],
["q","h","m","j","f","w"],
["s","b","l","t","z","c"]
]

passwords = ["about", "after", "again", "below", "could",
			 "every", "first", "found", "great", "house",
			 "large", "learn", "never", "other", "place",
			 "plant", "point", "right", "small", "sound",
			 "spell", "still", "study", "their", "there",
			 "these", "thing", "think", "three", "water",
			 "where", "which", "world", "would", "write"]

def printLetterDistributions(passwords):
	letterDictList = []
	for i in range(0,5):
		letterDict = {}
		for word in passwords:
			if word[i] in letterDict:
				letterDict[word[i]] += 1
			else:
				letterDict[word[i]] = 1
		letterDictList.append(letterDict)
	print(json.dumps(letterDictList, sort_keys=True, indent=4))

def getPossibilityRow(i=0):
	indexTextArray = ["first", "second", "third", "fourth", "fifth"]
	exampleTextArray = ["a b d q r e", "s w h x i l", "u w z t g l", "q h m j f w", "s b l t z c"]
	displayText = ('Please type all six possibilities for ' + indexTextArray[i] +
				  ' letter, separated by spaces:\n' + 
				   'ex: '+ exampleTextArray[i] +'\n' + 
				   '    ')
	row = input(displayText)
	return row.lstrip().rstrip().split()

def givenPossibilitiesFindPassword(possibilities=possibilities, passwords=passwords):
	wordSetList = []
	for i in range(0,5):
		wordSet = set()
		for password in passwords:
			for letter in possibilities[i]:
				if password[i] == letter:
					wordSet.add(password)
		wordSetList.append(wordSet)
	
	intersection = wordSetList[0]
	for i in range(1,4):
		intersection = intersection.intersection(wordSetList[i])
	
	for password in intersection:
		return password

if __name__ == "__main__":
	#printLetterDistributions(passwords)
	possibilities = []
	for i in range(0,5):
		possibilities.append(getPossibilityRow(i))
	password = givenPossibilitiesFindPassword(possibilities, passwords)
	print("The password is: " + password)
