import random


def determiner_potion_huile_faible(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_objet_magique = 'arme magique'
        type = 'huile'
        valeur = 50
    if 4 <= resultat <= 6:
        nom_objet_magique = 'armure du mage'
        type = 'potion'
        valeur = 50
    if 7 <= resultat <= 9:
        nom_objet_magique = 'bouclier de la foi (+2)'
        type = 'potion'
        valeur = 50
    if 10 <= resultat <= 12:
        nom_objet_magique = 'endurance aux énergies destructives'
        type = 'potion'
        valeur = 50
    if resultat == 13:
        nom_objet_magique = 'gourdin magique'
        type = 'huile'
        valeur = 50
    if 14 <= resultat <= 15:
        nom_objet_magique = 'invisibilité pour les animaux'
        type = 'potion'
        valeur = 50
    if 16 <= resultat <= 17:
        nom_objet_magique = 'invisibilité pour les morts-vivants'
        type = 'potion'
        valeur = 50
    if 18 <= resultat <= 20:
        nom_objet_magique = 'morsure magique'
        type = 'potion'
        valeur = 50
    if resultat == 21:
        nom_objet_magique = 'passage sans trace'
        type = 'potion'
        valeur = 50
    if resultat == 22:
        nom_objet_magique = 'pierre magique'
        type = 'huile'
        valeur = 50
    if 23 <= resultat <= 24:
        nom_objet_magique = 'protection contre (un alignement)'
        type = 'potion'
        valeur = 50
    if 25 <= resultat <= 26:
        nom_objet_magique = 'regain d\'assurance'
        type = 'potion'
        valeur = 50
    if resultat == 27:
        nom_objet_magique = 'sanctuaire'
        type = 'potion'
        valeur = 50
    if 28 <= resultat <= 29:
        nom_objet_magique = 'saut'
        type = 'potion'
        valeur = 50
    if 30 <= resultat <= 39:
        nom_objet_magique = 'soins légers'
        type = 'potion'
        valeur = 50
    if 40 <= resultat <= 41:
        nom_objet_magique = 'bénédiction d\'arme'
        type = 'huile'
        valeur = 100
    if 42 <= resultat <= 45:
        nom_objet_magique = 'agrandissement'
        type = 'potion'
        valeur = 200
    if resultat == 45:
        nom_objet_magique = 'rapetissement'
        type = 'potion'
        valeur = 200
    if 46 <= resultat <= 47:
        nom_objet_magique = 'aide'
        type = 'potion'
        valeur = 300
    if resultat == 48:
        nom_objet_magique = 'alignement indétectable'
        type = 'potion'
        valeur = 300
    if resultat == 49:
        nom_objet_magique = 'bouclier de la foi (+3)'
        type = 'potion'
        valeur = 300
    if 50 <= resultat <= 51:
        nom_objet_magique = 'délivrance de la paralysie'
        type = 'potion'
        valeur = 300
    if resultat == 52:
        nom_objet_magique = 'détection faussée'
        type = 'potion'
        valeur = 300
    if 53 <= resultat <= 55:
        nom_objet_magique = 'endurance de l\'ours'
        type = 'potion'
        valeur = 300
    if 56 <= resultat <= 58:
        nom_objet_magique = 'flou'
        type = 'potion'
        valeur = 300
    if 59 <= resultat <= 61:
        nom_objet_magique = 'force de taureau'
        type = 'potion'
        valeur = 300
    if 62 <= resultat <= 64:
        nom_objet_magique = 'grâce féline'
        type = 'potion'
        valeur = 300
    if 65 <= resultat <= 67:
        nom_objet_magique = 'invisibilité'
        resultat = random.randint(1, 2)
        if resultat == 1:
            type = 'potion'
        else:
            type = 'huile'
        valeur = 300
    if 68 <= resultat <= 69:
        nom_objet_magique = 'lévitation'
        resultat = random.randint(1, 2)
        if resultat == 1:
            type = 'potion'
        else:
            type = 'huile'
        valeur = 300
    if 70 <= resultat <= 71:
        nom_objet_magique = 'patte d\'araignée'
        type = 'potion'
        valeur = 300
    if 72 <= resultat <= 74:
        nom_objet_magique = 'peau d\'écorce (+2)'
        type = 'potion'
        valeur = 300
    if 75 <= resultat <= 76:
        nom_objet_magique = 'protection contre les projectiles (10/magie)'
        type = 'potion'
        valeur = 300
    if 77 <= resultat <= 79:
        nom_objet_magique = 'ralentissement du poison'
        type = 'potion'
        valeur = 300
    if 80 <= resultat <= 82:
        nom_objet_magique = 'résistance aux énergies destructives (une énergie, 10)'
        type = 'potion'
        valeur = 300
    if 83 <= resultat <= 85:
        nom_objet_magique = 'restauration partielle'
        type = 'potion'
        valeur = 300
    if 86 <= resultat <= 87:
        nom_objet_magique = 'ruse du renard'
        type = 'potion'
        valeur = 300
    if 88 <= resultat <= 89:
        nom_objet_magique = 'sagesse du hibou'
        type = 'potion'
        valeur = 300
    if 90 <= resultat <= 94:
        nom_objet_magique = 'soins modérés'
        type = 'potion'
        valeur = 300
    if 95 <= resultat <= 96:
        nom_objet_magique = 'splendeur de l\'aigle'
        type = 'potion'
        valeur = 300
    if resultat == 97:
        nom_objet_magique = 'ténèbres'
        type = 'huile'
        valeur = 300
    if 98 <= resultat <= 100:
        nom_objet_magique = 'vision dans le noir'
        type = 'potion'
        valeur = 300
    nom_objet_magique = f'{type} de {nom_objet_magique}'
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_potion_huile_intermediaire(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 2:
        nom_objet_magique = 'bénédiction d\'arme'
        type = 'huile'
        valeur = 100
    if 3 <= resultat <= 4:
        nom_objet_magique = 'agrandissement'
        type = 'potion'
        valeur = 200
    if resultat == 5:
        nom_objet_magique = 'rapetissement'
        type = 'potion'
        valeur = 200
    if resultat == 6:
        nom_objet_magique = 'aide'
        type = 'potion'
        valeur = 300
    if resultat == 7:
        nom_objet_magique = 'alignement indétectable'
        type = 'potion'
        valeur = 300
    if 8 <= resultat <= 9:
        nom_objet_magique = 'bouclier de la foi (+3)'
        type = 'potion'
        valeur = 300
    if resultat == 10:
        nom_objet_magique = 'délivrance de la paralysie'
        type = 'potion'
        valeur = 300
    if resultat == 11:
        nom_objet_magique = 'détection faussée'
        type = 'potion'
        valeur = 300
    if 12 <= resultat <= 14:
        nom_objet_magique = 'endurance de l\'ours'
        type = 'potion'
        valeur = 300
    if 15 <= resultat <= 17:
        nom_objet_magique = 'flou'
        type = 'potion'
        valeur = 300
    if 18 <= resultat <= 20:
        nom_objet_magique = 'force de taureau'
        type = 'potion'
        valeur = 300
    if 21 <= resultat <= 23:
        nom_objet_magique = 'grâce féline'
        type = 'potion'
        valeur = 300
    if 24 <= resultat <= 25:
        nom_objet_magique = 'invisibilité'
        resultat = random.randint(1, 2)
        if resultat == 1:
            type = 'potion'
        else:
            type = 'huile'
        valeur = 300
    if resultat == 26:
        nom_objet_magique = 'lévitation'
        resultat = random.randint(1, 2)
        if resultat == 1:
            type = 'potion'
        else:
            type = 'huile'
        valeur = 300
    if resultat == 27:
        nom_objet_magique = 'patte d\'araignée'
        type = 'potion'
        valeur = 300
    if resultat == 28:
        nom_objet_magique = 'peau d\'écorce (+2)'
        type = 'potion'
        valeur = 300
    if resultat == 29:
        nom_objet_magique = 'protection contre les projectiles (10/magie)'
        type = 'potion'
        valeur = 300
    if resultat == 30:
        nom_objet_magique = 'ralentissement du poison'
        type = 'potion'
        valeur = 300
    if 31 <= resultat <= 32:
        nom_objet_magique = 'résistance aux énergies destructives (une énergie, 10)'
        type = 'potion'
        valeur = 300
    if resultat == 33:
        nom_objet_magique = 'restauration partielle'
        type = 'potion'
        valeur = 300
    if 34 <= resultat <= 35:
        nom_objet_magique = 'ruse du renard'
        type = 'potion'
        valeur = 300
    if 36 <= resultat <= 37:
        nom_objet_magique = 'sagesse du hibou'
        type = 'potion'
        valeur = 300
    if 38 <= resultat <= 45:
        nom_objet_magique = 'soins modérés'
        type = 'potion'
        valeur = 300
    if 46 <= resultat <= 47:
        nom_objet_magique = 'splendeur de l\'aigle'
        type = 'potion'
        valeur = 300
    if resultat == 48:
        nom_objet_magique = 'ténèbres'
        type = 'huile'
        valeur = 300
    if 49 <= resultat <= 50:
        nom_objet_magique = 'vision dans le noir'
        type = 'potion'
        valeur = 300
    if resultat == 51:
        nom_objet_magique = 'bouclier de la foi (+4)'
        type = 'potion'
        valeur = 600
    if resultat == 52:
        nom_objet_magique = 'peau d\'écorce(+3)'
        type = 'potion'
        valeur = 600
    if 53 <= resultat <= 55:
        nom_objet_magique = 'résistance aux énergies destructives (une énergie, 20)'
        type = 'potion'
        valeur = 700
    if 56 <= resultat <= 57:
        nom_objet_magique = 'Affûtage'
        type = 'huile'
        valeur = 750
    if 58 <= resultat <= 59:
        nom_objet_magique = 'Antidétection'
        type = 'potion'
        valeur = 750
    if 60 <= resultat <= 61:
        nom_objet_magique = 'Arme magique suprême (+1)'
        type = 'huile'
        valeur = 750
    if resultat == 62:
        nom_objet_magique = 'Cercle magique contre (un alignement)'
        type = 'potion'
        valeur = 750
    if resultat == 63:
        nom_objet_magique = 'Délivrance des malédictions'
        type = 'potion'
        valeur = 750
    if 64 <= resultat <= 66:
        nom_objet_magique = 'Déplacement'
        type = 'potion'
        valeur = 750
    if resultat == 67:
        nom_objet_magique = 'Don des langues'
        type = 'potion'
        valeur = 750
    if resultat == 68:
        nom_objet_magique = 'Etat gazeux'
        type = 'potion'
        valeur = 750
    if resultat == 69:
        nom_objet_magique = 'Flèches enflammées'
        type = 'huile'
        valeur = 750
    if resultat == 70:
        nom_objet_magique = 'Guérison de la cécité/surdité'
        type = 'potion'
        valeur = 750
    if resultat == 71:
        nom_objet_magique = 'Guérison des maladies'
        type = 'potion'
        valeur = 750
    if 72 <= resultat <= 74:
        nom_objet_magique = 'Héroïsme'
        type = 'potion'
        valeur = 750
    if resultat == 75:
        nom_objet_magique = 'Lumière du jour'
        type = 'huile'
        valeur = 750
    if resultat == 76:
        nom_objet_magique = 'Marche sur l\'onde'
        type = 'potion'
        valeur = 750
    if 77 <= resultat <= 78:
        nom_objet_magique = 'Morsure magique suprême (+1'
        type = 'potion'
        valeur = 750
    if 79 <= resultat <= 81:
        nom_objet_magique = 'Neutralisation du poison'
        type = 'potion'
        valeur = 750
    if 82 <= resultat <= 83:
        nom_objet_magique = 'Panoplie magique (+1)'
        type = 'huile'
        valeur = 750
    if 84 <= resultat <= 86:
        nom_objet_magique = 'Protection contre les énergies destructives (une énergie)'
        type = 'potion'
        valeur = 750
    if 87 <= resultat <= 88:
        nom_objet_magique = 'Rage'
        type = 'potion'
        valeur = 750
    if 89 <= resultat <= 90:
        nom_objet_magique = 'Rapidité'
        type = 'potion'
        valeur = 750
    if 91 <= resultat <= 92:
        nom_objet_magique = 'Respiration aquatique'
        type = 'potion'
        valeur = 750
    if 93 <= resultat <= 97:
        nom_objet_magique = 'Soins importants'
        type = 'potion'
        valeur = 750
    if 98 <= resultat <= 100:
        nom_objet_magique = 'Vol'
        type = 'potion'
        valeur = 750
    nom_objet_magique = f'{type} de {nom_objet_magique}'
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_potion_huile_puissant(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if resultat == 1:
        nom_objet_magique = 'alignement indétectable'
        type = 'potion'
        valeur = 300
    if resultat == 2:
        nom_objet_magique = 'bouclier de la foi (+3)'
        type = 'potion'
        valeur = 300
    if resultat == 3:
        nom_objet_magique = 'délivrance de la paralysie'
        type = 'potion'
        valeur = 300
    if 4 <= resultat <= 5:
        nom_objet_magique = 'flou'
        type = 'potion'
        valeur = 300
    if 6 <= resultat <= 7:
        nom_objet_magique = 'invisibilité'
        resultat = random.randint(1, 2)
        if resultat == 1:
            type = 'potion'
        else:
            type = 'huile'
        valeur = 300
    if resultat == 8:
        nom_objet_magique = 'restauration partielle'
        type = 'potion'
        valeur = 300
    if 9 <= resultat <= 13:
        nom_objet_magique = 'soins modérés'
        type = 'potion'
        valeur = 300
    if 14 <= resultat <= 15:
        nom_objet_magique = 'vision dans le noir'
        type = 'potion'
        valeur = 300
    if 16 <= resultat <= 17:
        nom_objet_magique = 'bouclier de la foi (+4)'
        type = 'potion'
        valeur = 600
    if resultat == 18:
        nom_objet_magique = 'peau d\'écorce(+3)'
        type = 'potion'
        valeur = 600
    if 19 <= resultat <= 20:
        nom_objet_magique = 'résistance aux énergies destructives (une énergie, 20)'
        type = 'potion'
        valeur = 700
    if 21 <= resultat <= 22:
        nom_objet_magique = 'Affûtage'
        type = 'huile'
        valeur = 750
    if 23 <= resultat <= 24:
        nom_objet_magique = 'Antidétection'
        type = 'potion'
        valeur = 750
    if resultat == 25:
        nom_objet_magique = 'Cercle magique contre (un alignement)'
        type = 'potion'
        valeur = 750
    if resultat == 26:
        nom_objet_magique = 'Délivrance des malédictions'
        type = 'potion'
        valeur = 750
    if 27 <= resultat <= 29:
        nom_objet_magique = 'Déplacement'
        type = 'potion'
        valeur = 750
    if resultat == 30:
        nom_objet_magique = 'Don des langues'
        type = 'potion'
        valeur = 750
    if resultat == 31:
        nom_objet_magique = 'Etat gazeux'
        type = 'potion'
        valeur = 750
    if resultat == 32:
        nom_objet_magique = 'Flèches enflammées'
        type = 'huile'
        valeur = 750
    if resultat == 33:
        nom_objet_magique = 'Guérison de la cécité/surdité'
        type = 'potion'
        valeur = 750
    if resultat == 34:
        nom_objet_magique = 'Guérison des maladies'
        type = 'potion'
        valeur = 750
    if 35 <= resultat <= 37:
        nom_objet_magique = 'Héroïsme'
        type = 'potion'
        valeur = 750
    if resultat == 38:
        nom_objet_magique = 'Lumière du jour'
        type = 'huile'
        valeur = 750
    if resultat == 39:
        nom_objet_magique = 'Marche sur l\'onde'
        type = 'potion'
        valeur = 750
    if 40 <= resultat <= 42:
        nom_objet_magique = 'Neutralisation du poison'
        type = 'potion'
        valeur = 750
    if 43 <= resultat <= 44:
        nom_objet_magique = 'Protection contre les énergies destructives (une énergie)'
        type = 'potion'
        valeur = 750
    if resultat == 45:
        nom_objet_magique = 'Rage'
        type = 'potion'
        valeur = 750
    if 46 <= resultat <= 47:
        nom_objet_magique = 'Rapidité'
        type = 'potion'
        valeur = 750
    if resultat == 48:
        nom_objet_magique = 'Respiration aquatique'
        type = 'potion'
        valeur = 750
    if 49 <= resultat <= 56:
        nom_objet_magique = 'Soins importants'
        type = 'potion'
        valeur = 750
    if 57 <= resultat <= 61:
        nom_objet_magique = 'Vol'
        type = 'potion'
        valeur = 750
    if resultat == 62:
        nom_objet_magique = 'Bouclier de la foi (+5)'
        type = 'potion'
        valeur = 900
    if 63 <= resultat <= 64:
        nom_objet_magique = 'Peau d\'écorce (+4)'
        type = 'potion'
        valeur = 900
    if resultat == 65:
        nom_objet_magique = 'Espoir'
        type = 'potion'
        valeur = 1050
    if 66 <= resultat <= 68:
        nom_objet_magique = 'Résistance aux énergies destructives (une énergie, 30)'
        type = 'potion'
        valeur = 1100
    if 69 <= resultat <= 72:
        nom_objet_magique = 'Arme magique suprême (+3)'
        type = 'huile'
        valeur = 1200
    if 73 <= resultat <= 76:
        nom_objet_magique = 'Morsure magique suprême (+2)'
        type = 'potion'
        valeur = 1200
    if 77 <= resultat <= 80:
        nom_objet_magique = 'Panoplie magique (+2)'
        type = 'huile'
        valeur = 1200
    if resultat == 81:
        nom_objet_magique = 'Peau d\'écorce (+5)'
        type = 'potion'
        valeur = 1200
    if resultat == 82:
        nom_objet_magique = 'Protection contre les projectiles (15/magie)'
        type = 'potion'
        valeur = 1500
    if 83 <= resultat <= 85:
        nom_objet_magique = 'Arme magique suprême (+3)'
        type = 'huile'
        valeur = 1800
    if 86 <= resultat <= 88:
        nom_objet_magique = 'Morsure magique suprême (+3)'
        type = 'potion'
        valeur = 1800
    if 89 <= resultat <= 91:
        nom_objet_magique = 'Panoplie magique (+3)'
        type = 'potion'
        valeur = 1800
    if 92 <= resultat <= 93:
        nom_objet_magique = 'Arme magique suprême (+4)'
        type = 'huile'
        valeur = 2400
    if 94 <= resultat <= 95:
        nom_objet_magique = 'Morsure magique suprême (+4)'
        type = 'potion'
        valeur = 2400
    if 96 <= resultat <= 97:
        nom_objet_magique = 'Panoplie magique (+4)'
        type = 'huile'
        valeur = 2400
    if resultat == 98:
        nom_objet_magique = 'Arme magique suprême (+5)'
        type = 'huile'
        valeur = 3000
    if resultat == 99:
        nom_objet_magique = 'Morsure magique suprême (+5)'
        type = 'potion'
        valeur = 3000
    if resultat == 100:
        nom_objet_magique = 'Panoplie magique (+5)'
        type = 'huile'
        valeur = 3000
    nom_objet_magique = f'{type} de {nom_objet_magique}'
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur

