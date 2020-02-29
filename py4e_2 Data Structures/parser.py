fname = 'words.txt'
fhandle = open(fname)
fileread = fhandle.read()

# make list of all words then count them into a dictionary
wordsDict = dict()
wordsAll = fileread.rstrip().lower().split()
for word in wordsAll:
    wordsDict[word] = wordsDict.get(word, 0) + 1

# strip text into single string, make list of all characters, count them into dictionary
lettersDict = dict()
lettersAll = fileread.replace(' ','').replace('\n','')
lettersAll = list(lettersAll)
for letter in lettersAll:
    lettersDict[letter] = lettersDict.get(letter, 0) + 1

# ipnut word and query instances from wordsDict. Search is case-neutral.
queryWord = input("What word do you want to count? ")
queryWord = queryWord.lower()
if queryWord in wordsDict :
    queryWordCount = wordsDict[queryWord]
    print("The word \""+queryWord+"\" appears",queryWordCount,"times in \""+fname+"\"")
else:
    print("The word \""+queryWord+"\" appears 0 times in \""+fname+"\"")

# count each vowel and print
vowels = ['a','e','i','o','u']
for vowel in vowels:
    vowelCount = lettersDict[vowel]
    print("The vowel \"" + vowel + "\" appears",vowelCount,"times in \""+fname+"\"")