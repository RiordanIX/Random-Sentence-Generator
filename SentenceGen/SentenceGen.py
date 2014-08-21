from random import randint
from sys import exit
import wordList

"""
This prints a random simple sentence repeatedly until the user enters 'n'
in the prompt.
"""

###### Sentence Structures ######

def randArticle():
    return wordList.articles[randint(0, len(articles)-1)]

def randNoun():
    return wordList.nouns[randint(0, wordList.numNouns)]
    
def pluralNoun(noun):
    """
    Returns the plural version of a regular noun.
    """
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
    return wordList.reg_verbs[randint(0, wordList.numVerbs)]

def pastSimpleVerb(verb = None):
    """
    Returns the Simple Past version of a regular verb.
    """
    if !verb:
        print "Need to supply a Verb to use"
        return None
    if verb[-1] == 'e':                 # If verb ends with 'e', just add 'd'.
        return verb + 'd'
    
    if verb[-1] == 'x':                 # If verb ends with 'x', ignore other
        return verb + 'ed'              # rules and just add 'ed'.
        
    if verb[-2] in wordList.vowels:     # If 2nd to last letter is a vowel,
        if verb[-3] in wordList.vowels: # double the last consonant letter
            return verb + 'ed'          # unless the letter before last is 
        return verb + verb[-1] + 'ed'   # a vowel too.  mop -> mopped,
                                        # loop -> looped

    if verb[-1] == 'y':                 # If verb ends in 'y' or 'ey',
        if verb[-2] == 'e':             # replaces them with 'ied'.
            return verb[:-2] + 'ied'    
        return verb[:-1] + 'ied'
    
    return verb + 'ed'

def sentenceSubVerbObj(plural = True):
    """
    Returns a sentence in the form of Subject, Verb, Object
    """
    if plural:
        sentence = pluralNoun(randNoun())
    else:
        sentence = randNoun()
    sentence += " " + pastSimpleVerb(randVerb()) + " the "
    sentence += pluralNoun(randNoun()) + "."
    
    return sentence.capitalize()
    
while True:
    print sentenceSubVerbObj()
    if raw_input("> ") == 'n':
        exit(1)