import requests
import getpass
import os
import re
import datetime
import sys
from configparser import ConfigParser


def getAllDate(eslogin,espasswd,url):

    urlAllDate = url+"*?v"
    r = requests.get(urlAllDate, auth=(eslogin,espasswd),verify=False)

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

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def removeOldDate (olddate,eslogin,espasswd,url):
    try:

        for date_dl in olddate:
            urlOldDate = url+"-"+ date_dl.strftime('%Y.%m.%d')
            requests.delete(urlOldDate, auth=(eslogin,espasswd),verify=False)
            print("Succes")
    except:
        print("Error")

def main(defaultage):
    cfg = ConfigParser()
    cfg.read('config.ini')

    eslogin = cfg.get('server','login')
    espasswd = cfg.get('server','password')
    url = cfg.get('server','serverurl')
    port = cfg.get('server','port')
    index = cfg.get('delete','index')
    fullurl =url+":"+port+"/"+index

##    age = int(sys.argv[1])
    age = cfg.get('delete','age')
    if representsInt(age) == False:
        age = defaultage

    if age!=0 or age!=None:
        ind_date = getAllDate(eslogin,espasswd,fullurl)
        old_date = getOldDate(ind_date,age)
        if old_date != 0 or old_date != None:
            v = 0
            removeOldDate(old_date,eslogin,espasswd,fullurl)
        else:
            print("No date")
    elif age == 0:
        ind_date = getAllDate(eslogin,espasswd,fullurl)
        removeOldDate(ind_date,eslogin,espasswd,fullurl)
    else:
        print ('Parametr is empty or equals 0')
if __name__ == "__main__":
    main(14)
