#! /bin/python
import csv
import os
os.chdir(os.path.dirname(__file__))

# Q3
# Ouvrez le ficher en lecture
# Utilisez le module csv pour lire le contenu du fichier
# Sautez la première ligne contenant les en-têtes
# Ajoutez chaque ligne à la variable list_client
# Finalement, imprimer la variable list_client

nom_fichier = "fichier_a_lire.csv"
list_client = []

with open(nom_fichier,"r") as f_lu:
    f_reader = csv.reader(f_lu)
    next(f_reader)
    for line in f_reader:
        f_reader = line
        list_client.append(f_reader)

print(list_client)

    




