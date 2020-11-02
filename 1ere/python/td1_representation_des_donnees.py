# Ex 1
monTuple = (1,2,3,4,5,6)
print(monTuple)
print(monTuple[0])
print(monTuple[2])
print(monTuple[-1])

# Ex 2
maListe = [1, 2, 3, 4, 5, 6]
print(maListe[0])
print(maListe[2])
maListe.append(7)
print(maListe)
del maListe[0]
print(maListe)
maListe[0] = 99
print(maListe)
print(len(maListe))
print(maListe[len(maListe)-1])

# Ex 3
liste = [i for i in range(0, 21)]
liste2 = [i for i in range(0, 21, 3)]

# Ex 4
def OppListe(liste):
    for i in range(len(liste)):
        for x in range(len(liste[i])):
            liste[i][x] = -liste[i][x]
    return liste

L = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(L)

liste_finale = OppListe(L)
print(liste_finale)