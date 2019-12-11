from pymongo import MongoClient
from c_add_tri import list_name, list_note

#Connection à MongoDB
client = MongoClient("mongodb+srv://Shoco:brlamera42@cluster0-esyaf.mongodb.net")
# Définie la db à utiliser
db=client.tri_rpg

def show_result():

    for cpt in range(len(list_name)):
        tri_rpg = {
            'name' : list_name[cpt],
            'note' : list_note[cpt]
        }
        result = db.tri_list.insert_one(tri_rpg)
        print('Created {0} of {1} as {2}'.format((cpt+1), len(list_name), result.inserted_id))
        