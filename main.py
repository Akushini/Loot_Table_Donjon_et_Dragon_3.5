from auth import auth
from menu import menu
from rencontre import rencontre
from utils import colored

sheetlist = auth()
piece_cuivre = piece_argent = piece_or = piece_platine = gemmes = objets_arts = objets_non_magiques = 0
objet_magique_faible = objet_magique_intermediaire = objet_magique_puissant = 0
valeur_des_gemmes = valeur_des_objets_arts = valeur_objets_non_magiques = valeur_objets_magiques = 0
list_objets_non_magiques = {}
list_gemmes = {}
list_objets_arts = {}
list_objets_magiques_faibles = {}
list_objets_magiques_intermediaires = {}
list_objets_magiques_puissants = {}
choix_menu = False
butin = False
tresor = False
fin = False
while not tresor:
    while not choix_menu:
        butin = False
        tirer_tresor = input(colored(255, 255, 255, "Voulez-vous tirer un tresor complet ? :"))
        if tirer_tresor == "oui":
            choix_menu = True
            while not butin:
                bonne_reponse = False
                while not bonne_reponse:
                    niveau_rencontre = input("Entrez le niveau de la rencontre (entre 1 et 30) :")
                    if niveau_rencontre.isdigit() and 1 <= int(niveau_rencontre) <= 30:
                        bonne_reponse = True
                    else:
                        print("Veuillez entrer un nombre entier entre 1 et 30")
                facteur_tresor = input("Entrez le facteur de tresor :")
                piece_platine, piece_or, piece_argent, piece_cuivre, gemmes, objets_arts, objets_non_magiques, \
                objet_magique_faible, objet_magique_intermediaire, objet_magique_puissant, valeur_des_gemmes, \
                valeur_des_objets_arts, valeur_objets_non_magiques, valeur_objets_magiques, list_objets_non_magiques, \
                list_gemmes, list_objets_arts, list_objets_magiques_faibles, list_objets_magiques_intermediaires, \
                list_objets_magiques_puissants = rencontre(niveau_rencontre, facteur_tresor, sheetlist) # recueil des données
                if piece_cuivre > 0:
                    print(f'Pièces de {colored(183, 118, 71, "cuivre")} : {colored(183, 118, 71, piece_cuivre)}')
                if piece_argent > 0:
                    print(f'Pièces d\'{colored(192, 192, 192, "argent")} : {colored(192, 192, 192, piece_argent)}')
                if piece_or > 0:
                    print(f'Pièces d\'{colored(255, 215, 0, "or")} : {colored(255, 215, 0, piece_or)}')
                if piece_platine > 0:
                    print(f'Pièces de {colored(229, 228, 226, "platine")} : {colored(229, 228, 226, piece_platine)}')
                if gemmes > 0:
                    for nom_gemme, info in list_gemmes.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_gemme.split("|")[0])} d\'une valeur de '
                              f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
                    print(f'Valeur totale des gemmes récupérées :{colored(255, 215, 0, valeur_des_gemmes)} pièces d\''
                          f'{colored(255, 215, 0, "or")}\n')
                if objets_arts > 0:
                    for nom_objet_art, info in list_objets_arts.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_art.split("|")[0])} d\'une valeur de '
                              f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
                    print(f'Valeur totale d\'objets d\'arts récupérés :{colored(255, 215, 0, valeur_des_objets_arts)} '
                          f'pièces d\'{colored(255, 215, 0, "or")}\n')
                if objets_non_magiques > 0:
                    for nom_objet_non_magique, info in list_objets_non_magiques.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_non_magique)} d\'une valeur de '
                              f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
                    print(f'Valeur totale des objets communs récupérés : {valeur_objets_non_magiques} '
                          f'pièces d\'{colored(255, 215, 0, "or")}')
                if objet_magique_faible > 0:
                    for nom_objet_magique, info in list_objets_magiques_faibles.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
                if objet_magique_intermediaire > 0:
                    for nom_objet_magique, info in list_objets_magiques_intermediaires.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
                if objet_magique_puissant > 0:
                    for nom_objet_magique, info in list_objets_magiques_puissants.items():
                        print(f'{info["nombre"]} {colored(70, 130, 180, nom_objet_magique)} d\'une valeur de '
      f'{colored(238, 201, 0, info["valeur"])} pièces d\'{colored(255, 215, 0, "or")}')
                if valeur_objets_magiques > 0:
                    print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
                reponse_finale = False
                while not reponse_finale:
                    recommencer = input("Voulez-vous tirer un autre butin ? :")
                    if recommencer == "oui":
                        butin = True
                        choix_menu = False
                        reponse_finale = True
                        tresor = False
                    elif recommencer == "non":
                        print("Au revoir")
                        exit()
                    else:
                        print("Répondez par oui ou non")
        elif tirer_tresor == "non":
            tresor, choix_menu = menu(tresor, choix_menu, sheetlist)
        else:
            print("Répondez par oui ou non")
