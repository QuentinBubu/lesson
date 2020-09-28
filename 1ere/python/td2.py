def maFacture(prixUnitaire, quantite):
    return prixUnitaire*quantite
    
def maFacture2(prixUnitaire, quantite):
    prix = prixUnitaire*quantite
    if prix >= 100:
        prix -= prix*0.15
    return prix
    
def maFacture3(prixUnitaire, quantite):
    prixU = prixUnitaire*quantite
    if prixU >= 100:
        prix = prixU-prixU*0.15
    else:
        prix = prixU
    return f"Le prix sans réduction est de: {prixU} et le prix final est de {prix}"
    
def maFacture4(prixUnitaire, quantite, carteMagasin):
    prixU = prixUnitaire*quantite
    if prixU >= 100 and carteMagasin == "Oui":
        prix = prixU-prixU*0.15
    else:
        prix = prixU
    return f"Le prix sans réduction est de: {prixU} et le prix final est de {prix}"