from pymongo import MongoClient

client = MongoClient("mongodb+srv://Shoco:brlamera42@cluster0-esyaf.mongodb.net")
db=client.tri_rpg
cursor = db["tri_list"].find().sort([("note", 1), ("name", 1)])

def aff_list():

    tlist = []
    for doc in enumerate(cursor):
        print(doc, "\n")
