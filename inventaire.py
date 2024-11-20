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
        if os.path.exists(name_fils) and os.path.getsize(name_fils) == 0:
            print("Le fichier est vide.")
        else:
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
        print("Erreur lors du chargement de l'inventaire.")

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

    with open("stock.json", "r") as f:
        stock_data = json.load(f) 

    for produit in bdd:
        for stock_item in stock_data:
            try:
                quantite = int(produit["Quantite"])
                number_stock = int(stock_item["Rupture de stock a partir"])
            
                if quantite < number_stock:
                    print(f"Le produit '{produit['Produit']}' est en rupture de stock ({quantite} unités restantes).")
            except ValueError:
                print("Valeur incorrecte trouvée, vérifiez les données dans les fichiers JSON.")

    with open("bdd.json", "w") as fichier:
        json.dump(bdd, fichier, indent=4)

    with open("stock.json", "w") as f:
        json.dump(stock_data, f, indent=4)
   
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

def limite_rupture():
    with open("stock.json", "r") as fichier:
        stock = json.load(fichier)

        for info in stock:
            print("\n")
            print(f"Les produits seront en rupture de stock a partir de : {info["Rupture de stock a partir"]} exemplaire.")

    with open("stock.json", "w") as fichier:
        json.dump(stock, fichier, indent=4)

def modif_rupture():
    # Charger le fichier JSON
    with open("stock.json", "r") as fichier:
        stock = json.load(fichier)

    # Demander la valeur seuil pour la rupture de stock
    nombre = int(input("À partir de combien de produits en réserve sera-t-il considéré en rupture de stock ? : "))

    # Vérifier si le fichier contient déjà une entrée
    if stock:  # Si le fichier contient au moins une entrée
        try:
            stock[0]["Rupture de stock a partir"] = nombre
            print(f"La valeur de 'Rupture de stock a partir' a été mise à jour à {nombre}.")
        except:
            print("Une erreur s'est produite lors de la mise à jour.")
    else:  # Si le fichier est vide
        try:
            stock = [{"Rupture de stock a partir": nombre}]
            print(f"Aucune valeur existante. Une nouvelle valeur de 'Rupture de stock a partir' a été créée : {nombre}.")
        except:
            print("Une erreur s'est produite lors de la création d'une nouvelle valeur.")

    # Sauvegarder les modifications dans le fichier JSON
    try:
        with open("stock.json", "w") as fichier:
            json.dump(stock, fichier, indent=4)
            print("Les modifications ont été sauvegardées avec succès.")
    except:
        print("Une erreur s'est produite lors de la sauvegarde des modifications.")

def about_stock():
        
        while True:
            print("\nVoici les options pour gerer les parametre du stock :")
            print("1. Limite rupture de stock.")
            print("2. Modifier la limitie rupture de sotck.")
            print("3. Retour en arrière.")
            choix = input("Choisissez une option : ")

            if choix == "1":
                limite_rupture()
            elif choix == "2":
                modif_rupture()
            elif choix == "3":
                break
            else:
                print("ERREUR")

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