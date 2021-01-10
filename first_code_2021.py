
def check(inp_letter,word):

        if inp_letter in word:
            return word.count(inp_letter)

        else:
            return False

terminate = False
tries = 7
letters_left = 0

while tries:
    inp_letter = input("enter a single letter: ")

    if len(inp_letter)>1:
        print("you entered an invalid input ")
        continue

    a = check(inp_letter,"test")
    print(a)
    
    if a == False:
        tries -= 1
        print(tries, "tries left")

    elif a:
        letters_left += check(inp_letter,"test")
        print(letters_left)

    if letters_left == 4:
        print("you got the word ")
        break
else:
    print("out of tries sorry ")