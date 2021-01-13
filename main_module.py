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
    exit
    


print("welcome to hangman.  ............ . enter guess when you think you are ready to guess the word")



def game():
    
    tries = 7
    letters_left = 0
    entered_letters = set()
    word = "test hello"


    while tries:
        
        inp_letter = input("enter a single letter: ")

        if stop:
            break
        
        if inp_letter == "guess":
            inp_letter = input("enter the word: ")

            if inp_letter == word:
                print("you got the word")
                break
            else:
                print("sorry thats not the word")
                print()
                continue

        elif len(inp_letter)>1 or inp_letter == "" or inp_letter == " ":
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
th_func = threading.Thread(target = timer)
game_func = threading.Thread(target = game)

th_func.start()
game_func.start()

th_func.join()
stop = True

print("\n time up \n press enter to continue")
