from v_aff_tri import aff_list
from v_add_tri import add_list
from v_del_tri import del_list

def start_main():

    choix = input("Que voulez-vous faire ? (V)oir la liste actuelle - (A)jouter des éléments à la liste actuelle - (S)upprimer des éléments de la liste actuelle\n(Exemple, pour voir la liste, tapez \"V\")    ")
    choix = choix.lower()
    if str(choix) == 'v':
        aff_list()
    elif str(choix) == 'a':
        add_list()
    elif str(choix) == "s":
        del_list()
    else:
        err_list()

def err_list():
    print("\nCette option n'existe pas, ou est incorrecte\n")
    return start_main()