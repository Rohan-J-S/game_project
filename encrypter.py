
def encrypt(text):

    key = {'a':'h','b':'d','c':'s','d':'n','e':'a','f':'i','g':'q','h':'k','i':'e','j':'y','k':'u','l':'j','m':'o','n':'t','o':'c','p':'w','q':'m','r':'b','s':'r','t':'f','u':'l','v':'x','w':'p','x':'g','y':'z','z':'v',' ':' '}
    
    for y in range(len(text)):
        s = ""

        for z in range(len(text[y])):

            if text[y][z] == "\n":
                break

            s += key[text[y][z]]
        text[y] = s
    return text


