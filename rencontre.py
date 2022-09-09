from utils import lancer_des, lancer_gemme, lancer_objet_art, tirer_objet_non_magique, determiner_objet_magique_faible, \
    determiner_objet_magique_intermediaire, determiner_objet_magique_puissant
import random

"""Permet de définir les items avant l'appel des autres fonctions"""


def rencontre(niveau_rencontre, facteur_tresor, sheetlist):
    # tirage aleatoire du tresor en pieces
    piece_cuivre = piece_argent = piece_or = piece_platine = gemmes = objets_arts = objets_non_magiques = 0
    objet_magique_faible = objet_magique_intermediaire = objet_magique_puissant = 0
    # tirage niveau 1
    if niveau_rencontre == "1":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 15 <= resultat <= 29:
                piece_cuivre += lancer_des(1, 6) * 1000
            if 30 <= resultat <= 52:
                piece_argent += lancer_des(1, 8) * 100
            if 53 <= resultat <= 95:
                piece_or += lancer_des(2, 8) * 10
            if 96 <= resultat <= 100:
                piece_platine += lancer_des(1, 3) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 91 <= resultat <= 95:
                gemmes += 1
            if 96 <= resultat <= 100:
                objets_arts += 1
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 75 <= resultat <= 95:
                objets_non_magiques += 1
            if 96 <= resultat <= 100:
                objet_magique_faible += 1
            objets_tires += 1
    # tirage niveau 2
    if niveau_rencontre == "2":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 14 <= resultat <= 23:
                piece_cuivre += lancer_des(1, 10) * 1000
            if 24 <= resultat <= 43:
                piece_argent += lancer_des(2, 10) * 100
            if 44 <= resultat <= 95:
                piece_or += lancer_des(4, 10) * 10
            if 96 <= resultat <= 100:
                piece_platine += lancer_des(1, 4) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 82 <= resultat <= 95:
                gemmes += lancer_des(1, 3)
            if 96 <= resultat <= 100:
                objets_arts += lancer_des(1, 3)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 50 <= resultat <= 85:
                objets_non_magiques += 1
            if 86 <= resultat <= 100:
                objet_magique_faible += 1
            objets_tires += 1
    # tirage niveau 3
    if niveau_rencontre == "3":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 12 <= resultat <= 21:
                piece_cuivre += lancer_des(2, 10) * 1000
            if 22 <= resultat <= 41:
                piece_argent += lancer_des(4, 8) * 100
            if 42 <= resultat <= 95:
                piece_or += lancer_des(1, 4) * 100
            if 96 <= resultat <= 100:
                piece_platine += lancer_des(1, 6) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 78 <= resultat <= 95:
                gemmes += lancer_des(1, 3)
            if 96 <= resultat <= 100:
                objets_arts += lancer_des(1, 3)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 50 <= resultat <= 79:
                objets_non_magiques += lancer_des(1, 3)
            if 80 <= resultat <= 100:
                objet_magique_faible += 1
            objets_tires += 1
    # tirage niveau 4
    if niveau_rencontre == "4":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 12 <= resultat <= 21:
                piece_cuivre += lancer_des(3, 10) * 1000
            if 22 <= resultat <= 41:
                piece_argent += lancer_des(4, 12) * 100
            if 42 <= resultat <= 95:
                piece_or += lancer_des(1, 6) * 100
            if 96 <= resultat <= 100:
                piece_platine += lancer_des(1, 8) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 71 <= resultat <= 95:
                gemmes += lancer_des(1, 4)
            if 96 <= resultat <= 100:
                objets_arts += lancer_des(1, 3)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 43 <= resultat <= 62:
                objets_non_magiques += lancer_des(1, 4)
            if 63 <= resultat <= 100:
                objet_magique_faible += 1
            objets_tires += 1
    # tirage niveau 5
    if niveau_rencontre == "5":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 11 <= resultat <= 19:
                piece_cuivre += lancer_des(1, 4) * 10000
            if 20 <= resultat <= 38:
                piece_argent += lancer_des(1, 6) * 1000
            if 39 <= resultat <= 95:
                piece_or += lancer_des(1, 8) * 100
            if 96 <= resultat <= 100:
                piece_platine += lancer_des(1, 10) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 61 <= resultat <= 95:
                gemmes += lancer_des(1, 4)
            if 96 <= resultat <= 100:
                objets_arts += lancer_des(1, 4)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 58 <= resultat <= 67:
                objets_non_magiques += lancer_des(1, 4)
            if 68 <= resultat <= 100:
                objet_magique_faible += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 6
    if niveau_rencontre == "6":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 11 <= resultat <= 18:
                piece_cuivre += lancer_des(1, 6) * 10000
            if 19 <= resultat <= 37:
                piece_argent += lancer_des(1, 8) * 1000
            if 38 <= resultat <= 95:
                piece_or += lancer_des(1, 10) * 100
            if 96 <= resultat <= 100:
                piece_platine += lancer_des(1, 12) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 57 <= resultat <= 92:
                gemmes += lancer_des(1, 4)
            if 93 <= resultat <= 100:
                objets_arts += lancer_des(1, 4)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 55 <= resultat <= 59:
                objets_non_magiques += lancer_des(1, 4)
            if 60 <= resultat <= 99:
                objet_magique_faible += lancer_des(1, 3)
            if resultat == 100:
                objet_magique_intermediaire += 1
            objets_tires += 1
    # tirage niveau 7
    if niveau_rencontre == "7":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 12 <= resultat <= 18:
                piece_cuivre += lancer_des(1, 10) * 10000
            if 19 <= resultat <= 35:
                piece_argent += lancer_des(1, 12) * 1000
            if 36 <= resultat <= 93:
                piece_or += lancer_des(2, 6) * 100
            if 94 <= resultat <= 100:
                piece_platine += lancer_des(3, 4) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 49 <= resultat <= 88:
                gemmes += lancer_des(1, 4)
            if 89 <= resultat <= 100:
                objets_arts += lancer_des(1, 4)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 52 <= resultat <= 97:
                objet_magique_faible += lancer_des(1, 3)
            if 68 <= resultat <= 100:
                objet_magique_intermediaire += 1
            objets_tires += 1
    # tirage niveau 8
    if niveau_rencontre == "8":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 11 <= resultat <= 15:
                piece_cuivre += lancer_des(1, 12) * 10000
            if 16 <= resultat <= 29:
                piece_argent += lancer_des(2, 6) * 1000
            if 30 <= resultat <= 87:
                piece_or += lancer_des(2, 8) * 100
            if 88 <= resultat <= 100:
                piece_platine += lancer_des(3, 6) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 46 <= resultat <= 85:
                gemmes += lancer_des(1, 6)
            if 86 <= resultat <= 100:
                objets_arts += lancer_des(1, 4)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 49 <= resultat <= 96:
                objet_magique_faible += lancer_des(1, 4)
            if 68 <= resultat <= 100:
                objet_magique_intermediaire += 1
            objets_tires += 1
    # tirage niveau 9
    if niveau_rencontre == "9":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 11 <= resultat <= 15:
                piece_cuivre += lancer_des(2, 6) * 10000
            if 16 <= resultat <= 29:
                piece_argent += lancer_des(2, 8) * 1000
            if 30 <= resultat <= 85:
                piece_or += lancer_des(5, 4) * 100
            if 86 <= resultat <= 100:
                piece_platine += lancer_des(2, 12) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 41 <= resultat <= 80:
                gemmes += lancer_des(1, 8)
            if 81 <= resultat <= 100:
                objets_arts += lancer_des(1, 4)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 44 <= resultat <= 91:
                objet_magique_faible += lancer_des(1, 4)
            if 92 <= resultat <= 100:
                objet_magique_intermediaire += 1
            objets_tires += 1
    # tirage niveau 10
    if niveau_rencontre == "10":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 11 <= resultat <= 24:
                piece_argent += lancer_des(2, 10) * 1000
            if 25 <= resultat <= 79:
                piece_or += lancer_des(6, 4) * 100
            if 80 <= resultat <= 100:
                piece_platine += lancer_des(5, 6) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 36 <= resultat <= 79:
                gemmes += lancer_des(1, 8)
            if 80 <= resultat <= 100:
                objets_arts += lancer_des(1, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 41 <= resultat <= 88:
                objet_magique_faible += lancer_des(1, 4)
            if 58 <= resultat <= 67:
                objet_magique_intermediaire += 1
            if 68 <= resultat <= 100:
                objet_magique_puissant += 1
            objets_tires += 1
    # tirage niveau 11
    if niveau_rencontre == "11":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 9 <= resultat <= 14:
                piece_argent += lancer_des(3, 10) * 1000
            if 15 <= resultat <= 75:
                piece_or += lancer_des(4, 8) * 100
            if 76 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 10
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 25 <= resultat <= 74:
                gemmes += lancer_des(1, 10)
            if 75 <= resultat <= 100:
                objets_arts += lancer_des(1, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 32 <= resultat <= 84:
                objet_magique_faible += lancer_des(1, 4)
            if 85 <= resultat <= 98:
                objet_magique_intermediaire += 1
            if 99 <= resultat <= 100:
                objet_magique_puissant += 1
            objets_tires += 1
    # tirage niveau 12
    if niveau_rencontre == "12":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 9 <= resultat <= 14:
                piece_argent += lancer_des(3, 12) * 1000
            if 15 <= resultat <= 75:
                piece_or += lancer_des(1, 4) * 1000
            if 76 <= resultat <= 100:
                piece_platine += lancer_des(1, 4) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 18 <= resultat <= 70:
                gemmes += lancer_des(1, 10)
            if 71 <= resultat <= 100:
                objets_arts += lancer_des(1, 8)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 28 <= resultat <= 82:
                objet_magique_faible += lancer_des(1, 6)
            if 83 <= resultat <= 97:
                objet_magique_intermediaire += 1
            if 98 <= resultat <= 100:
                objet_magique_puissant += 1
            objets_tires += 1
    # tirage niveau 13
    if niveau_rencontre == "13":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 9 <= resultat <= 75:
                piece_or += lancer_des(1, 4) * 1000
            if 76 <= resultat <= 100:
                piece_platine += lancer_des(1, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 12 <= resultat <= 66:
                gemmes += lancer_des(1, 12)
            if 67 <= resultat <= 100:
                objets_arts += lancer_des(1, 10)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 20 <= resultat <= 73:
                objet_magique_faible += lancer_des(1, 6)
            if 74 <= resultat <= 95:
                objet_magique_intermediaire += 1
            if 96 <= resultat <= 100:
                objet_magique_puissant += 1
            objets_tires += 1
    # tirage niveau 14
    if niveau_rencontre == "14":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 9 <= resultat <= 75:
                piece_or += lancer_des(1, 6) * 1000
            if 76 <= resultat <= 100:
                piece_platine += lancer_des(1, 12) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 12 <= resultat <= 66:
                gemmes += lancer_des(2, 8)
            if 67 <= resultat <= 100:
                objets_arts += lancer_des(2, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 20 <= resultat <= 58:
                objet_magique_faible += lancer_des(1, 6)
            if 59 <= resultat <= 92:
                objet_magique_intermediaire += 1
            if 93 <= resultat <= 100:
                objet_magique_puissant += 1
            objets_tires += 1
    # tirage niveau 15
    if niveau_rencontre == "15":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 4 <= resultat <= 74:
                piece_or += lancer_des(1, 8) * 1000
            if 75 <= resultat <= 100:
                piece_platine += lancer_des(3, 4) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 10 <= resultat <= 65:
                gemmes += lancer_des(2, 10)
            if 66 <= resultat <= 100:
                objets_arts += lancer_des(2, 8)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 12 <= resultat <= 46:
                objet_magique_faible += lancer_des(1, 10)
            if 47 <= resultat <= 90:
                objet_magique_intermediaire += 1
            if 91 <= resultat <= 100:
                objet_magique_puissant += 1
            objets_tires += 1
    # tirage niveau 16
    if niveau_rencontre == "16":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 4 <= resultat <= 74:
                piece_or += lancer_des(1, 12) * 1000
            if 75 <= resultat <= 100:
                piece_platine += lancer_des(3, 4) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 8 <= resultat <= 64:
                gemmes += lancer_des(4, 6)
            if 65 <= resultat <= 100:
                objets_arts += lancer_des(2, 10)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 41 <= resultat <= 46:
                objet_magique_faible += lancer_des(1, 10)
            if 47 <= resultat <= 90:
                objet_magique_intermediaire += lancer_des(1, 3)
            if 91 <= resultat <= 100:
                objet_magique_puissant += 1
            objets_tires += 1
    # tirage niveau 17
    if niveau_rencontre == "17":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 4 <= resultat <= 68:
                piece_or += lancer_des(3, 4) * 1000
            if 69 <= resultat <= 100:
                piece_platine += lancer_des(2, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 5 <= resultat <= 63:
                gemmes += lancer_des(4, 8)
            if 64 <= resultat <= 100:
                objets_arts += lancer_des(3, 8)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 34 <= resultat <= 84:
                objet_magique_intermediaire += lancer_des(1, 3)
            if 85 <= resultat <= 100:
                objet_magique_puissant += 1
            objets_tires += 1
    # tirage niveau 18
    if niveau_rencontre == "18":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(3, 6) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(5, 4) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 5 <= resultat <= 54:
                gemmes += lancer_des(3, 12)
            if 55 <= resultat <= 100:
                objets_arts += lancer_des(3, 10)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 25 <= resultat <= 80:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 81 <= resultat <= 100:
                objet_magique_puissant += 1
            objets_tires += 1
    # tirage niveau 19
    if niveau_rencontre == "19":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(3, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(3, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 4 <= resultat <= 50:
                gemmes += lancer_des(6, 6)
            if 51 <= resultat <= 100:
                objets_arts += lancer_des(6, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 5 <= resultat <= 70:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 71 <= resultat <= 100:
                objet_magique_puissant += 1
            objets_tires += 1
    # tirage niveau 20
    if niveau_rencontre == "20":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 21
    if niveau_rencontre == "21":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            objet_magique_puissant += 1
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 22
    if niveau_rencontre == "22":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            objet_magique_puissant += 2
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 23
    if niveau_rencontre == "23":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            objet_magique_puissant += 4
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 24
    if niveau_rencontre == "24":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            objet_magique_puissant += 6
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 25
    if niveau_rencontre == "25":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            objet_magique_puissant += 9
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 26
    if niveau_rencontre == "26":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            objet_magique_puissant += 12
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 27
    if niveau_rencontre == "27":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            objet_magique_puissant += 17
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 28
    if niveau_rencontre == "28":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            objet_magique_puissant += 23
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 29
    if niveau_rencontre == "29":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            objet_magique_puissant += 31
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1
    # tirage niveau 30
    if niveau_rencontre == "30":
        pieces_tirees = 0
        while pieces_tirees < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 65:
                piece_or += lancer_des(4, 8) * 1000
            if 66 <= resultat <= 100:
                piece_platine += lancer_des(4, 10) * 100
            pieces_tirees += 1
        # tirage des gemmes et objets d'arts
        biens_precieux_tires = 0
        while biens_precieux_tires < int(facteur_tresor):
            resultat = random.randint(1, 100)
            if 3 <= resultat <= 38:
                gemmes += lancer_des(4, 10)
            if 39 <= resultat <= 100:
                objets_arts += lancer_des(7, 6)
            biens_precieux_tires += 1
        # tirage des objets communs ou magiques
        objets_tires = 0
        while objets_tires < int(facteur_tresor):
            objet_magique_puissant += 42
            resultat = random.randint(1, 100)
            if 26 <= resultat <= 65:
                objet_magique_intermediaire += lancer_des(1, 4)
            if 66 <= resultat <= 100:
                objet_magique_puissant += lancer_des(1, 3)
            objets_tires += 1

    # Tirage du nom de la valeur des gemmes
    list_gemmes = {}
    valeur_des_gemmes = 0
    gemmes_estimees = 0
    while gemmes_estimees < gemmes:
        valeur_des_gemmes, valeur, nom_gemme = lancer_gemme(valeur_des_gemmes)
        if list_gemmes.get(nom_gemme):
            list_gemmes[nom_gemme]['nombre'] += 1
            list_gemmes[nom_gemme]['valeur'] += valeur
        else:
            list_gemmes[nom_gemme] = {'nombre': 1, 'valeur': valeur}
        gemmes_estimees += 1
    # Tirage du nom et de la valeur des objets d'art
    list_objets_arts = {}
    valeur_des_objets_arts = 0
    objets_arts_estimees = 0
    while objets_arts_estimees < objets_arts:
        valeur_des_objets_arts, valeur, nom_objet_art = lancer_objet_art(valeur_des_objets_arts)
        if list_objets_arts.get(nom_objet_art):
            list_objets_arts[nom_objet_art]['nombre'] += 1
            list_objets_arts[nom_objet_art]['valeur'] += valeur
        else:
            list_objets_arts[nom_objet_art] = {'nombre': 1, 'valeur': valeur}
        objets_arts_estimees += 1
    # Tirage des objets non magiques
    list_objets_non_magiques = {}
    valeur_objets_non_magiques = 0
    objets_non_magiques_definis = 0
    while objets_non_magiques_definis < objets_non_magiques:
        valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur = \
            tirer_objet_non_magique(valeur_objets_non_magiques)
        if list_objets_non_magiques.get(nom_objet_non_magique):
            list_objets_non_magiques[nom_objet_non_magique]['nombre'] += nombre_objet_non_magique
            list_objets_non_magiques[nom_objet_non_magique]['valeur'] += valeur
        else:
            list_objets_non_magiques[nom_objet_non_magique] = {'nombre': nombre_objet_non_magique, 'valeur': valeur}
        objets_non_magiques_definis += 1
    # Tirage des objets magiques faibles
    list_objets_magiques_faibles = {}
    valeur_objets_magiques = 0
    objets_magiques_faibles_definis = 0
    while objets_magiques_faibles_definis < objet_magique_faible:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
            determiner_objet_magique_faible(valeur_objets_magiques, sheetlist)
        if list_objets_magiques_faibles.get(nom_objet_magique):
            list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
            list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
        else:
            list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique, 'valeur': valeur}
        objets_magiques_faibles_definis += 1
    # Tirage des objets magiques intermediaires
    list_objets_magiques_intermediaires = {}
    valeur_objets_magiques = 0
    objets_magiques_intermediaires_definis = 0
    while objets_magiques_intermediaires_definis < objet_magique_intermediaire:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
            determiner_objet_magique_intermediaire(valeur_objets_magiques, sheetlist)
        if list_objets_magiques_intermediaires.get(nom_objet_magique):
            list_objets_magiques_intermediaires[nom_objet_magique]['nombre'] += nombre_objet_magique
            list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
        else:
            list_objets_magiques_intermediaires[nom_objet_magique] = {'nombre': nombre_objet_magique, 'valeur': valeur}
        objets_magiques_intermediaires_definis += 1
    # Tirage des objets magiques puissants
    list_objets_magiques_puissants = {}
    valeur_objets_magiques = 0
    objets_magiques_puissants_definis = 0
    while objets_magiques_puissants_definis < objet_magique_puissant:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
            determiner_objet_magique_puissant(valeur_objets_magiques, sheetlist)
        if list_objets_magiques_puissants.get(nom_objet_magique):
            list_objets_magiques_puissants[nom_objet_magique]['nombre'] += nombre_objet_magique
            list_objets_magiques_puissants[nom_objet_magique]['valeur'] += valeur
        else:
            list_objets_magiques_puissants[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                               'valeur': valeur}
        objets_magiques_puissants_definis += 1
    return piece_platine, piece_or, piece_argent, piece_cuivre, gemmes,objets_arts, objets_non_magiques, \
                objet_magique_faible, objet_magique_intermediaire, objet_magique_puissant, valeur_des_gemmes, \
                valeur_des_objets_arts, valeur_objets_non_magiques, valeur_objets_magiques, list_objets_non_magiques, \
                list_gemmes, list_objets_arts, list_objets_magiques_faibles, list_objets_magiques_intermediaires, \
                list_objets_magiques_puissants

