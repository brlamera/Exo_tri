from c_add_tri import recup_rpg, recup_note, creat_tuple, sort_rpg, continuer
from m_add_tri import show_result

def add_list():

    flag = "y"

    while flag == "y":
        rpg = recup_rpg()
        note = recup_note()
        couple = creat_tuple(rpg, note)
        final = sort_rpg(couple)
        flag = continuer()
    show_result()
    print("Couple(s) ajouté(s) :", final)
