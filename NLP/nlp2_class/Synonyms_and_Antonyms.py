# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:42:53 2019

@author: Murilo
"""

# Finding synonyms and antonyms of words

# Importing libraries
from nltk.corpus import wordnet

# Initializing the list of synnonyms and antonyms
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())
            
            
# Displaying the synonyms and antonyms
print(set(synonyms))
print(set(antonyms))