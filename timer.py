import time
import threading

def func():
    global ctdn
    ctdn = 11 #number of seconds +1
    temp = ctdn
    for i in range(temp,0,-1):
        ctdn -= 1
        print(ctdn) #remove once game func added in while
        time.sleep(1)

th_func = threading.Thread(target = func)
th_func.start()

while ctdn>-1:
    #put game function here
    if ctdn == 0:
        print()
        print('OVER')
        break
