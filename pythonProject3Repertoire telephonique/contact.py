# 0 pour quitter
# 1 escritoire dans le repertoire
# 2 pour faire la recherche
# on entre son choix
import os


def menu():
    print(" 0 : Quitter")
    print(" 1 : Enregistrer un numero")
    print(" 2 : Recherche un numero")
    print(" 3 pour supprimer")
    print(" 4 pour envoyer un message")
    print(" 5 pour lister l'ensemnle de données")


menu()

# entrez son choix

choix = int(input("Entrez votre choix : "))

if choix == 0:
    print("0 vous quittez le repertoire")
while choix == 1:
    nom = input("Entrez votre Nom : ")
    if nom == "0":  # si nom est egale a 0 affichons le menu et affiche entrez le choix
        print(menu())
        choix = int(input("Entrez votre choix : "))
    else:
        num = input("telephone : ")
        monfichier = open("numero.txt", "a")  # j'ouvre mon fichier txt
        choix = monfichier.write(nom)  # ajouter les noms  a mon fichier
        monfichier.write(":")  # nom = numero
        monfichier.write(num)  # ajouter les numeros a mon fichier
        monfichier.write("\n")
        monfichier.close()
        print("Numero enregistrer avec succès")

while choix == 2:
    print("vous recherchez quel contact ? ")
    nom = input("Entrez le nom de la personne :")
    if nom == "0":
        print(menu())
        choix = int(input("Entrez votre choix : "))
    else:
        monfichier = open("numero.txt")
        for line in monfichier:  # on parcour le fichier2
            if line.startswith(nom):  # affichons d'abord le nom
                print(line)
                break

while choix == 3:
    nom = input("Entrez le nom a modifier :")
    if nom == "0":
        print(menu())
        choix = int(input("Entrez votre choix : "))
    else:
        nouveau_nom = input("Entrez un nouveau nom")
        # modifier les donnees
        with open("numero.txt", "r+") as fichier:
            monfichier = fichier.readlines()  # lire le contenu du fichier
            for i in range(len(monfichier)):
                if nom in monfichier[i]:
                    monfichier[i] = monfichier[i].replace(nom, nouveau_nom)
                    # renisialiser le curseur au debut du fichier
                    fichier.seek(0)  # reutiliser la position au debut du curseur
                    # ecrire les donnees modifiées dans le fichier
                    fichier.writelines(monfichier)
                    fichier.close()
                    print("le Nom a été modifier avec succès")
                    break
while choix == 4:
    nom = input("Entrez le nom a Supprimer :")
    if nom == "0":
        print(menu())
        choix = int(input("Entrez votre choix : "))
    else:
        print("Voulez-vous supprimer :", nom)
        print("si oui tapez 6 pour supprimer ou zero pour sortir")
        nom = input("Entrez la valeur")
        if nom == "0":
            print()
        elif nom == "6":
            # modifier les donnees
            with open("numero.txt", "r") as fichier:
                monfichier = fichier.readlines()  # lire le contenu du fichier
                fichierd = [line for line in monfichier if
                            nom not in line]
                with open("numero.txt", "w") as fichie:
                    fichie.writelines(fichierd) #ecris le vide
                print("contact supprimer")
        else:
            print("contact nom supprimer")
            break
while choix == 5:
    print("la liste de votre repertoire")

    with open('numero.txt', 'r') as fichier:
        monfichier = fichier.readlines()
    for ligne in monfichier:
        print(ligne.strip())
    break