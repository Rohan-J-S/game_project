import time
import threading

def func():
    global ctdn
    ctdn = 31 #number of seconds
    temp = ctdn
    while ctdn>0:
        ctdn -= 1
        time.sleep(1)

