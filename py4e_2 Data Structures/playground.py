fname = 'words.txt'
fhand = open(fname)

# dictionary each words
wordCounts = dict()
for line in open(fname):
    words = line.rstrip().lower().split()
    for word in words:
        wordCounts[word] = wordCounts.get(word, 0) + 1

# dictionary each letter
letterCounts = dict()
for line in open(fname):
    letters = line.lower().replace(' ','')
    letters = list(letters)

    
    for letter in letters: 
        letterCounts[letter] = letterCounts.get(letter, 0) + 1
print(letterCounts)

"""
# query instances of a word
queryWord = "the" #input("What word do you want to count? ")
queryWord = queryWord.lower()
if queryWord in wordCounts:
    queryWordCount = wordCounts[queryWord]
    print("The word \""+queryWord+"\" appears",queryWordCount,"times in \""+fname+"\"")
else:
    print("The word \""+queryWord+"\" appears 0 times in \""+fname+"\"")

# count each vowel
vowels = ['a','e','i','o','u']
for vowel in vowels:
    if vowel in letterCounts:
        vowelCount = letterCounts[vowel]
        print("The vowel \"" + vowel + "\" appears",vowelCount,"times in \""+fhand+"\"")
"""