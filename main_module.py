from decrypter_project import decrypt
import time
import threading


x = open("movie_list.txt","r")
text = x.readlines()

dec = decrypt(text)
dec_2 = decrypt(dec)

def timer():
    global ctdn
    ctdn = 11 #number of seconds +1
    temp = ctdn
    for i in range(temp,0,-1):
        ctdn -= 1
        #remove once game func added in while
        time.sleep(1)
    else:
        raise ValueError("time up lmao")


print("welcome to hangman.  ............ . enter guess when you think you are ready to guess the word")



def game():
    
    tries = 7
    letters_left = 0
    entered_letters = set()

    while tries:
        inp_letter = input("enter a single letter: ")
        
        
        if inp_letter == "guess":
            inp_letter = input("enter the word: ")

            if inp_letter == "test":
                print("you got the word")
                break
            else:
                print("sorry thats not the word")
                print()
                continue

        elif len(inp_letter)>1 or inp_letter == "":
            print("you entered an invalid input ")
            print()
            continue

        elif inp_letter in entered_letters:
            print("you have aldready entered that letter: ")
            print()
            continue

        entered_letters.add(inp_letter)
        a = "test".count(inp_letter)
        print(a)
        
        if a == False:
            tries -= 1
            print(tries, "tries left")
            print()

        elif a:
            letters_left += a
            print(letters_left)
            print()
            

        if letters_left == 4:
            print("you got the word ")
            break
    else:
        print("out of tries sorry ")

try:  
    th_func = threading.Thread(target = timer)
    game_func = threading.Thread(target = game)

    th_func.start()
    game_func.start()
except ValueError:
    print("sorry time up")

