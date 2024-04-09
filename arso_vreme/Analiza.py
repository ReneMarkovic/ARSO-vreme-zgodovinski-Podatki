import pandas as pd
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt
import calendar
import re
import os
import seaborn as sns
import scipy.stats as stats
from scipy.stats import pearsonr
import os


def analiziraj_podatke():
    os.system("cls")
    print("    - Pričenjam z analizo podatkov.")
    wd = os.getcwd()
    data_path = os.path.join(wd, "zbrani_podatki","CSV")

    folder=data_path
    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            
            ########################
            ########################
            ########################           GRAFI DNEVNIH TEMPRERATUR -> CELOTEN ČAS
            ########################
            ########################
            
            data = pd.read_csv(os.path.join(folder, filename), header=None, names=['year', 'month', 'day', 'etp', 'padavine', 'Tmin', 'Tmax', 'Tpov'])
            data["date"] = pd.to_datetime(data[['year', 'month', 'day']])
            
            plt.plot(data['date'], data["Tmin"],label="Tmin",linewidth=1)
            plt.plot(data['date'], data["Tmax"],label="Tmax",linewidth=1)
            plt.plot(data['date'], data["Tpov"],label="Tpov",linewidth=1)                  
            plt.title(f"Temperatura v {filename}",fontsize=10)
            plt.legend(fontsize=8)
            plt.xlabel('Datum',fontsize=8)
            plt.ylabel('T[°C]',fontsize=8)       
            plt.savefig(os.path.join(folder,"grafi", f"{filename.replace('.csv','')}_temperature.png"),dpi=200)
            plt.clf()
            plt.close()
            
            ########################
            ########################
            ########################           Tabele statističnih podatkov temperatur za celoten čas
            ########################
            ########################        
            
            
            temp_statistika = data[['Tmin', 'Tmax', 'Tpov']].describe()
            rowLabels = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
            ax = plt.subplot(1, 1, 1)
            table = plt.table(cellText=temp_statistika.values,
                    rowLabels=rowLabels,
                    colLabels=temp_statistika.columns,
                    cellLoc='center',
                    loc='center')
            table.auto_set_font_size(False)
            table.set_fontsize(8)
            ax.add_table(table)
            ax.axis("off")
            plt.savefig(os.path.join(folder,"grafi", f"{filename.replace('.csv','')}_temperature_tabela.png"),dpi=200)
            plt.clf()
            plt.close
            
            ########################
            ########################
            ########################           GRAFI MESEČNIH POVPREČIJ PO VSEH LETIH TEMPERATUR
            ########################
            ######################## 
            
            data["month"] = data["date"].dt.month # add a new column for the month
            monthly_temps = data.groupby("month")[["Tmin", "Tmax", "Tpov"]].mean() # group by month and calculate average Tmin, Tmax, Tpov
            data_by_month = data.groupby(data["date"].dt.month).mean()
            plt.plot(data_by_month.index, data_by_month["Tmin"],label="Tmin",linewidth=1)
            plt.plot(data_by_month.index, data_by_month["Tmax"],label="Tmax",linewidth=1)
            plt.plot(data_by_month.index, data_by_month["Tpov"],label="Tpov",linewidth=1)                  
            plt.title(f"Povprečna mesečna temperatura po vseh letih v {filename}",fontsize=10)
            plt.legend(fontsize=8)
            plt.xlabel('Month',fontsize=8)
            plt.ylabel('T[°C]',fontsize=8)
            plt.xticks(data_by_month.index, calendar.month_name[1:13], rotation=35, ha='right',fontsize=7)

            plt.savefig(os.path.join(folder,"grafi",  f"{filename.replace('.csv','')}_mesecne_povprecne_temperature.png"),dpi=200)
            plt.show()
            plt.close()
            
            ########################
            ########################
            ########################           KORELACIJA MED TPOV IN ETP
            ########################
            ######################## 

    Tpov_list = []
    etp_list = []

    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            data = pd.read_csv(os.path.join(folder, filename), header=None, names=['year', 'month', 'day', 'etp', 'padavine', 'Tmin', 'Tmax', 'Tpov'])
            Tpov_mean = data['Tpov'].mean()
            etp_mean = data['etp'].mean()
            Tpov_list.append(Tpov_mean)
            etp_list.append(etp_mean)
            correlation = pd.DataFrame({'Tpov':Tpov_list,'etp':etp_list}).corr()
    correlation, p_value=pearsonr(Tpov_list, etp_list)
    sns.regplot(x=Tpov_list,y= etp_list,data=data)

    plt.xlabel("Povprečna temperatura ")
    plt.ylabel('Povprečna etp')
    plt.title('Korelacija med povp. temo in etp za celo slovenijo')
    plt.annotate(f'correlation: {correlation:.2f}', xy=(0.2, 0.9), xycoords='axes fraction')

    filename = os.path.join(folder,"grafi","Korelacija_etp_Tpov.jpg")
    plt.savefig(filename,dpi=200,bbox_inches='tight')
    plt.show()
    plt.close() 

    ########################
    ########################
    ########################           KORELACIJA MED TPOV IN PADAVINAMI
    ########################
    ######################## 

    Tpov_list = []
    padavine_list = []

    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            data = pd.read_csv(os.path.join(folder, filename), header=None, names=['year', 'month', 'day', 'etp', 'padavine', 'Tmin', 'Tmax', 'Tpov'])
            Tpov_mean = data['Tpov'].mean()
            padavine_mean = data['padavine'].mean()
            Tpov_list.append(Tpov_mean)
            padavine_list.append(padavine_mean)
            correlation = pd.DataFrame({'Tpov':Tpov_list,'padavine':padavine_list}).corr()
    correlation, p_value=pearsonr(Tpov_list, padavine_list)
    sns.regplot(x=Tpov_list,y= padavine_list,data=data)

    plt.xlabel("Povprečna temperatura ")
    plt.ylabel('Povprečne paedavine')
    plt.title('Korelacija med povp. temo in padavinami za celo slovenijo')
    plt.annotate(f'correlation: {correlation:.2f}', xy=(0.2, 0.9), xycoords='axes fraction')

    filename = os.path.join(folder,"grafi","Korelacija_padavine_Tpov.jpg")
    plt.savefig(filename,dpi=200,bbox_inches='tight')
    plt.show()
    plt.close() 


    ########################
    ########################
    ########################           POVPREČNI PODATKI ZA CELO SLOVENIJO PO ČASU
    ########################
    ######################## 

    Tmin_list = []
    Tmax_list = []
    Tpov_list = []
    date_list = []

    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            data = pd.read_csv(os.path.join(folder, filename), header=None, names=['year', 'month', 'day', 'etp', 'padavine', 'Tmin', 'Tmax', 'Tpov'])
            data["date"] = pd.to_datetime(data[['year', 'month', 'day']])
            Tmin_mean = data['Tmin'].mean()
            Tmax_mean = data['Tmax'].mean()
            Tpov_mean = data['Tpov'].mean()
            date = data['date'].iloc[0]
            
            Tmin_list.append(Tmin_mean)
            Tmax_list.append(Tmax_mean)
            Tpov_list.append(Tpov_mean)
            date_list.append(date)

    df = pd.DataFrame({'date':date_list, 'Tmin':Tmin_list, 'Tmax':Tmax_list, 'Tpov':Tpov_list})
    df.set_index('date', inplace=True)
    df.plot()
    plt.xlabel('Datum')
    plt.ylabel('Temperatura [°C]')
    plt.title('Povprečen Tmin, Tmax, and Tpov po času')
    filename = os.path.join(folder,"grafi","Avg_temp_celaSLO.jpg")
    plt.savefig(filename,dpi=200,bbox_inches='tight')
    plt.show()
    plt.close()


    ########################
    ########################
    ########################           opisna statistika v vsakem mestu
    ########################
    ######################## 
    mean_Tpov = []
    std_Tpov = []
    max_Tmax = []
    min_Tmin = []
    labels_row=[]
    # iterate through files in folder
    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            data = pd.read_csv(os.path.join(folder, filename), header=None, names=['year', 'month', 'day', 'etp', 'padavine', 'Tmin', 'Tmax', 'Tpov'])
            labels_row.append(filename)
            mean_Tpov.append(data['Tpov'].mean())
            std_Tpov.append(data['Tpov'].std())
            max_Tmax.append(data['Tmax'].max())
            min_Tmin.append(data['Tmin'].min())

    # create dataframe with values
    data = {'mean_Tpov': mean_Tpov, 'std_Tpov': std_Tpov, 'max_Tmax': max_Tmax, 'min_Tmin': min_Tmin}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots(1, 1)
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center',rowLabels=labels_row)
    table.auto_set_font_size(False)
    table.set_fontsize(6)
    ax.axis("off")
    table.scale(1, 1.5)
    plt.title("Opisna statistika dnevnih povprečij",y=2.10, x=0.50,fontsize=18)

    filename=os.path.join(folder,"grafi","Tabela_all_time_podatki.jpg")
    plt.savefig(filename,dpi=200,bbox_inches='tight')
    plt.show()
    plt.close()
    print("Analiza je zaključena.")