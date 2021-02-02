from decrypter_project import decrypt
from random import randrange

def word():
    x = open("movie_list.txt","r")
    text = x.readlines()

    dec = decrypt(text)
    dec_2 = decrypt(dec)

    ind = randrange(0,len(dec))
    word = dec_2[ind]
    w = ''
    for i in word:
        if i not in 'aeiouAEIOU ':
            w+= '_'
        else:
            w += i
    return [w,word]

def game(word,inp_letter,letters_left,entered_letters,ct,bl_word): 
    run,info_text = True,None
    vowels,ct_vow = set('aeiouAEIOU'),0
    entered_letters.update(vowels)

    if inp_letter == word:
        run = False

    elif len(inp_letter)>1 or inp_letter == "" or inp_letter == " " or not inp_letter.isalpha():
        info_text = "You entered an invalid input"


    elif inp_letter in entered_letters:
        info_text = "You have already entered that letter"

    else:
        entered_letters.add(inp_letter)
        a = word.count(inp_letter)
        
        if a == 0:
            ct += 1
            info_text = "That letter is not there"

        elif a:
            letters_left -= a
            for times in range(a):
                for index in range(len(word)):
                    if inp_letter == word[index]:
                        bl_word = bl_word[:index] + inp_letter + bl_word[index+1:]

        if letters_left == 0:
            run = False
    return [run,letters_left,entered_letters,ct,bl_word,info_text]

def vow_ct(word,inp_letters):
    lt = 0
    for i in word:
            if i in 'aeiouAEIOU' and i not in inp_letters:
                lt += word.count(i)
                inp_letters.add(i)
    return lt



