from time import sleep

def func():
    global ctdn
    ctdn = 46 #number of seconds
    temp = ctdn
    while ctdn>0:
        ctdn -= 1
        sleep(1)

