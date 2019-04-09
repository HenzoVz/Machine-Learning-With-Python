# -*- coding: utf-8 -*-

# Tokenization of paragraphs/sentences
# Importing Libraries
import re
import nltk
#nltk.download()

paragraph = """Thank you all so very much. Thank you to the Academy. 
               Thank you to all of you in this room. I have to congratulate 
               the other incredible nominees this year. The Revenant was 
               the product of the tireless efforts of an unbelievable cast
               and crew. First off, to my brother in this endeavor, Mr. Tom 
               Hardy. Tom, your talent on screen can only be surpassed by 
               your friendship off screen … thank you for creating a t
               ranscendent cinematic experience. Thank you to everybody at 
               Fox and New Regency … my entire team. I have to thank 
               everyone from the very onset of my career … To my parents; 
               none of this would be possible without you. And to my 
               friends, I love you dearly; you know who you are. And lastly,
               I just want to say this: Making The Revenant was about
               man's relationship to the natural world. A world that we
               collectively felt in 2015 as the hottest year in recorded
               history. Our production needed to move to the southern
               tip of this planet just to be able to find snow. Climate
               change is real, it is happening right now. It is the most
               urgent threat facing our entire species, and we need to work
               collectively together and stop procrastinating. We need to
               support leaders around the world who do not speak for the 
               big polluters, but who speak for all of humanity, for the
               indigenous people of the world, for the billions and 
               billions of underprivileged people out there who would be
               most affected by this. For our children’s children, and 
               for those people out there whose voices have been drowned
               out by the politics of greed. I thank you all for this 
               amazing award tonight. Let us not take this planet for 
               granted. I do not take tonight for granted. Thank you so very much."""
               

# Tokenizing sentences
sentences = nltk.sent_tokenize(paragraph)
print(sentences)


# Tokenizing words
words = nltk.word_tokenize(paragraph) 
print(words)

pattern1 = "Apples are tasty"
pattern2 = "Today I feel like crying."

#Se zero ou mais caracteres no início da string corresponderem ao padrão de expressão regular
if re.match(r"^Apples",pattern1):
    print("Matches!")
else:
    print("No Match!")

# Verificando se o termo de pesquisa existe no texto    
if re.search(r"\.$",pattern2):
    print("Match!")
else:
    print("No Match!")
    
pattern1 = "I love Avengers" #I love Justice League

print(re.sub(r"Avengers","Justice League",pattern1))

print(re.sub(r"[a-z]","0",pattern1,1,flags=re.I))

sentence1 = "Welcome to the year 2018"
sentence2 = "Just ~%* ++++--- arrived at @Jack's place. #fun"
sentence3 = "I                  love                u"

sentence1_modified = re.sub(r'\d','',sentence1)
print(sentence1_modified)

sentence2_modified = re.sub(r'[@#\.\']','',sentence2)
print(sentence2_modified)

sentence2_modified = re.sub(r'\W',' ',sentence2)
print(sentence2_modified)

sentence2_modified = re.sub(r'\s+',' ',sentence2_modified)                               
print(sentence2_modified)

sentence2_modified = re.sub(r"\s+[a-zA-Z]\s+",' ',sentence2_modified)
print(sentence2_modified)

sentence3_modified = re.sub(r'\s+',' ',sentence3)     
print(sentence3_modified)

X = ["This is a wolf @scary",
     "Welcome to the jungle #missing",
     "111322 the number to know",
     "Remember the name s - John",
     "I                love               you"]


for i in range(len(X)):
    X[i] = re.sub(r"\W"," ",X[i])
    X[i] = re.sub(r"\d"," ",X[i])
    X[i] = re.sub(r"\s+[a-z]\s+"," ",X[i],flags=re.I)
    X[i] = re.sub(r"\s+"," ",X[i])
    X[i] = re.sub(r"^\s","",X[i])
    X[i] = re.sub(r"\s$","",X[i])

print(X)