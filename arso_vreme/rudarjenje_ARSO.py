import numpy as np
import requests
import random
import time
import os
from tqdm.auto import tqdm


def check_sub_folder():
    if os.path.isdir("zbrani_podatki/RAW"):
        pass
    else:
        os.mkdir("zbrani_podatki/RAW")
    if os.path.isdir("zbrani_podatki/grafi"):
        pass
    else:
        os.mkdir("zbrani_podatki/grafi")
    if os.path.isdir("zbrani_podatki/CSV"):
        pass
    else:
        os.mkdir("zbrani_podatki/CSV")
    return None

def get_data(datum:int=202405):
    '''
    get_data(datum:int=202405)
    datum: int - datum v obliki leta in meseca, do katerega želimo pridobiti podatke.
    Funkcija pridobi podatke o vremenu iz spletne strani ARSO in jih shrani v mapo zbrani_podatki.
    '''
    os.system("cls")
    print("    - Pričenjam z rudarjenjem podatkov na ARSO spletni strani.")
    if os.path.isdir("zbrani_podatki"):
        check_sub_folder()
    else:
        os.mkdir("zbrani_podatki")
        check_sub_folder()
    # Za vsako merilno postajo v datoteko zapiše v formatu:
    # leto,mesec,dan,etp,padavine,Tmin,Tmax,Tpov,Tmin5

    # etp je evapotranspiracija, ki vključuje evaporacijo in transpiracijo iz zemljine površine v atmosfero
    # padavine so v enotah mm
    # Tmin je najnižja temperatura, Tmax najvišja in Tpov povprečna temperatura
    # Tmin5 je najnižja temperatura na višini 5 cm in ni podana za vse merilne postaje
    
    wd = os.getcwd()
    
    merilne_postaje = []
    path = os.path.join(wd, "mesta.txt")
    with open(path, 'r') as f:
        mm = f.read().split('\n')

    for m in mm:
        merilne_postaje.append(m.split('\t'))

    www = 'https://meteo.arso.gov.si/uploads/probase/www/agromet/product/form/sl/data/'

    for mesto, leto_start in tqdm(merilne_postaje,total = len(merilne_postaje), desc = "Delež pridobljenih podatkov iz merilnih mest"):
        mesec = 1
        filename = mesto+'.txt'
        leto = int(leto_start)
        path = os.path.join(wd,"zbrani_podatki","RAW", filename)
        GET = False
        if filename not in os.listdir("zbrani_podatki/RAW"):
            f = open(path, 'w')
            f.close()
            GET = True
        
        while (int(f'{leto}' + f'{mesec:02}') < datum) and GET:
            
            time.sleep(random.uniform(0.5,1))
            link = www + mesto + '_' + f'{leto}' + f'{mesec:02}' + '.txt'
            
            try:
                download = requests.get(link).content.decode("utf-8").replace('\r', '')
                download = download.split('\n')
                
                podatki = []
                
                for i in range(4, len(download)-1):
                    podatki.append(download[i].split('\t'))
                
                for p in podatki:
                    # Če ni podatka za etp ali padavine napiše vrednosti 0.0
                    if p[1] == '':
                        p[1] = 0.0
                    if p[2] == '':
                        p[2] = 0.0
                    
                    # Če so podatki za Tmin5 jih zapiše, če ne pa ne
                    if p[6] == '':
                        f.write(f'{leto},{mesec},{p[0]},{p[1]},{p[2]},{p[3]},{p[4]},{p[5]}\n')
                    else:
                        f.write(f'{leto},{mesec},{p[0]},{p[1]},{p[2]},{p[3]},{p[4]},{p[5]},{p[6]}\n')
                    
            except:
                pass
            
            mesec += 1
            if mesec == 13:
                mesec = 1
                leto += 1
                print(mesto, leto)
        
        f.close()
