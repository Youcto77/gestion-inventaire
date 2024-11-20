import json
import os
import time
import sys


name_fils = "bdd.json"
if not os.path.exists(name_fils):
    with open(name_fils, "w") as fichier:
        fichier.write("[]")
    print("L'inventaire a été créé avec succès !")
else:
    print("Le fichier d'inventaire existe déjà.")

name_fils_stock = "stock.json"
if not os.path.exists(name_fils_stock):
    with open(name_fils_stock, "w") as f:
        f.write("[]")
    print("Le fichier pour le stock a aussi été créer avec succès !")
else:
    print("Le fichier de stock existe deja !")


def open_inventary():
    try: 
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
    except:
        print("ERROR")

def add_products():
    
    with open('bdd.json', "r") as fichier:
        bdd = json.load(fichier)

    nom = input("Quel est le produit que vous voulez ajouter ? : ")
    quantite = int(input("Combien de ce produit va-t-il avoir en stock ? : "))
    prix = int(input("Quel est le prix à l'unité du produit ? : "))
    nouveaux_produit = {"Produit": nom, "Quantite": quantite, "Prix": prix}
    try:
        bdd.append(nouveaux_produit)  
    except:
        print("Error lors de l'ajout du produit dans l'inventaire !")

    with open("bdd.json", "w") as fichier:
        json.dump(bdd, fichier, indent=4)

def delete_products():

    with open("bdd.json", "r") as fichier:
        bdd = json.load(fichier)

    nom = input("Quel est le nom du produit que vous voulez supprimer :")
    for produit in bdd:
        if produit["Produit"] == nom:
            try:
                bdd.remove(produit)
            except:
                print("Error lors de la suppression d'un produits")
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
            try:
                produit["Quantite"] = quantite  
            except:
                print("Error lors de la mise a jour d'un produit !")
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
            try:
                produit["Prix"] = prix
            except:
                print("Error lors de la mise a jour d'un produit !")
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
        
def delete_all_inventary():
    with open("bdd.json", "r") as fichier:
        bdd = json.load(fichier)

        response = input("Voulez vous vraiment supprimer l'integralité de l'inventaire (oui/non) ? : ")
        if response == "oui":
            print("Chargement", end="")
            for _ in range(10):
                time.sleep(0.5) 
                print(".", end="", flush=True)  
            print(" Terminé!")
            try:
                with open("bdd.json", "w") as f:
                    pass
                with open("bdd.json", "w") as f:
                    f.write("[]")
                    print("L'inventaire a été supprimé avec succès !")
            except:
                print("Error de la suppression totale de l'inventaire !")
        else:
            print("Annulation de l'inventaire !")

def rename_products():
    with open("bdd.json", "r") as fichier:
        bdd = json.load(fichier)

        name = input("Quelle est le nom du produit que vous voulez renommer ? : ")
        new_name = input(f"Quelle est le nouveaux nom que vous voulez donner à {name} ? : ")

        for produit in bdd:
            if produit["Produit"] == name:
                try:
                    produit["Produit"] = new_name
                except:
                    print("Error lors de la modification du nom d'un produit !")
                print(f"Vous avez modifié le nom du produit {name}")
            else:
                print(f"Une erreur est survenue lors de la modification du produit : {name}")

        with open("bdd.json", "w") as fichier:
            json.dump(bdd, fichier, indent=4)

def about_stock():
    with open("stock.json", "r") as fichier:
        stock = json.load(fichier)

        msg = input("A partir de combien de produits, les produits seront en rupture de stock ? : ")
        try:
            msg = {"Rupture de stock a partir": msg}
            stock.append(msg)
        except:
            print("Une erreur est survenu lors de l'ajout du gérage de stock !")

    with open("stock.json", "w") as fichier:
            json.dump(stock, fichier, indent=4)

while True:
    print("\nListe des options : ")
    print("1. Voire l'inventaire.")
    print("2. Ajouter un produit.")
    print("3. Supprimer un produit.")
    print("4. Mettre a jour la quantite d'un produit.")
    print("5. Mettre a jour le prix d'un produit.")
    print("6. Recherche de produit en rupture de stock.")
    print("7. Supprimer l'intégralité de l'inventaire.")
    print("8. Modifier le nom d'un produit.")
    print("9. Informations sur le stock.")
    print("10. Quitter.")
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
        delete_all_inventary()
    elif choix == "8":
        rename_products()
    elif choix == "9":
        about_stock()
    elif choix == "10":
        print("Vous allez quitter.")
        break
    else:
        print("Option invalide !")