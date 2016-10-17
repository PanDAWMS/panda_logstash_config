import requests
import getpass
import os
import re
import datetime
import sys

def getAllDate(eslogin,espasswd):
    r = requests.get('https://es-atlas.cern.ch:9203/_cat/indices/atlas_pandalogs*?v', auth=(eslogin,espasswd),verify=False)

    status_code = r.status_code
    if status_code == 200:
        response_text = r.text
        date_reg_exp = re.compile('\d{4}[.]\d{2}[.]\d{2}')

        matches_list=date_reg_exp.findall(response_text)
        ind_date =[]

        for match in matches_list:
            ind_date.append(datetime.datetime.strptime(match, '%Y.%m.%d').date())
    return ind_date

def getOldDate (inddate,age):
    now = datetime.date.today()
    olddate=[]
    for date in inddate:
        day_count = (now - date).days
        if day_count > age:
            olddate.append(date)
    return olddate

def removeOldDate (olddate,eslogin,espasswd):
    try:
        for date_dl in olddate:
            url = "https://es-atlas.cern.ch:9203/atlas_pandalogs-"+ date_dl.strftime('%Y.%m.%d')
            rdelete = requests.delete(url, auth=(eslogin,espasswd),verify=False)
            print("Succes")
    except:
        print("Error")

def main():
    eslogin = 'es-atlas'
    espasswd = '*********'
    age = int(sys.argv[1])
    if age!=0 or age!= None:

        ind_date = getAllDate(eslogin,espasswd)
        old_date = getOldDate(ind_date,age)
        if old_date != 0 or old_date != None:
            removeOldDate(old_date,eslogin,espasswd)
        else:
            print("No date")
    elif age == 0:
        ind_date = getAllDate(eslogin,espasswd)
        removeOldDate(ind_date,eslogin,espasswd)
    else:
        print ('Parament is empty or equals 0')
if __name__ == "__main__":
    main()
