
def check(inp_letter,word):
    if inp_letter == word:
        return True

    elif inp_letter in word:
        return word.count(inp_letter)+1

    else:
        return False

print("welcome to hangman.  ............ . enter guess when you think you are ready to guess the word")

terminate = False
tries = 7
letters_left = 0
entered_letters = set()
target = 4

while tries:
    inp_letter = input("enter a single letter: ")
    

    if inp_letter == "guess":
        inp_letter = input("enter the word (or a letter if you want to): ")

    elif len(inp_letter)>1:
        print("you entered an invalid input ")
        continue

    elif inp_letter in entered_letters:
        print("you have aldready entered that letter: ")
        continue

    entered_letters.add(inp_letter)
    a = check(inp_letter,"test")
    print(a)
    
    if a == False:
        tries -= 1
        print(tries, "tries left")

    elif a-1:
        letters_left += check(inp_letter,"test")
        print(letters_left)
        target += 1

    elif letters_left == target or a == True:
        print("you got the word ")
        break
else:
    print("out of tries sorry ")