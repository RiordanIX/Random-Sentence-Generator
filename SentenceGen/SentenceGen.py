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
    
    
    
def pluralNoun(noun = None):
    """
    Returns the plural version of a regular noun.
    """
    if !noun:
        print wordList.no_noun
        return None
    if noun[-1] == 'y':
        if noun[-2] == 'e':
            if noun == 'key':
                return noun + 's'
            else:
                return noun[:-2] + "ies"
        else:
            return noun[:-1] + "ies"
            
    elif noun[-1] == 'x':
        return noun + "es"
        
    elif noun[-1] == 'h':
        return noun + "es"
    else:
        return noun + 's'

    
    
def randVerb():
    return wordList.reg_verbs[randint(0, wordList.numVerbs)]

    
    
def verbSimplePresent(subject, verb = None):
    """
    Returns the Simple Present form of a regular verb.
    """
    if !verb:
        print wordList.no_verb
        return None
        
    elif subject in wordList.first_and_second_obj_pronouns:
        return verb
        
    elif verb[-1] == 'h' or 'x':
        return verb + 'es'
        
    elif verb[-1] == 'y':
        if verb[-2] == 'e':
            return verb[:-2] + 'ies'
        else:
            return verb[:-1] + 'ies'
    else:
        return verb + 's'

    
    
def verbSimplePast(verb = None):
    """
    Returns the Simple Past form of a regular verb.
    """
    if !verb:
        print wordList.no_verb
        return None
    elif verb[-1] == 'e':               # If verb ends with 'e', just add 'd'.
        return verb + 'd'
    
    elif verb[-1] == 'x':               # If verb ends with 'x', ignore other
        return verb + 'ed'              # rules and just add 'ed'.
        
    elif verb[-2] in wordList.vowels:   # If 2nd to last letter is a vowel,
        if verb[-3] in wordList.vowels: # double the last consonant letter
            return verb + 'ed'          # unless the letter before last is 
        else:                           # a vowel too.  mop -> mopped,
            return verb + verb[-1] + 'ed'# loop -> looped

    elif verb[-1] == 'y':               # If verb ends in 'y' or 'ey',
        if verb[-2] == 'e':             # replaces them with 'ied'.
            return verb[:-2] + 'ied'
        else:
            return verb[:-1] + 'ied'
    else:
        return verb + 'ed'

    
    
def verbSimpleFuture(verb = None):
    if !verb:
        print wordList.no_verb
        return None
    return beFuture + verb



def sentenceSubVerbObj(plural = True):
    """
    Returns a sentence in the form of Subject, Verb, Object
    """
    if plural:
        sentence = pluralNoun(randNoun())
    else:
        sentence = randNoun()
    
    sentence += " " + verbSimplePast(randVerb()) + " the "
    sentence += pluralNoun(randNoun()) + "."
    
    return sentence.capitalize()



while True:
    print sentenceSubVerbObj()
    if raw_input("> ") == 'n':
        exit(1)
