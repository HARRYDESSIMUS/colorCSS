def solde(prix,pourcentage):
    prixmoyen=prix*(pourcentage/100)
    prixsolde=prix-prixmoyen
    return prixsolde
print(solde(345,70))

def imc(poids,taille):
    resultat=poids/(taille**2)
    if resultat>=18.5 and resultat<=24.9:
        print(f"votre IMC est : {resultat} il est normal prenez soin de vous toujours")
    else:
         print(f"votre IMC est : {resultat} il n'est pas normal prenez soin de vous toujours")
imc(79,1.90)
