from pymongo import MongoClient

client = MongoClient("mongodb+srv://Shoco:brlamera42@cluster0-esyaf.mongodb.net")
db=client.tri_rpg
cursor = db["tri_list"].find().sort([("note", 1), ("name", 1)])


def list_aff_del():
    tlist = []
    for num, doc in enumerate(cursor):
        tlist.append(doc['_id'])
        print(num + 1, "-->", doc, "\n")
    return tlist

def delete(list_id):
    nb = input("Quel couple voulez-vous supprimer ? (Indiquez le nombre)")
    if not str(nb).isnumeric() or int(nb) > len(list_id) or int(nb) <= 0:
        print("Nombre erroné")
        return delete(list_id)
    else:
        db.tri_list.delete_one({"_id" : list_id[int(nb)-1]})
