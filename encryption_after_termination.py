from random import randrange
def encrypt():

    x = open("movie_list.txt","r")
    text = x.readlines()

    values = list(range(32,65+27+32))
    key = dict()

    for letter in range(32,65+27+32):
        val = randrange(0,len(values))
        key[chr(letter)] = values[val]
        values.pop(val)


    for y in range(len(text)):
        s = ""
        for z in range(len(text[y])):
            if text[y][z] == "\n":
                continue
            s += chr(key[text[y][z]])
        text[y] = s+"\n"
    x.close()

    f = open("movie_list.txt","w")
    for b in text:
        f.write(b)

    key_file = open("key.txt","w+")
    for value in key.values():
        key_file.write(str(value) + "\n")