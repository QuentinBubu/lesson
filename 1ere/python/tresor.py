import math
import time
def est_premier(nombre):
    if nombre < 0:
        return "Erreur"
    if nombre%2 == 0 and nombre != 2: #Si il est paire
        return False
    elif nombre == 2:
        return True
    for i in range(2,100):
        if nombre%i==0 and i != nombre:
            return False
    return True
    
    
def est_premier2(nombre):
    start_time = time.time()
    if nombre < 0:
        return "Erreur"
    elif nombre == 2:
        return True
        
    i = nombre-1
    while i != 3:
        if nombre%i == 0:
            return False
        i -= 1
    return True

def sphinx_aime(nombre):
    if nombre < 2:
        return "Erreur: Saisissez un chiffre/nombre suppérieur à 1"
    if est_premier(nombre) and est_premier(nombre+2):
        return "Il aime le chiffre/nombre"
    else:
        return "Il aime pas le chiffre/nombre!"

def code_hall():
    for i in range(2,100):
        if est_premier(i+2):
            return i

def est_puissance_2(nb):
    nb = math.log(nb, 2)
    b = str(nb).split(".")
    if b[1] == "0":
        return True
    else:
        return False

def osiris_aime(nombre):
    if est_puissance_2(nombre+1) and nombre%5 == 3:
        z = 3
        
# est_premier(117)
# print(time.time())