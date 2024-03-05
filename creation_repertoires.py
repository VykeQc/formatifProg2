# importez les packages os et csv #
import os
os.chdir(os.path.dirname(__file__))

titre_des_colonnes = ['Matricule', 'Groupe', "Nom de l'étudiant", "Prénom de l'étudiant", 'Prog.']

groupe_cours_prog2 = [  ['2273383', '1010', 'Carrier', 'Alexandre', '420.BU'], 
                    ['2222119', '1080', 'Dion', 'Paul', '420.BB'], 
                    ['2229304', '1010', 'Douida', 'Wissale', '420.BA'], 
                    ['2218593', '1080', 'El Ammari', 'Amar', '420.BA'], 
                    ['2237984', '1080', 'Germain', 'Pierre', '420.BA'], 
                    ['2240637', '1010', 'Guilbault', 'Marc', '420.BA'], 
                    ['2243257', '1010', 'Jeannotte', 'Sylvain', '420.BU'], 
                    ['2212995', '1080', 'Joliveau', 'Edouard', '420.BB'], 
                    ['2211737', '1010', 'Kuru', 'Mika', '420.BU'], 
                    ['2268776', '1010', 'Lambert', 'Marc', '420.BA'], 
                    ['2144391', '1010', 'Moreno', 'Paolo', '420.BA'], 
                    ['2263531', '1010', 'Mahoud', 'Mohamed', '420.BB'], 
                    ['2265314', '1080', 'Péloquin', 'Guillaume', '420.BA'], 
                    ['2255712', '1010', 'Potvin', 'Pierre-Louis', '420.BA'], 
                    ['2149039', '1010', 'Plante', 'Lucie', '420.BA'], 
                    ['2173080', '1010', 'Sarrazin', 'Laurie', '420.BA'], 
                    ['2284942', '1080', 'Tin', 'Michel', '420.BA'], 
                    ['2263742', '1010', 'Tran', 'Jackson', '420.BB'], 
                    ['2244212', '1010', 'Vallieres', 'Mario', '420.BB'] ]

# On vous donne une liste d'étudiants dans le cours de prog 2.

# Il y a deux groupes d'étudiants différents dans la liste.
# On souhaite créer un répertoire pour le cours dont le nom est "prog2", 
#   puis créer un répertoire pour chaque groupe,
#   et dans ces répertoires, créer un répertoire par étudiant.

