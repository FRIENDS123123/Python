from typing import MutableMapping


introString = input("Enter Any Sentence")
characterCount=0
wordCount=1
for i in  introString:
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1
print("Number of Words")
print(wordCount)      
print("Number of characters")
print(characterCount)

