def decrypt():
    y = open("key.txt","r")
    keys = y.readlines()

    rev_dict = dict()
    asci = 32
    for x in keys:
      
        rev_dict[int(x)] = chr(asci)
        asci += 1

    y.close()

    h = open("key.txt","w")
    h.write("")
    h.close()

    x = open("tt.txt","r")
    text = x.readlines()

    for d in range(len(text)):
        s = ""
        for z in range(len(text[d])):
            if text[d][z] == "\n":
                continue
            s += rev_dict[ord(text[d][z])]
           
        text[d] = s
    x.close()
    return text

decrypt()
