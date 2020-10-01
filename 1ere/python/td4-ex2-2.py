def tarif_carte(pass_type):
    if pass_type == "Jeune":
        return 50
    elif pass_type == "Senior":
        return 60
    else:
        return "Carte inconnue"
        
def plein_tarif(starter_city, finish_city):
    if starter_city == finish_city:
        return "Erreur"
    if starter_city or finish_city == "Grenoble" and starter_city or finish_city == "Paris":
        return 100
    elif starter_city or finish_city == "Grenoble" and starter_city or finish_city == "Lyon":
        return 20
    elif starter_city or finish_city == "Lyon" and starter_city or finish_city == "Paris":
        return 80
    else:
        return "Trajet inconnu"
        
def tarif_billet(starter_city, finish_city, period = None, pass_type = None, edit_ticket = True):
    price = plein_tarif(starter_city, finish_city)
    if price == "Trajet inconnu":
        return "Trajet inconnu"
    
    if pass_type == None and not edit_ticket:
        return price*0.9
    elif pass_type == None:
        return price
        
    if period == "bleue":
        return price*0.5 if pass_type == "Jeune" or "Senior" else "Carte invalide"
    elif period == "blanche":
        if pass_type == "Jeune":
            return price*0.7
        elif pass_type == "Senior":
            return price*0.75
        else:
            return "Carte invalide"
    else:
        return "Erreur"