# 1
mon_dico = {}
mon_dico["nom"] = "Durand"
mon_dico["prenom"] = "Christophe"
mon_dico["date_de_naissance"] = "29/02/1981"

# 2
print(f"Bonjours, je suis {mon_dico['prenom']} {mon_dico['nom']}, je suis né le {mon_dico['date_de_naissance']}")

# 3
mon_dico["lieu_de_naissance"] = "Bonneville"
print(f"à {mon_dico['lieu_de_naissance']}")

# 4
mes_fruits = {
    "poire": 3,
    "pomme": 4,
    "orange": 2
}

del mes_fruits["pomme"]

# 5
mes_fruits = {
    "poire": 3,
    "pomme": 4,
    "orange": 2
}

mes_fruits["pomme"] = mes_fruits["pomme"]-1

# 6
mes_fruits = {
    "poire": 3,
    "pomme": 4,
    "orange": 2
}

print("liste de fruits:")

for fruit in mes_fruits.keys():
    print(fruit)
    
# 7
mes_fruits = {
    "poire": 3,
    "pomme": 4,
    "orange": 2
}

for qte in mes_fruits.values():
    print(qte)

# 8
mes_fruits = {
    "poire": 3,
    "pomme": 4,
    "orange": 2
}

print("Stoke de fruits:")

for fruit, qte in mes_fruits.items():
    print(f"{fruit} : {qte}")
































