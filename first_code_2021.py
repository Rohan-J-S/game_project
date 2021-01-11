


print("welcome to hangman.  ............ . enter guess when you think you are ready to guess the word")

terminate = False
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
            continue

    elif len(inp_letter)>1 or inp_letter == "":
        print("you entered an invalid input ")
        continue

    elif inp_letter in entered_letters:
        print("you have aldready entered that letter: ")
        continue

    entered_letters.add(inp_letter)
    a = "test".count(inp_letter)
    print(a)
    
    if a == False:
        tries -= 1
        print(tries, "tries left")

    elif a:
        letters_left += a
        print(letters_left)
        

    if letters_left == 4:
        print("you got the word ")
        break
else:
    print("out of tries sorry ")