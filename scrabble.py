def alphabetize(a):
    return ''.join(sorted(a))

def alpha(fname):
	return ''.join(sorted(fname))
    
def anagram(n, j):
    if alphabetize(n)== alphabetize(j):
        print "it's an anagram"
    else:
        print "it's not an anagram"

def anagramlist(original):
    #create dictionary
    d = {}
    #add elements- keys are alphabetized words, values are a list of original words
    for w in original:
        a = alphabetize(w)
        if a in d:
            b = d[a]
            if w in b:
                continue
            else:
                d[a].append(w)
        else:
            d[a] = [w]
    z = d.values()
    o = []
    for y in z:
        if len(y) > 1:
            print y

#this function creates a dictionary where the keys are the alphabetized words and the values are a list of words that can be made witht that key
def scrabdictsort():
	import string
#	#create list of all the words from scrabble dictionary
	f= open('scrabbledictionary.txt')
	allwords = []
	#get rid of return character and lowercase everything
	for w in f:
		w = w[:-2]
		w = string.lower(w)
		allwords.append(w)
	#create dictionary
	d = {}
	for w in allwords:
		aword = alphabtize(w)
		#if aword is already in d append new word to list
		if aword in d:
			old = d[aword]
			#avoiding repeats
			if w in old:
				continue
			else:
				d[aword].append(w)
		#if word isn't in dictionary create a new entry
		else:
			d[aword]=[w]
	return d

#this function finds if any given word can be spelled with the set of letters where both of them are sorted alphabetically
def wordmatch(letters, word):
	#if word is empty string that means that word can be spelled with these letters
	if word == '':
		return True
	#if letters is empty string that means this word cannot be spelled with the given letters
	elif letters == '':
		return False
	#this part is using recursion to go through the letters string to see if they can be used to spell some given word
	else:
		#first character in word
		w1 = word[0]
		#first character in letters
		l1 = letters[0]
		#if the first characters match check to see if the second letters match
		if w1 ==l1:
			return wordmatch(letters[1:], word[1:])
		else:
			#if the first characters don't match AND the first character in letters is less than the first character in word, use recursion to check to see if the second character in letters matches the first character in word
			if l1 < w1:
				return wordmatch(letters[1:], word[:])
			#if the first characters don't match and the character in word is less than the character in letter, that word cannot be spelled with the letters
			if w1 < l1:
				return False

#this function is to go through of all the possible words in the world and return just the ones that can be spelled with the string letters
def scrabblefinder(letters):
	#first alphabetize the string given
	aletters = alphabetize(letters)
	d = scrabdictsort()
	#delete all the items that can't be spelled with letters
	for w in d.keys():
		if wordmatch(aletters, w) is False:
			del d[w]
	return d

#this function sorts all the words that can be spelled with letters (from scrabblefinder) and puts them in a new dictionary where the keys are the length of the words and the values are the words
def wordsort(letters):
	possiblewords = scrabblefinder(letters)
	sortedwords = {}
	for k in possiblewords.keys():
		#l is the length of any given key
		l = len(k)
		#if that entry already exists, add lists together
		if l in sortedwords:
			sortedwords[l] = sortedwords[l] + possiblewords[k]
		#if that entry doesn't exist, create a new one
		else:	
			sortedwords[l] = possiblewords[k]
	return sortedwords

#this function takes all the words you can make and presents them with longest to shortest
def scrabbler(letters):
	sortedwords = wordsort(letters)
	#start with the longest possible length m
	m = max(sortedwords.keys())
	while m > 1:
		#if m is a valid key, print the corresponding values
		if m in sortedwords:
			print 'possible ' + str(m) + ' letter words are'
			print sortedwords[m]
		#find the next word length
		m = m - 1
