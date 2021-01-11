def decrypt(text):
    dec_key = {'h':'a','d':'b','s':'c','n':'d','a':'e','i':'f','q':'g','k':'h','e':'i','y':'j','u':'k','j':'l','o':'m','t':'n','c':'o','w':'p','m':'q',"b":"r",'r':'s','f':'t','l':'u','x':'v','p':'w','g':'x','z':'y','v':'z',' ':' '}

    for y in range(len(text)):
        s = ""
        for z in range(len(text[y])):
            if text[y][z] == "\n":
                break
            s += dec_key[text[y][z]]
        text[y] = s
    return text
print(decrypt(['hxatqabr ', 'etsawfect', 'nltuebu']))