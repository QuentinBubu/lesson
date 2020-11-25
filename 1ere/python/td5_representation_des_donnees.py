d = {
     "nom": "Dupuis",
     "prenom": "Jacque",
     "age": 30
}

d["prenom"] = "Jacques"

for k in d.keys():
    print(k)
    
for v in d.values():
    print(v)
    
for k, v in d.items():
    print(f"{k} => {v}")
    
print(f"{d['prenom']} {d['nom']} a {d['age']} ans")

print(len(d))

dicoEtudiants = {
    "etudiant_1": 13,
    "etudiant_2": 17,
    "etudiant_3": 9,
    "etudiant_4": 15,
    "etudiant_5": 8,
    "etudiant_6": 14,
    "etudiant_7": 16,
    "etudiant_8": 12,
    "etudiant_9": 13,
    "etudiant_10": 15,
    "etudiant_11": 14,
    "etudiant_12": 9,
    "etudiant_13": 10,
    "etudiant_14": 12,
    "etudiant_15": 13,
    "etudiant_16": 7,
    "etudiant_17": 12,
    "etudiant_18": 15,
    "etudiant_19": 9,
    "etudiant_20": 17
}

dicoEtudiantAdmis = {}
dicoEtudiantNonAdmis = {}

for k, v in dicoEtudiants.items():
    if v >= 10:
        dicoEtudiantAdmis[k] = v
    else:
        dicoEtudiantNonAdmis[k] = v
    
def dicoVersNote(dico):
    moy = 0
    for v in dico.values():
        moy += v
    return round(moy/len(dico), 2)
    
    
print(f"""{dicoVersNote(dicoEtudiantAdmis)} de moyenne pour les étudiants admis,
{dicoVersNote(dicoEtudiantNonAdmis)} de moyenne pour les étudiants non admis,
et {dicoVersNote(dicoEtudiants)} de moyenne générale!""") 