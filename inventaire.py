inventaire = []
mdp = "1234"
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
        produit_trouve = False
        for produit in inventaire:
            if produit[0] == nom:
                inventaire.remove(produit)
                print(f"Produit {nom} supprimé avec succès.")
                produit_trouve = True
                break 
        if not produit_trouve:
            print(f"Produit {nom} non trouvé dans l'inventaire.")
    else:
        print("Mot de passe incorrect !")

def ajour_quantite(nom, quantite):
    for produit in inventaire:
        if produit[0] == nom:
            produit[1] = quantite
    print(f"Le produit {nom} a bien été mis a jour !")

def ajour_prix(nom, prix):
    for produit in inventaire:
        if produit[0] == nom:
            produit[2] = prix
    print(f"Le prix du produit {nom} a été modifié")

def rupture_stock():
    for produit in inventaire:
        try:
            quantite = int(produit[1])
            if quantite < 5:
                print(f"Le produit '{produit[0]}' est en rupture de stock ({quantite} unités restantes).")
        except ValueError:
            print("Aucun produit en rupture de stock.")
        
while True:
    print("\nListe des options : ")
    print("1. Voire l'inventaire.")
    print("2. Ajouter un produit.")
    print("3. Supprimer un produit.")
    print("4. Mettre a jour la quantite d'un produit.")
    print("5. Mettre a jour le prix d'un produit.")
    print("6. Recherche de produit en rupture de stock.")
    print("7. Quitter.")
    choix = input("Choisissez une option : ")

    if choix == "1":
        ouvrire_inventaire()
    elif choix == "2":
        ajouter_produit()
    elif choix == "3":
        supprimer_produit()
    elif choix == "4":
        nom = input("Quelle est le nom du produit sur le quel vous voulez mettre a jour la quantite ? : ")
        quantite = input("Quelle est la nouvelle quantite ? : ")
        ajour_quantite(nom, quantite)
    elif choix == "5":
        nom = input("Quelle est le nom du produit sur le quel vous voulez mettre a jour le prix ? : ")
        prix = input("Quelle est le nouveaux prix : ")
        ajour_prix(nom, prix)
    elif choix == "6":
        rupture_stock()
    elif choix == "7":
        print("Vous allez quitter.")
        break
    else:
        print("Option invalide ! ahah")

