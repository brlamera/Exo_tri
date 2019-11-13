list_rpg = []
list_name = ["Final Fantasy", "Shenmue", "BloodBorne", "Dark Souls", "Xenoblade Chronicles", "TESV Skyrim", "TLOZTP", "Fable"]
list_note = ["10", "4", "9", "8", "3", "0", "4", "5"]

def sort_list(name_rpg, note_rpg):
    """Renvoit une liste des différents RPG triés par leur note"""
    if not str(note_rpg).isnumeric() or int(note_rpg) < 0 or int(note_rpg) > 10:
        print("Note invalide.")
    tuple_rpg = (name_rpg, int(note_rpg))
    list_rpg.append(tuple_rpg)
    return sorted(list_rpg, key=lambda sort: sort[1])