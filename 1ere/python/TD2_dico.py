# 1
dico = {
    "pommes": 3,
    "oranges": 2,
    "kiwis": 8,
    "courges": 1,
    "noix": 50,
    "citrons": 4
}
print(dico)

dico["courges"] = 3
print(dico)

dico["fraises"] = 9
print(dico)

del dico["noix"]
print(dico)

print(*dico.keys())

for achat, nombre in dico.items():
    print(f"{achat} => {nombre}")
    
for achat, nombre in dico.items():
    print(f"{achat} => {nombre}") if nombre%2 == 0 else 0
    
total = 0
for nombre in dico.values():
    total+=nombre

print(total)

# 2

def sommeElements(liste):
    total = 0
    for nombre in liste:
        total+=nombre
    return total

def sommePairs(liste):
    total = 0
    for nombre in liste:
        total+=nombre if nombre%2 == 0 else 0
    return total

def nbElemPairs(liste):
    total = 0
    for nombre in liste:
        total+=1 if nombre%2 == 0 else 0
    return total

def maxPair(liste):
    if min(liste) < 0:
        return "Erreur"
    return max(liste)

def minPair(liste):
    if min(liste) < 0 or max(liste) >= 100:
        return "Erreur"
    return min(liste)

def indiceDe(number, liste):
    if len(liste) == 0 or number < 0:
        return "Erreur"
    return liste.index(number)

def trouvePremierPair(liste):
    if len(liste) == 0:
        return "Erreur"
    for x in liste:
        if x%2 == 0:
            return x