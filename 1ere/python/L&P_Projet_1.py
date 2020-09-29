import math

def calculHypothenus(a, b):
    return round(math.sqrt(a**2 + b**2), 2)

def reciproque(hypothenus, a, b):
    if calculHypothenus(a,b) == hypothenus:
        return True
    else:
        return False

#print(calculHypothenus(float(input("Valeur 1: ")), float(input("Valeur 2: "))), "est la valeur de l'hypothenus")

#print(calculHypothenus(float(input("Valeur hypothenus: ")), float(input("Valeur 1: ")), int(input("Valeur 2: "))))