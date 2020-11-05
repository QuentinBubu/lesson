# Ex 1
<<<<<<< HEAD
import math
=======
>>>>>>> 1a90bc52700091114c12dc5cb52c45c8bdabeec6
"""
listInf = [i for i in range(0,1000)]
print(listInf)

<<<<<<< HEAD
listCarres = [i**2 for i in listInf if p**2 <= 1000]
# Or
#listCarres = [i**2 for i in range(0,1000)]
#print(listCarres)

listBaseCarres = [math.sqrt(i) for i in listCarres if i < 1000]
=======
listCarres = [i**2 for i in listInf]
# Or
listCarres = [i**2 for i in range(0,1000)]
print(listCarres)

listBaseCarres = [i for i in listCarres if i < 1000]
>>>>>>> 1a90bc52700091114c12dc5cb52c45c8bdabeec6
print(listBaseCarres)

listCubes = [i**3 for i in range(0,1000)]
print(listCubes)

listBaseCubes = [i for i in listCubes if i < 1000]
print(listBaseCubes)

listCarresCubes = [i for i in listBaseCubes if i in listBaseCarres]
print(listCarresCubes)


# Ex 2

def calcSomme(number):
    number = str(number)
    somme = 0
    for i in range(len(number)):
        somme += int(number[i])
    return somme

def calcExp3(number):
    return number**3

def rechercheDudeney():
    listValid = []
    for i in range(1,100000):
        if calcExp3(calcSomme(i)) == i:
            listValid.append(i)
    return listValid

print(rechercheDudeney())

"""

# Ex 2+

def calcSomme(number):
    number = list(str(number))
    somme = 0
    for i in range(len(number)):
        somme += int(number[i])
    return somme

# !
def calcSommeDix(number):
    result = 0
    while number != 0:
        result += number%10
        number -= number%10
        #number /= 10
    return result













def calcExp3(number):
    return number**3

def rechercheDudeney():
    listValid = []
    for i in range(1,100000):
        if calcExp3(calcSomme(i)) == i:
            listValid.append(i)
    return listValid

print(rechercheDudeney())
























