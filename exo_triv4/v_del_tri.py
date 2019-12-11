from pymongo import MongoClient
from m_del_tri import list_aff_del, delete

def del_list():

    tlist = list_aff_del()
    delete(tlist)