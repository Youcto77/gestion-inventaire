import json
import os


name_fils = "bdd.json"
if not os.path.exists(name_fils):
    # Créer le fichier avec un inventaire vide s'il n'existe pas
    with open(name_fils, "w") as fichier:
        fichier.write("[]")
    print("L'inventaire a été créé avec succès !")
else:
    print("Le fichier d'inventaire existe déjà.")

def open_inventary():

    with open("bdd.json", "r") as fichier:
        bdd = json.load(fichier)
    print("------------------------------------")
    print()
    print("\nVoici la liste des produits :")
    print()
    print("------------------------------------")
    for produit in bdd:
        print(f"Produit : {produit['Produit']}")
        print(f" Quantité : {produit['Quantite']} unités")
        print(f" Prix : {produit['Prix']} € / unité")
        print("------------------------------------")

def add_products():
    
    with open('bdd.json', "r") as fichier:
        bdd = json.load(fichier)

    nom = input("Quel est le produit que vous voulez ajouter ? : ")
    quantite = input("Combien de ce produit va-t-il avoir en stock ? : ")
    prix = input("Quel est le prix à l'unité du produit ? : ")
    nouveaux_produit = {"Produit": nom, "Quantite": quantite, "Prix": prix}
    bdd.append(nouveaux_produit)  

    with open("bdd.json", "w") as fichier:
        json.dump(bdd, fichier, indent=4)

def delete_products():

    with open("bdd.json", "r") as fichier:
        bdd = json.load(fichier)

    nom = input("Quel est le nom du produit que vous voulez supprimer :")
    for produit in bdd:
        if produit["Produit"] == nom:
            bdd.remove(produit)
            print(f"Le produit {nom} a été supprimé de l'inventaire !")
        else:
            print("Une erreur est survenu lors de la suppréssions d'un produit")
    with open("bdd.json", "w") as fichier:
        json.dump(bdd, fichier, indent=4)

def updates_quantity():

    with open("bdd.json", "r") as fichier:
        bdd = json.load(fichier)

    nom = input("Quel est le produit que vous voullez mettre a jour sa quantite ? : ")
    quantite = int(input("Quelle est sa nouvelle quantite ? : "))

    for produit in bdd:
        if produit["Produit"] == nom:
            produit["Quantite"] = quantite  # Mettre à jour la quantité
            print(f"La quantité du produit '{nom}' a bien été modifiée à {quantite} unités.")
        else:
            print(f"Une erreur s'est produite lors de la maise ajour du produit {nom}")

    with open("bdd.json", "w") as fichier:
        json.dump(bdd, fichier, indent=4)

def updates_price():

    with open("bdd.json", "r") as fichier:
        bdd = json.load(fichier)

    nom = input("Quel est le produit que vous voullez mettre a jour son prix ? : ")
    prix = int(input("Quelle est son nouveaux prix ? : "))

    for produit in bdd:
        if produit["Produit"] == nom:
            produit["Prix"] = prix
            print(f"Le produit {nom} a un nouveaux prix de {prix}€.")
        else:
            print(f"Une erreur s'est produit lors du changement du prux du produit {nom}")

    with open("bdd.json", "w") as fichier:
        json.dump(bdd, fichier, indent=4)


def out_of_stock():

    with open("bdd.json", "r") as fichier:
        bdd = json.load(fichier)

    for produit in bdd:
        try:
            quantite = int(produit["Quantite"])
            if quantite < 5:
                print(f"Le produit '{produit["Produit"]}' est en rupture de stock ({quantite} unités restantes).")
        except ValueError:
            print("Aucun produit en rupture de stock.")

        with open("bdd.json", "w") as fichier:
            json.dump(bdd, fichier, indent=4)
        
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
        open_inventary()
    elif choix == "2":
        add_products()
    elif choix == "3":
        delete_products()
    elif choix == "4":
        updates_quantity()
    elif choix == "5":
        updates_price()
    elif choix == "6":
        out_of_stock()
    elif choix == "7":
        print("Vous allez quitter.")
        break
    else:
        print("Option invalide !")

