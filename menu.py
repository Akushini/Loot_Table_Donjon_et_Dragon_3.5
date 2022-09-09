from anneau import determiner_anneau_puissant, determiner_anneau_intermediaire, determiner_anneau_faible
from arme import determiner_arme_faible, determiner_arme_intermediaire, determiner_arme_puissant
from armure import determiner_armure_bouclier_faible, determiner_armure_bouclier_intermediaire, \
    determiner_armure_bouclier_puissant
from baguette import determiner_baguette_faible, determiner_baguette_intermediaire, determiner_baguette_puissant
from baton import determiner_baton_puissant, determiner_baton_intermediaire
from objet_merveilleux import determiner_objet_merveilleux_intermediaire, \
    determiner_objet_merveilleux_faible, determiner_objet_merveilleux_puissant
from potions_huiles import determiner_potion_huile_faible, determiner_potion_huile_intermediaire, \
    determiner_potion_huile_puissant
from sceptre import determiner_sceptre_intermediaire, determiner_sceptre_puissant
from utils import lancer_gemme, lancer_objet_art, poser_question_puissance, determiner_parchemin_faible, \
    determiner_parchemin_puissant, determiner_parchemin_intermediaire, colored


def menu(tresor, choix_menu, sheetlist):
    valeur_objets_magiques = 0
    objets_magiques_faibles_definis = 0
    objets_magiques_intermediaires_definis = 0
    objets_magiques_puissants_definis = 0
    list_objets_magiques_faibles = {}
    list_objets_magiques_intermediaires = {}
    list_objets_magiques_puissants = {}
    reponse_menu = input("Que voulez-vous faire ?            \n"
                         "1   - Tirer des gemmes            \n"
                         "2   - Tirer des objets d\'arts     \n"
                         "3   - Tirer des baguettes          \n"
                         "4   - Tirer des armes magiques     \n"
                         "5   - Tirer des armures magiques   \n"
                         "6   - Tirer des anneaux            \n"
                         "7   - Tirer des parchemins  \n"
                         "8   - Tirer des batons        \n"
                         "9   - Tirer des scpetres       \n"
                         "10  - Tirer des objets merveilleux \n"
                         "11  - Tirer des potions et huiles \n")
    if reponse_menu.isdigit() and 1 <= int(reponse_menu) <= 11:
        if reponse_menu.isdigit() and int(reponse_menu) == 1:
            bonne_reponse = False
            while not bonne_reponse:
                gemmes = int(input("combien de gemmes ?"))
                if gemmes > 0:
                    list_gemmes = []
                    valeur_des_gemmes = 0
                    gemmes_estimees = 0
                    bonne_reponse = True
                else:
                    print("Veuillez entrer un nombre entier supérieur à 0")
                while gemmes_estimees < gemmes:
                    valeur_des_gemmes, valeur, nom_gemme = lancer_gemme(valeur_des_gemmes)
                    list_gemmes.append((nom_gemme, valeur))
                    gemmes_estimees += 1
                print(f'Gemmes trouvées : {gemmes}')
                for aTuple in list_gemmes:
                    print(f'1 {colored(70, 130, 180, aTuple[0])}d\'une valeur de '
                          f'{colored(238, 201, 0, aTuple[1])} pièces d\'{colored(255, 215, 0, "or")}')
                    print()
                    print(f'Valeur totale des gemmes récupérées : {valeur_des_gemmes} pièces d\''
                          f'{colored(255, 215, 0, "or")}')
        if reponse_menu.isdigit() and int(reponse_menu) == 2:
            bonne_reponse = False
            while not bonne_reponse:
                objets_arts = int(input("combien d\'objet d\'arts ?"))
                if objets_arts > 0:
                    list_objets_arts = []
                    valeur_des_objets_arts = 0
                    objets_arts_estimees = 0
                    bonne_reponse = True
                else:
                    print("Veuillez entrer un nombre entier supérieur à 0")
                while objets_arts_estimees < objets_arts:
                    valeur_des_objets_arts, valeur, nom_objet_art = lancer_objet_art(valeur_des_objets_arts)
                    list_objets_arts.append((nom_objet_art, valeur))
                    objets_arts_estimees += 1
                    print(f'Objets d\'arts trouvés : {objets_arts}')
                    for aTuple in list_objets_arts:
                        print(f'1 {colored(70, 130, 180, aTuple[0])}d\'une valeur de '
                              f'{colored(238, 201, 0, aTuple[1])} pièces d\'{colored(255, 215, 0, "or")}')
                    print()
                    print(f'Valeurs totale des objets d\'arts récupérés : {valeur_des_objets_arts} pièces d\''
                          f'{colored(255, 215, 0, "or")}')
        if reponse_menu.isdigit() and int(reponse_menu) == 3:
            bonne_reponse = False
            while not bonne_reponse:
                puissance, combien = poser_question_puissance()
                if puissance == 1:
                    objet_magique_faible = combien
                    while objets_magiques_faibles_definis < objet_magique_faible:
                        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                            determiner_baguette_faible(valeur_objets_magiques)
                        if nom_objet_magique in list_objets_magiques_faibles:
                            list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                            list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                        else:
                            list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                               'valeur': valeur}
                        objets_magiques_faibles_definis += 1
                        bonne_reponse = True
                if puissance == 2:
                    objet_magique_intermediare = combien
                    while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                            determiner_baguette_intermediaire(valeur_objets_magiques)
                        if nom_objet_magique in list_objets_magiques_faibles:
                            list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                            list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                        else:
                            list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                               'valeur': valeur}
                        objets_magiques_intermediaires_definis += 1
                        bonne_reponse = True
                if puissance == 3:
                    objet_magique_puissant = combien
                    while objets_magiques_puissants_definis < objet_magique_puissant:
                        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                            determiner_baguette_puissant(valeur_objets_magiques)
                        if nom_objet_magique in list_objets_magiques_faibles:
                            list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                            list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                        else:
                            list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                               'valeur': valeur}
                        objets_magiques_puissants_definis += 1
                        bonne_reponse = True
                for nom_objet_magique, info in list_objets_magiques_faibles.items():
                    print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
                print()
                for nom_objet_magique, info in list_objets_magiques_intermediaires.items():
                    print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
                print()
                for nom_objet_magique, info in list_objets_magiques_puissants.items():
                    print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
                print()
                print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 4:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                objet_magique_faible = combien
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_arme_faible(
                        valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_faibles_definis += 1
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_arme_intermediaire(
                        valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_arme_puissant(
                        valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_puissants_definis += 1
            for nom_objet_magique, info in list_objets_magiques_faibles.items():
                print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_intermediaires.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_puissants.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 5:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                objet_magique_faible = combien
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure_bouclier_faible(
                        valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_faibles_definis += 1
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_armure_bouclier_intermediaire(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_armure_bouclier_puissant(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_puissants_definis += 1
            for nom_objet_magique, info in list_objets_magiques_faibles.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_intermediaires.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_puissants.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 6:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                objet_magique_faible = combien
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_anneau_faible(
                        valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_faibles_definis += 1
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_anneau_intermediaire(
                        valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_anneau_puissant(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_puissants_definis += 1
            for nom_objet_magique, info in list_objets_magiques_faibles.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_intermediaires.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_puissants.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 7:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                objet_magique_faible = combien
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_parchemin_faible(
                        valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_faibles_definis += 1
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_parchemin_intermediaire(
                        valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_parchemin_puissant(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_puissants_definis += 1
            for nom_objet_magique, info in list_objets_magiques_faibles.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_intermediaires.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_puissants.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 8:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                print("les batons de faible puissance n'existent pas")
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_baton_intermediaire(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_baton_puissant(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_puissants_definis += 1
            for nom_objet_magique, info in list_objets_magiques_faibles.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_intermediaires.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_puissants.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            if valeur_objets_magiques > 0:
                print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 9:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                print("les sceptres de faible puissance n'existent pas")
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_sceptre_intermediaire(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_sceptre_puissant(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_puissants_definis += 1
            for nom_objet_magique, info in list_objets_magiques_faibles.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_intermediaires.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_puissants.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            if valeur_objets_magiques > 0:
                print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 10:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                objet_magique_faible = combien
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_objet_merveilleux_faible(valeur_objets_magiques, sheetlist)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_faibles_definis += 1
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_objet_merveilleux_intermediaire(valeur_objets_magiques, sheetlist)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_objet_merveilleux_puissant(valeur_objets_magiques, sheetlist)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_puissants_definis += 1
            for nom_objet_magique, info in list_objets_magiques_faibles.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_intermediaires.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_puissants.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            if valeur_objets_magiques > 0:
                print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 11:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                objet_magique_faible = combien
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_potion_huile_faible(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_faibles_definis += 1
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_potion_huile_intermediaire(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = \
                        determiner_potion_huile_puissant(valeur_objets_magiques)
                    if nom_objet_magique in list_objets_magiques_faibles:
                        list_objets_magiques_faibles[nom_objet_magique]['nombre'] += nombre_objet_magique
                        list_objets_magiques_faibles[nom_objet_magique]['valeur'] += valeur
                    else:
                        list_objets_magiques_faibles[nom_objet_magique] = {'nombre': nombre_objet_magique,
                                                                           'valeur': valeur}
                    objets_magiques_puissants_definis += 1
            for nom_objet_magique, info in list_objets_magiques_faibles.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_intermediaires.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            for nom_objet_magique, info in list_objets_magiques_puissants.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
            print()
            print(
                f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
    else:
        print("Veuillez entrer un nombre entier entre 1 et 11")
    reponse_finale = False
    while not reponse_finale:
        recommencer = input("Voulez-vous tirer un autre butin ? :")
        if recommencer == "oui":
            reponse_finale = True
            return tresor, choix_menu
        if recommencer == "non":
            tresor = True
            choix_menu = True
            reponse_finale = True
            print("Au revoir")
            return tresor, choix_menu
        else:
            print("Répondez par oui ou non")
