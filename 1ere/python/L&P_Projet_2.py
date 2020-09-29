# Level 1
def tableMultiComplete():
    for x in range(1, 10):
        print(f"Table de: {x}:")
        for i in range(11):
            print(f"{x}*{i} = ", x*i)


# Level 2
def tableMulti(n):
    for i in range(11):
        print(f"{n}*{i} = ", n*i)
    
def tableMultiFinale():
    for i in range(11):
        tableMulti(i)


# Level 3
def tableMultiCarre(n):
    number = ""
    i = 0
    while i < 9:
        if n*i+n < 10:
            number += " " + str(n*i+n) + " "
        else:
            number += str(n*i+n) + " "
        i += 1
    return number

def tableMultiFinaleCarre():
    i = 1
    while i < 10:
        print(tableMultiCarre(i))
        i += 1


# Level 3+
def tableMultiCarre2(n):
    number = ""
    i = 9
    while i != 9:
        if n/i+n < 10:
            number += " " + str(n/i+n) + " "
        else:
            number += str(n/i+n) + " "
        i -= 1
    return number

def tableMultiFinaleCarre2():
    i = 9
    while i != 0:
        print(tableMultiCarre(i))
        i -= 1


# Level 3++
def tableMultiCarre3(n):
    number = ""
    for i in range(11):
        number += str(n*i+n) + " "
    return number
    
def tableMultiFinaleCarre3():
    for i in range(1,10):
        print(tableMultiCarre(i))


# Level 3+++
def matrix():
    for i in range(1,11):
        l = []
        for x in range(1,11):
            if i*x < 10:
                l.append(f"{i*x} ")
            else:
                l.append(i*x)
        print(*l)


# Level 3++++
def matrix2():
    for i in range(1,11):
        l = []
        for x in range(1,11):
            l.append(f"{i*x} ") if i*x < 10 else l.append(i*x)
        print(*l)
        
        



