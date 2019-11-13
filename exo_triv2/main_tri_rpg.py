"""Executable du tri de rpg, utilisant les fonctions stockées en tri_rpg"""

from tri_rpg import *

flag = "y"

while flag == "y":

    rpg = recup_rpg()
    note = recup_note()
    couple = creat_tuple(rpg, note)
    final = sort_rpg(couple)
    flag = continuer()

print(final)
