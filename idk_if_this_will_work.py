from decrypter_project import decrypt
from time import sleep
from threading import Thread
from random import randrange

import pygame
import timer
import threading
pygame.init()   #initialising pygame

win = pygame.display.set_mode((300,300))
pygame.display.set_caption("hangman")   #window is called hangman
run,ct = True,0
PATH = "C:\hangman_comp_project"    #path of folder

def animation():

    class text():
        def __init__(self):
            self.x = 100
            self.y = 100
            self.text_font = pygame.font.Font(None,24)
            self.text = ''
            self.box = pygame.Rect(self.x-5,self.y-5,140,24)
            self.color = (255,0,0)
        def draw_box(self):
            pygame.draw.rect(win,self.color,self.box,2)

    hang_draw = []
    for i in range(1,7):    #getting images of hangman
        img = pygame.image.load(PATH +"\hang" + str(i) + '.png')
        hang_draw.append(img)

    #classes
    user_text = text()
    word = text()
    word.y,word.text,word.x = word.y-30,'WORD',word.x-5
    time_left = text()
    th_func = threading.Thread(target = timer.func)
    th_func.start()
    time_left.text = str(timer.ctdn)
    while run:  #main loop
        pygame.time.delay(75)
        time_left.text = str(timer.ctdn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #when you press big red cross at corner
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text.text = user_text.text[:-1]
                elif event.key == pygame.K_RETURN:
                    ct+=1
                else:
                    user_text.text += event.unicode     #which key is pressed
        if timer.ctdn == 0:
            run = False
        win.fill((0,0,0))
        surface = user_text.text_font.render(user_text.text,True,(255,255,255))
        ctdn_surface = time_left.text_font.render(time_left.text,True,(255,0,0))
        word_surface = word.text_font.render(word.text,True,(255,255,255))
        user_text.box.w = max(50,surface.get_width() + 10)
        win.blit(hang_draw[ct],(0,0))   #hangman
        win.blit(surface,(user_text.x,user_text.y))     #text input
        win.blit(word_surface,(word.x,word.y))
        win.blit(ctdn_surface,(0,0))
        user_text.draw_box()
        pygame.display.update()

    pygame.quit()
x = open("movie_list.txt","r")
text = x.readlines()

dec = decrypt(text)
dec_2 = decrypt(dec)

ind = randrange(0,len(dec))
word = dec_2[ind]



    

print("welcome to hangman.  ............ . enter guess when you think you are ready to guess the word. All input mjust be given in lowercase. ")



def game(word):
    
    tries = 7
    letters_left = 0
    entered_letters = set() #to ensure no repetetion of letters
   

    while tries:
        
        inp_letter = input("enter a single letter: (or guess if you think you are ready) ")

        if stop:
            break
        
        if inp_letter == "guess": #if user is ready to answer
            inp_letter = input("enter the word: ")

            if inp_letter == word:
                print("you got the word")
                break
            else:
                print("sorry thats not the word")
                print()
                continue

        elif len(inp_letter)>1 or inp_letter == "" or inp_letter == " " or not inp_letter.isalpha(): #invalid inputs
            print("you entered an invalid input ")
            print()
            continue

        elif inp_letter in entered_letters:
            print("you have aldready entered that letter: ")
            print()
            continue

        entered_letters.add(inp_letter)
        a = word.count(inp_letter)
        print("letter occours",a,"times") 
        
        if a == False:
            tries -= 1
            print(tries, "tries left")
            print()

        elif a:
            letters_left += a
            print(len(word)-word.count(" ")-letters_left,"letters left")
            print()
            

        if letters_left == len(word)-word.count(" "): 
            print("you got the word ")
            break

        
    else:
        print("out of tries sorry ")


stop = False
game_func = Thread(target = game,args = (word,))
animation_func = Thread(target = animation)


game_func.start()
animation_func.start()

animation_func.join()
stop = True

print("\n time up \n press enter to continue")
