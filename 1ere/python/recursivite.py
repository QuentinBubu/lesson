def fctA():
    print("Début de fonction fctA")
    i = 0
    while i < 5:
        print(f"fctA {i}")
        i += 1
    print("Fin de fonction fctA")
    
def fctB():
    print("Début de fonction fctB")
    i = 0
    while i < 5:
        if i == 3:
            fctA()
            print("Retour à la fonction B")
        print(f"fctB {i}")
        i += 1
    print("Fin de fonction B")

fctB()

# 2

def fctA():
    print("Hello")
    fctA()
    
# fctA()

# 3

def fonct(n):
    if n > 0:
        fonct(n-1)
    print(n)
    
fonct(3)

def fact(n):
    if n > 0:
        return n*fact(n-1)
    else:
        return 1

# 5

def fib(number):
    print(number)
    print("****")
    if number > 0:
        print(number+fib(number-1))
        print("-----")
        return number+fib(number-1)
    return 0























