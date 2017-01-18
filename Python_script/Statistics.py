import os
import re
import json
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from elasticsearch.client import CatClient

from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')

def getConnection():
    eslogin = cfg.get('server', 'login')
    espasswd = cfg.get('server', 'password')
    host = cfg.get('server','serverhost')
    port = cfg.get('server', 'port')
    ssl = bool(cfg.get('server','ssl'))
    #certs = bool(cfg.get('server','certs'))

    es = Elasticsearch(
        [host],
        http_auth=(eslogin, espasswd),
        port=int(port),
        use_ssl=ssl,
        verify_certs=False
    )
    return es
def getFullListIndicies(connection):
    ids_client = CatClient(connection)
    full_list_of_indicies = []
    short_list_of_indicies = []
    list_ind = str(cfg.get('statistic','indices')).split(' ')
    if (len(list_ind)>1):
        for ind in list_ind:
            ind_star = ind+'*'
            str_list = str(ids_client.indices(index=ind_star, v=True))
            full_list_of_indicies.extend(str_list.split("\n"))
            date_reg_exp = re.compile(ind+'-\d{4}[.]\d{2}[.]\d{2}')
            short_list_of_indicies.extend(date_reg_exp.findall(str_list))
    else:
        list_ind_star = list_ind+'*'
        str_list = str(ids_client.indices(index=list_ind_star, v=True))
        full_list_of_indicies.extend(str_list.split("\n"))
        date_reg_exp = re.compile(list_ind_star + '-\d{4}[.]\d{2}[.]\d{2}')
        short_list_of_indicies.extend(date_reg_exp.findall(str_list))
    return full_list_of_indicies,short_list_of_indicies
def getIndexMappingList(connection,index):
    mapList = []
    idx_client = IndicesClient(connection)
    mapping = idx_client.get_mapping(index=index, request_timeout=30)
    mapList = mapping[index]['mappings']
    return mapList

def writeToFileLists (ls,folder,filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(folder+'\\'+filename, 'w') as f:
        for s in ls:
            f.write(s + '\n')

def main():
    try:
        con = getConnection()
        list,shtlist = getFullListIndicies(con)
        print('################HEALTH########################')
        print(con.cluster.health())
        print('##################INDICIES####################')
        print list
        folder = cfg.get('statistic','path')
        #writeToFileLists(list,folder=folder,filename='Stats.txt')
        for index in list:
            print(index)
        print(shtlist)
        for index in shtlist:
            print('##############MAPPING#####################')
            print(index)
            type = getIndexMappingList(con,index)
            with open(folder+'/'+index+'.txt', "w") as f:
                json.dump(type, f, indent = 0, ensure_ascii=False)
            print(type)
            print('###########################################')
    except:
        pass
if __name__ == '__main__': main()

