from random import randint
from sys import exit

"""
This prints a random simple sentence repeatedly until the user enters 'n'
in the prompt.
"""

nouns = ['aardvark', 'animal', 'alimony', 'avatar', 'bitch', 'bib', 'bucket',
		'cat', 'cadaver', 'camp', 'crap', 'crocodile', 'cucaburro', 'donkey',
		'elephant', 'fox', 'glove', 'hand', 'index', 'justice', 'wipe'
		]
		
reg_verbs = ['attack', 'boot', 'crap', 'ditch', 'etch', 'fix', 'gripe', 'hex',
			'invest', 'justify', 'kick', 'limp', 'mop', 'nod', 'open', 'poke',
			'rage', 'stare', 'tear', 'underestimate', 'venerate', 'whisk',
			'yell'
			]

articles = ['a', 'the']

conjunctions = ['and', 'but', 'or', 'with', 'while']

obj_pronouns = ['I', 'she', 'he', 'it', 'you']
ind_obj_pronouns = ['me', 'her', 'him', 'it', 'you']

vowels = ['a', 'e', 'i', 'o', 'u']

###### Global variables ######
nouns_index = len(nouns) - 1
verbs_index = len(reg_verbs) - 1



###### Sentence Structures ######

def randArticle():
	return articles[randint(0, len(articles)-1)]

def randNoun():
	return nouns[randint(0, nouns_index)]
	
def pluralNoun(noun):
	
	if noun[-1] == 'y':
		if noun[-2] == 'e':
			return noun[:-2] + "ies"
		else:
			return noun[:-1] + "ies"
			
	if noun[-1] == 'x':
		return noun + "es"
		
	if noun[-1] == 'h':
		return noun + "es"
		
	return noun + 's'

def randVerb():
	return reg_verbs[randint(0, verbs_index)]

def pastVerb(verb):
	if verb[-1] == 'e':
		return verb + 'd'
	
	if verb[-1] == 'x':
		return verb + 'ed'
	if verb[-2] in vowels:				# 99% of the time, need to add last
		if verb[-3] in vowels:			# char to keep the vowel pronunciation
			return verb + 'ed'			# the same.  Example:  mop -> mopped
		return verb + verb[-1] + 'ed'

	if verb[-1] == 'y':
		if verb[-2] == 'e':
			return verb[:-2] + 'ied'
		return verb[:-1] + 'ied'
	
	return verb + 'ed'

def sentenceSubVerbObj(plural = True):
	""" Returns a sentence in the form of Subject, Verb, Object"""

	sentence =  pluralNoun(randNoun()) + " " + pastVerb(randVerb()) + " "
	sentence += "the " + pluralNoun(randNoun()) + "."
	
	return sentence.capitalize()
	
while True:
	print sentenceSubVerbObj()
	if raw_input("> ") == 'n':
		exit(1)
