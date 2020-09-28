def maximum(nb1, nb2):
    return nb1 if nb1 > nb2 else nb2

def maximum3(nb1, nb2, nb3):
    return maximum(maximum(nb1, nb2), nb3)
    
def lundi(word):
    return f"{word} {word}"
    
def mardi(word):
    return f"{word}"*3 if len(word)%2 else f"{word}"*6
    
def mercredi(word):
    return f"impair" if len(word)%2 else f"{word}"
    
def jeudi(word):
    return word*(len(word)%3)
    
def vendredi(word):
    pass

def transforme(mot, num_jour):
    jours = [lundi(mot), mardi(mot), mercredi(mot), jeudi(mot), vendredi(mot)]
    return jours[num_jour-1]