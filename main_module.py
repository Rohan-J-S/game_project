  
from decryption_test import decrypt
from random import randrange

def word():
    x = open("movie_list.txt","r")
    text = x.readlines()


    global dec_2 
    dec_2 = decrypt(text)

    ind = randrange(0,len(dec_2))
    word = dec_2[ind]
    return word

    
print("welcome to hangman.  ............ . enter guess when you think you are ready to guess the word")

def game(word,inp_letter,letters_left,entered_letters,ct): 
    run = True

    if inp_letter == "guess":
        guess = input()
        if guess == word:
            print('you got the word')
            run = False
        else:
            print("sorry thats not the word")
            print()


    elif len(inp_letter)>1 or inp_letter == "" or inp_letter == " " or not inp_letter.isalpha():
        print("you entered an invalid input ")
        print()


    elif inp_letter in entered_letters:
        print("you have aldready entered that letter: ")
        print()

    else:
        entered_letters.add(inp_letter)
        a = word.count(inp_letter)
        print("letter occours",a,"times")
        
        if a == 0:
            print("not there noob")
            ct += 1

        elif a:
            letters_left -= a

        if letters_left == 0:
            print("you got the word ")
            run = False
    return [run,letters_left,entered_letters,ct]
