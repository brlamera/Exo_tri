"""Executable du tri de rpg, utilisant les fonctions stockées en tri_rpg"""
from pymongo import MongoClient
from tri_rpg import *

# Connection à MongoDB
client = MongoClient("mongodb+srv://Shoco:brlamera42@cluster0-esyaf.mongodb.net")
# Définie la db à utiliser
db=client.tri_rpg

flag = "y"

while flag == "y":
    rpg = recup_rpg()
    note = recup_note()
    couple = creat_tuple(rpg, note)
    final = sort_rpg(couple)
    flag = continuer()

for cpt in range(len(list_name)):
    tri_rpg = {
        'name' : list_name[cpt],
        'note' : list_note[cpt]
    }
    result = db.tri_test.insert_one(tri_rpg)
    print('Created {0} of {1} as {2}'.format((cpt+1), len(list_name), result.inserted_id))

print(final)