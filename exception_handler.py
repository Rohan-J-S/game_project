from math import factorial
def x(a):
    try:
        return factorial(a)
    except:
        print('enter a +ve number: ')
        a = int(input("...."))
        return x(a)
a = int(input("...."))
print(x(a))


