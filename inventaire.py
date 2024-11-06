inventaire = []
mdp = "InventaireClv77"
separation = ("======================================================================")

def ouvrire_inventaire():
    print(separation)
    print("\nVoici la liste des produits :")
    for produit in inventaire:
        print("\n")
        print(f"{produit[0]} :\n  {produit[1]} en stock\n  {produit[2]}€/u\n")
    print(separation)

def ajouter_produit():
    nom = input("Quel est le produit que vous voulez ajouter ? : ")
    quantite = input("Combien de ce produit va-t-il avoir en stock ? : ")
    prix = input("Quel est le prix à l'unité du produit ? : ")
    inventaire.append([nom, quantite, prix])
    print(f"Produit ajouté : {nom}, Quantité : {quantite}, Prix : {prix}€ /u")

def supprimer_produit():
    nom = input("Quel est le nom du produit que vous voulez supprimer ? : ")
    securite = input("Mot de passe : ")
    
    if securite == mdp:
        # Vérifier si le produit existe
        produit_trouve = False
        for produit in inventaire:
            if produit[0] == nom:
                inventaire.remove(produit)
                print(f"Produit {nom} supprimé avec succès.")
                produit_trouve = True
                break  # Sortir de la boucle une fois le produit trouvé
        if not produit_trouve:
            print(f"Produit {nom} non trouvé dans l'inventaire.")
    else:
        print("Mot de passe incorrect !")

while True:
    print("\nListe des options : ")
    print("1. Voire l'inventaire.")
    print("2. Ajouter un produit.")
    print("3. Supprimer un produit.")
    print("4. Quitter.")
    choix = input("Choisissez une option : ")

    if choix == "1":
        ouvrire_inventaire()
    elif choix == "2":
        ajouter_produit()
    elif choix == "3":
        supprimer_produit()
    elif choix == "4":
        print("Vous allez quitter.")
        break
    else:
        print("Option invalide ! ahah")


#A garder

#from random import*
#for i in range (10):
    #x=randint(1,6)
    #print(x)

