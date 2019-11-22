list_rpg = []
list_name = []
list_note =[]

def recup_rpg():
    """Fonction chargé de récupérer le nom du RPG"""
    name_rpg = input("Tapez le nom de votre RPG : ")
    list_name.append(name_rpg)
    return name_rpg

def recup_note():
    """Fonction chargé de récupérer la note du RPG"""
    note_rpg = input("Tapez la note de votre RPG : ")
    if not str(note_rpg).isnumeric() or int(note_rpg) < 0 or int(note_rpg) > 10:
        print("Note invalide.")
        return recup_note()
    else:
        list_note.append(note_rpg)
        return note_rpg

def creat_tuple(name_rpg, note_rpg):
    """Créé un tuple à partir des informations récoltées ultérieurement"""
    tuple_rpg = (str(name_rpg), int(note_rpg))
    return tuple_rpg

def sort_rpg(tuple_rpg):
    """Renvoit une liste des différents RPG triés par leur note"""
    list_rpg.append(tuple_rpg)
    return sorted(list_rpg, key=lambda sort: sort[1])

def continuer():
    """Fonction chargé de mettre fin au programme, ou non"""
    keep = input("Voulez vous continuer ? (y/n)")
    keep = keep.lower()
    if keep == "y" or keep == "n":
        return keep
    else:
        print("Réponse invalide.")
        return continuer()
