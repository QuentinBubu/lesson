import math
def est_premier(nombre):
    if nombre%2 == 0 and nombre != 2: #Si il est paire
        return False
    elif nombre == 2:
        return True
    for i in range(2,100):
        if nombre%i==0 and i != nombre:
            return False
    return True

def sphinx_aime(nombre):
    if nombre < 2:
        return "Erreur: Saisissez un chiffre/nombre suppérieur à 1"
    if est_premier(nombre) and est_premier(nombre+2):
        return "Il aime le chiffre/nombre"
    else:
        return "Il aime pas le chiffre/nombre!"

def code_hall():
    if nombre > 0:
        return "Pas strictement positif"
    for i in range(2,100):
        if est_premier(i+2):
            return i

def est_puissance_2(nb):
    if nombre > 0:
        return "Pas strictement positif"
    a = math.sqrt(nb)
    b = str(a).split(".")
    if  nb == a**2 and b[1] == "0":
        return True
    else:
        return False
        
def osiris_aime(nombre):
    if nombre > 0:
        return "Pas strictement positif"
    if est_puissance_2(nombre+1) and nombre%5 == 3:
        return True
    else:
        return False
    
def osiris_aime2():
    for i in range(1, 100):
        if est_puissance_2(i+1) and i%5 == 3:
            return i
        else:
            return False
    
def code_tresor():
    pass