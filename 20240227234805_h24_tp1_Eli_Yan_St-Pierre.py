import os
import csv
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

NOM_ÉTUDIANT = "nom, prénom" # Écrivez votre nom et prénom ici
GROUPE_ÉTUDIANT = ""         # Écrivez votre groupe ici.



# Objectif :
# Vous avez un fichier csv : "resultats_evaluation.csv". Il s'agit de résultats d'évaluations d'étudiants.
# On veut que vous en extrayiez l'information.
# Que vous faisiez des calculs pour faire une analyse statistique.
# Puis que vous transformiez les résultats obtenus en un dictionnaire.


###################################################################
##                          Partie 1                            ###
###################################################################

# Vous devez lire et extraire les informations du csv "resultats_evaluation.csv"
# Le format de ce csv ne permet pas d'extraire les données très facilement. Regardez-le avant de commencer.

# Ce csv contient 20 étudiants, chaque ligne correspondant à l'ID unique de l'étudiant, son nom, son programme, et le résultat de 8 évaluations. 5 Tps et 3 examens.

# Le but de cette partie est d'obtenir une liste qui contient chacune des valeurs du csv.
# MAIS, nous n'avons pas besoin du nom de l'étudiant ou du programme.

# variables

liste_etudiants = []

# lecture du .csv et filtrer les donnees

with open('resultats_evaluation.csv','r') as liste_file:
    liste_reader = csv.reader(liste_file, delimiter=';')
    next(liste_reader)
    next(liste_reader)
    for line in liste_reader:
        liste_reader = [line[0]]
        liste_reader.extend(line[3:])
        liste_etudiants.append(liste_reader)

# À la fin de cette partie. "liste_etudiants" doit contenir toutes la valeurs des étudiants. Sauf le nom et le programme de l'étudiant

###################################################################
##                          Partie 2                            ###
###################################################################

# On veut savoir le nombre d'étudiants ayant passé le cours ainsi que la moyenne de ceux ayant passé le cours.
# À partir de la "liste_etudiants" produite dans la partie 1, passé au travers et prenez note du nombre d'étudiants ayant passé et de leur note finale.
# Le cours est à double seuil, un étudiant doit avoir une moyenne de 60% ou plus dans la partie TPs AINSI qu'une moyenne de 60% ou plus dans la partie examen.
#       SI UN ÉTUDIANT À MOINS DE 60% dans une des deux parties, ca note final ne peut pas être supérieur à la note dans cette partie.

# À la fin de cette partie, on veut imprimer : 
#           - Le nombre d'étudiants ayant passé.
#           - La moyenne de ces étudiants
#           - La moyenne de tous les étudiants
#           - Le taux de succès au cours (pourcentage d'étudiants ayant passé)
        
# variables

etudiant_passe = 0
moy_passe = 0
total_passe = 0
moy_echec = 0
total_echec = 0

#calcule des moyennes et totaux

for etudiant in liste_etudiants:
    moy_tp = sum([int(resultat) for resultat in etudiant[1:6]])/5
    moy_ex = sum([int(resultat) for resultat in etudiant[6:]])/3

    if moy_tp >= 60 and moy_ex >= 60:
        etudiant_passe += 1
        moy_passe += (moy_tp + moy_ex)/2
    else:
        moy_echec = min(moy_tp, moy_ex)
        total_echec += moy_echec
moy_etudiant_passe = moy_passe / etudiant_passe
moy_total_etudiant = (total_echec + moy_passe)/len(liste_etudiants)
taux_succes = (etudiant_passe * 100)/len(liste_etudiants)
print("----------------------------------------------")

# print les resultats!

print(f"Etudiant ayant passe: {etudiant_passe}")
print(f"Moyenne des etudiants ayant passe: {round(moy_etudiant_passe)}%")
print(f"Moyenne total des etudiants: {round(moy_total_etudiant)}%")
print(f"Taux de succes: {round(taux_succes)}%")
print("----------------------------------------------")


###################################################################
##                          Partie 3                            ###
###################################################################

# On veut créer une liste de dictionnaires à partir de la liste obtenue dans la partie 1.
# Pour chaque étudiant on veut 3 paires clefs-valeurs dans le dictionnaire :
#               "ID" : Le id de l'étudiant
#               "note" : La note finale de l'étudiant.
#               "echec" : Une booléenne ayant la valeur True si l'étudiant échoue. Sinon la valeur False.
#
# Une fois cette liste de dictionnaire obtenue, imprimez-la dans le terminal. 

# variables

list_dict = []
ID = 0
note = 0
echec = None

# calcule de la note et si ils ont echoue ou pas

for etudiant in liste_etudiants:
    moy_tp = sum([int(resultat) for resultat in etudiant[1:6]])/5
    moy_ex = sum([int(resultat) for resultat in etudiant[6:]])/3

    
    if moy_tp >= 60 and moy_ex >= 60:
        note = round((moy_tp + moy_ex)/2)
        echec = False
    else:
        note = round(min(moy_tp, moy_ex))
        echec = True

    ID = etudiant[0]
# creation de la liste et des dictionnaires

    dict_etudiant = {"ID": ID, "note": f"{note}%", "echec": echec}
    list_dict.append(dict_etudiant)

# print le resultat!
print(list_dict)
print("----------------------------------------------")