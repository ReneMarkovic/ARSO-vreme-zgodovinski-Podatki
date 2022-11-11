import numpy as np
import requests
import random
import time

# Za vsako merilno postajo v datoteko zapiše v formatu:
# leto,mesec,dan,etp,padavine,Tmin,Tmax,Tpov,Tmin5

# etp je evapotranspiracija, ki vključuje evaporacijo in transpiracijo iz zemljine površine v atmosfero
# padavine so v enotah mm
# Tmin je najnižja temperatura, Tmax najvišja in Tpov povprečna temperatura
# Tmin5 je najnižja temperatura na višini 5 cm in ni podana za vse merilne postaje

merilne_postaje = []
with open('mesta.txt', 'r') as f:
    mm = f.read().split('\n')

for m in mm:
    merilne_postaje.append(m.split('\t'))

www = 'https://meteo.arso.gov.si/uploads/probase/www/agromet/product/form/sl/data/'

for mesto, leto_start in merilne_postaje:

    print(mesto)
    
    mesec = 1
    
    leto = int(leto_start)
    
    f = open('zbrani_podatki/'+mesto+'.txt', 'w')
    
    while int(f'{leto}' + f'{mesec:02}') < 202211:
        
        # time.sleep(random.uniform(0.5,3))
    
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
            print(leto)
    
    f.close()
