import random
import time


def determiner_objet_merveilleux_faible(valeur_objets_magiques, sheetlist):
    resultat = random.randint(1, 100)
    nom_objet_magique = sheetlist[0].cell(resultat, 1).value
    time.sleep(1)
    valeur = int(sheetlist[0].cell(resultat, 2).value)
    time.sleep(1)
    nombre_objet_magique = 1
    valeur_objets_magiques += valeur
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_objet_merveilleux_intermediaire(valeur_objets_magiques, sheetlist):
    resultat = random.randint(1, 100)
    nom_objet_magique = sheetlist[1].cell(resultat, 1).value
    time.sleep(1)
    valeur = int(sheetlist[1].cell(resultat, 2).value)
    time.sleep(1)
    nombre_objet_magique = 1
    valeur_objets_magiques += valeur
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_objet_merveilleux_puissant(valeur_objets_magiques, sheetlist):
    resultat = random.randint(1, 100)
    nom_objet_magique = sheetlist[2].cell(resultat, 1).value
    time.sleep(1)
    valeur = int(sheetlist[2].cell(resultat, 2).value)
    time.sleep(1)
    nombre_objet_magique = 1
    valeur_objets_magiques += valeur
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur
