
from time import *

def check(inp_letter,word):
 
    try:
        if len(inp_letter) > 1:
            raise ValueError
                
        elif inp_letter in word:
            
            return True

        else:
            return False

        for x in range(len(word)):
            if word[x] == inp_letter:
                word = word[:x] + word[x+1:]
    except:
        inp_letter = input("enter a single letter: ")
        return check(inp_letter,word)

terminate = False
tries = 7
while tries:
    inp_letter = input("enter letter: ")
    print(check(inp_letter,"test"))
    
    if check(inp_letter,"test") == False:
        tries -= 1
    print(tries, "tries left")
else:
    print("out of tries sorry ")