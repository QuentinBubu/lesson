def tarif_carte(pass_type):
    if pass_type == "Jeune":
        return 50
    elif pass_type == "Senior":
        return 60
    else:
        print("Carte inconnue")
        
def plein_tarif(starter_city, finish_city):
    if starter_city == "Grenoble" and finish_city == "Paris" or starter_city == "Paris" and finish_city == "Grenoble":
        return 100
    elif starter_city == "Grenoble" and finish_city == "Lyon" or starter_city == "Lyon" and finish_city == "Grenoble":
        return 20
    elif starter_city == "Lyon" and finish_city == "Paris" or starter_city == "Paris" and finish_city == "Lyon":
        return 80
    else:
        print("Trajet inconnu")
        
def tarif_billet(starter_city, finish_city, period = None, pass_type = None, edit_ticket = True):
    price = plein_tarif(starter_city, finish_city)
    if price == None:
        return "Trajet inconnu"
    
    if pass_type == None and edit_ticket:
        return price*0.9
    elif pass_type == None:
        return price
        
    if period == "bleue":
        return price*0.5 if pass_type == "Jeune" or pass_type == "Senior" else print("Carte invalide")
    elif period == "blanche":
        if pass_type == "Jeune":
            return price*0.7
        elif pass_type == "Senior":
            return price*0.75
        else:
            print("Carte invalide")
    else:
        print("Erreur")