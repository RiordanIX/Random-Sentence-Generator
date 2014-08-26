nouns = ['aardvark', 'animal', 'alimony', 'avatar', 'bitch', 'bib', 'bucket',
        'cat', 'cadaver', 'camp', 'crap', 'crocodile', 'cucaburro', 'donkey',
        'elephant', 'fox', 'glove', 'hand', 'index', 'justice', 'wipe'
        ]

reg_verbs = ['attack', 'boot', 'crap', 'ditch', 'etch', 'fix', 'gripe', 'hex',
            'invest', 'justify', 'kick', 'limp', 'mop', 'nod', 'open', 'poke',
            'rage', 'stare', 'tear', 'underestimate', 'venerate', 'whisk',
            'yell', 'zap'
            ]

bePast = {'he'  : 'was',
          'she' : 'was',
          'it'  : 'was',
          'I'   : 'was',
          'you' : 'were',
          'we'  : 'were',
          'they': 'were'}

bePresent = {'he'  : 'is',
             'she' : 'is',
             'it'  : 'is',
             'I'   : 'am',
             'you' : 'are',
             'we'  : 'are',
             'they': 'are'}

beFuture = 'will'

havePast = 'had'

havePresent = {'he'  : 'has',
               'she' : 'has',
               'it'  : 'has',
               'I'   : 'have',
               'you' : 'have',
               'we'  : 'have',
               'they': 'have'}

haveFuture = 'will have'

articles = ['a', 'the']

conjunctions = ['and', 'but', 'or', 'with', 'while']

third_obj_pronouns = ['he', 'she', 'it', 'they']

first_and_second_obj_pronouns = ['I', 'we', 'you']

ind_obj_pronouns = ['me', 'her', 'him', 'it', 'you', 'us']

vowels = ['a', 'e', 'i', 'o', 'u']

###### Global variables ######

no_verb = "Error:  No verb supplied."
no_noun = "Error:  No noun supplied."

numNouns = len(nouns) - 1

numVerbs = len(reg_verbs) - 1