"""Main de test"""

from tri_rpg_goal_only import *

cpt = 0
while cpt < len(list_name):
    list = sort_list(list_name[cpt], list_note[cpt])
    cpt += 1
print(list)
    