import math

def nEntiers(entier):
    a = 0
    for i in range(1,entier+1):
        a += i
    print(a)
    
def factorielle(nombre):
    a = 1
    for i in range(1,nombre+1):
        a *= i
    print(a)
    
def factoRec(nombre):
    if nombre > 2:
        return nombre*factoRec(nombre-1)
    return nombre
    
def remise(prix, nb):
    prix *= nb
    if nb >= 5: 
        prix -= prix*0.05
    return prix
    
    
def pun(text, nb):
    for i in range(nb):
        print(text)
        
def table(table):
    for i in range(11):
        print(f"{table}*{i} = ", table*i)
        
def table_1_9():
    for x in range(1, 10):
        print(f"Table de: {x}:")
        for i in range(11):
            print(f"{x}*{i} = ", x*i)

def ma_fonction(x):
    y = math.pow(x, 2)+2*x+10
    return y
    
def dis_bonjour(nom, age):
    phrase = f"Bonjour {nom}, vous avez {age}"
    return phrase
    
def ma_fonction():
    return "Voivi une fonction qui ne sert à rien"
    
def annonce(num, prov, dest):
    if dest != "0":
        msg = f"Le train n°{num} en provenance de {prov} et à destinnation de {dest}, entre en gare."
    else:
        msg = f"Le train n°{num} en provenance de {prov} entre en gare. Ce train ne s'arrête pas!"
    return msg
    
def age(age):
    if age < 18:
        print("Vous êtes mineur")
    elif age == 18:
        print("Vous venez d'être majeur")
    else:
        print("Vous êtes majeur")
        
def matrix():
    for i in range(1,11):
        l = []
        for x in range(1,11):
            if i*x < 10:
                l.append(f"{i*x} ")
            else:
                l.append(i*x)
        print(*l)

"""
age(int(input("Quel est votre âge? ")))
print("Hello world")

i = 12

i = 125
print(i)

a = 3.1
b = 7

a = 5
b = 10
resultat = a+b

a += 1

print(math.pow(2,3))

print(math.cos(9))

print(math.sqrt(9))

a = 5
b = 16
c = 3.14/2
d = b/a
e = b//a
g = b%a
h = math.pow(a,2)
i = math.sqrt(b)
j = math.sin(c)

print(type(2.2+1))

ma_chaine = "Bonjoiur tout le monde!"

print(ma_chaine)

a =  "Hello"
b = "World"

mon_expression = a + b

print(mon_expression)

ma_chaine = "Bonjour "
ma_chaine2 = "le "
print(ma_chaine + ma_chaine2 + "monde!")

mon_nombre = 5

res = "Nombre de personnes: " + str(mon_nombre)

res = f"Nombre de personnes:  {mon_nombre}"

print(dis_bonjour("Quentin", 16))

a = 4
b = 7
print(a==b)
print(a!=b)
print(a<b)

a = 4
b = 7

if a < b:
    print("Je suis toto.")
    print("Je n'aime pas titi.")
else:
    print("Je suis titi")
    print("Je n'aime pas toto")

print("En revanche, j'aime bien le python")



a = 5
b = 10
if a > 5 and b == 10:
    print("Toto")
else:
    print("Titi")

if a > 5 or b == 10:
    print("Tata")
else:
    print("Tutu")

i = 0

while i < 10:
    print(f"i vaut: {i}")
    i+=1
print("C'est terminé.")

def factoRecursive(nombre):
    if nombre >= 1:
        a = factoRecursive(nombre-1)
    else:
        a = 0
    b = nombre*a
    print(b)
    return b
    
"""




















































