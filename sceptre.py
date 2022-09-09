import random


def determiner_sceptre_intermediaire(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 7:
        nom_objet_magique = 'Sceptre de métamagie mineure, Extension de durée'
        valeur = 3000
    if 8 <= resultat <= 14:
        nom_objet_magique = 'Sceptre de métamagie mineure, Extension de portée'
        valeur = 3000
    if 15 <= resultat <= 21:
        nom_objet_magique = 'Sceptre de métamagie mineure, Incantation silencieuse'
        valeur = 3000
    if 22 <= resultat <= 28:
        nom_objet_magique = 'Scpetre inamovible'
        valeur = 7500
    if 29 <= resultat <= 35:
        nom_objet_magique = 'Sceptre de métamagie mineure, Extension d\'effet'
        valeur = 9000
    if 36 <= resultat <= 42:
        nom_objet_magique = 'Sceptre de détection des métaux et minéraux'
        valeur = 10500
    if 43 <= resultat <= 46:
        nom_objet_magique = 'Sceptre de métamagie modérée, Extension de durée'
        valeur = 11000
    if 47 <= resultat <= 50:
        nom_objet_magique = 'Sceptre de métamagie modérée, Extension de portée'
        valeur = 11000
    if 51 <= resultat <= 54:
        nom_objet_magique = 'Sceptre de métamagie modérée, Incantation silencieuse'
        valeur = 11000
    if 55 <= resultat <= 65:
        nom_objet_magique = 'Sceptre d\'oblitération'
        valeur = 11000
    if 66 <= resultat <= 71:
        nom_objet_magique = 'Sceptre merveilleux'
        valeur = 12000
    if 72 <= resultat <= 79:
        nom_objet_magique = 'Sceptre python'
        valeur = 13000
    if 80 <= resultat <= 83:
        nom_objet_magique = 'Scepgtre de métamagie mineure, Quintessence des sorts'
        valeur = 14000
    if 84 <= resultat <= 89:
        nom_objet_magique = 'Sceptre d\'extinction des feux'
        valeur = 15000
    if 90 <= resultat <= 97:
        nom_objet_magique = 'Sceptre vipère'
        valeur = 19000
    if 98 <= resultat <= 99:
        nom_objet_magique = 'Sceptre de métamagie modérée, Extension d\'effet'
        valeur = 32500
    if resultat == 100:
        nom_objet_magique = 'Sceptre de métamagie mineure, Incantation rapide'
        valeur = 35000
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_sceptre_puissant(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 2:
        nom_objet_magique = 'Sceptre de métamagie modérée, Extension de durée'
        valeur = 11000
    if 3 <= resultat <= 4:
        nom_objet_magique = 'Sceptre de métamagie modérée, Extension de portée'
        valeur = 11000
    if 5 <= resultat <= 6:
        nom_objet_magique = 'Sceptre de métamagie modérée, Incantation silencieuse'
        valeur = 11000
    if 7 <= resultat <= 10:
        nom_objet_magique = 'Sceptre d\'oblitération'
        valeur = 11000
    if 11 <= resultat <= 14:
        nom_objet_magique = 'Sceptre merveilleux'
        valeur = 12000
    if 15 <= resultat <= 18:
        nom_objet_magique = 'Sceptre python'
        valeur = 13000
    if 19 <= resultat <= 21:
        nom_objet_magique = 'Sceptre d\'extinction des feux'
        valeur = 15000
    if 22 <= resultat <= 25:
        nom_objet_magique = 'Sceptre vipère'
        valeur = 19000
    if 26 <= resultat <= 30:
        nom_objet_magique = 'Sceptre de détection de l\'hostilité'
        valeur = 19000
    if 31 <= resultat <= 36:
        nom_objet_magique = 'Sceptre de métamagie majeure, Extension de durée'
        valeur = 24500
    if 36 <= resultat <= 42:
        nom_objet_magique = 'Sceptre de métamagie majeure, Extension de portée'
        valeur = 24500
    if 43 <= resultat <= 48:
        nom_objet_magique = 'Sceptre de métamagie majeure, Incantation silencieuse'
        valeur = 24500
    if 49 <= resultat <= 53:
        nom_objet_magique = 'Sceptre de flétrissement'
        valeur = 25000
    if 54 <= resultat <= 58:
        nom_objet_magique = 'Sceptre de prestance'
        valeur = 25000
    if 59 <= resultat <= 64:
        nom_objet_magique = 'Sceptre de métamagie modérée, Extension d\'effet'
        valeur = 32500
    if 65 <= resultat <= 69:
        nom_objet_magique = 'Sceptre d\'orage'
        valeur = 33000
    if 70 <= resultat <= 73:
        nom_objet_magique = 'Sceptre de métamagie mineure, Incantation rapide'
        valeur = 35000
    if 74 <= resultat <= 77:
        nom_objet_magique = 'Sceptre d\'annulation'
        valeur = 37000
    if 78 <= resultat <= 80:
        nom_objet_magique = 'Sceptre d\'absorption'
        valeur = 50000
    if 81 <= resultat <= 84:
        nom_objet_magique = 'Sceptre de grand fléau'
        valeur = 50000
    if 85 <= resultat <= 86:
        nom_objet_magique = 'Sceptre de métamagie modérée, Quintessence des sorts'
        valeur = 54000
    if 87 <= resultat <= 88:
        nom_objet_magique = 'Sceptre de suzeraineté'
        valeur = 60000
    if 89 <= resultat <= 90:
        nom_objet_magique = 'Sceptre de sécurité'
        valeur = 61000
    if 91 <= resultat <= 92:
        nom_objet_magique = 'Sceptre de seigneurs de la guerre'
        valeur = 70000
    if 93 <= resultat <= 94:
        nom_objet_magique = 'Sceptre de métamagie majeure, Extension d\'effet'
        valeur = 73000
    if 95 <= resultat <= 96:
        nom_objet_magique = 'Sceptre de métamagie majeure, Incantation rapide'
        valeur = 75500
    if 97 <= resultat <= 98:
        nom_objet_magique = 'Sceptre d\'éternelle vigilance'
        valeur = 85000
    if resultat == 99:
        nom_objet_magique = 'Sceptre de métamagie majeure, Quintessence des sorts'
        valeur = 121500
    if resultat == 100:
        nom_objet_magique = 'Sceptre de métamagie majeure, Incantation rapide'
        valeur = 170000
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur

