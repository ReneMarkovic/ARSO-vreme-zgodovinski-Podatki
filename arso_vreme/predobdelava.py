import pandas as pd
import os
import glob
from tqdm.auto import tqdm


def ostrani_empty_newline(txt_file:str)->None:
    # Open and read the file
    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Check if the last line is just a newline and remove it if so
    if lines and lines[-1] == '\n':
        lines = lines[:-1]

    # Write the modified content back to the file
    with open(txt_file, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def pretvori_v_CSV():
    os.system("cls")
    print("    - Pričenjam s pretvarjanjem podatvko v CSV datoteko.")
    wd = os.getcwd()
    folder_path = os.path.join(wd, "zbrani_podatki","RAW")

    # seznam vseh txt datotek v mapi
    txt_files = glob.glob(folder_path + "/*.txt")

    # Prebere vse txt datoteke kot podatkovni okvir pandas
    for txt_file in tqdm(txt_files,total = len(txt_files),desc="Napredek pri pretvorbi v CSV datoteko"):
        print(f"\nDelam na datoteki {txt_file}")
        ostrani_empty_newline(txt_file)
        df = pd.read_csv(txt_file, delimiter=',', header=None, names=['leto', 'mesec', 'dan','etp','padavine','tmin','tmax','tpovp'],usecols=range(8))
        base_name = os.path.basename(txt_file)
        base_name = base_name.split('.')[0] # odstrani končnico datoteke – če sta ločeni z '.'
        df = df.assign(mesto=base_name)  #dodam novi stolpec = ime mesta
        csv_file = base_name + ".csv"
        path = os.path.join(wd,"zbrani_podatki","CSV",csv_file)
        df.to_csv(path, index=False)