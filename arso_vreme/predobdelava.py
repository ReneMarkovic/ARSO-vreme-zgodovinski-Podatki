import pandas as pd
import os
import glob
from tqdm.auto import tqdm


def pretvori_v_CSV():
    os.system("cls")
    print("    - Pričenjam s pretvarjanjem podatvko v CSV datoteko.")
    wd = os.getcwd()
    folder_path = os.path.join(wd, "zbrani_podatki","RAW")

    # seznam vseh txt datotek v mapi
    txt_files = glob.glob(folder_path + "/*.txt")

    # Prebere vse txt datoteke kot podatkovni okvir pandas
    for txt_file in tqdm(txt_files,total = len(txt_files),desc="Napredek pri pretvorbi v CSV datoteko"):
        df = pd.read_csv(txt_file, delimiter=',', header=None, error_bad_lines=False, names=['leto', 'mesec', 'dan','etp','padavine','tmin','tmax','tpovp'],usecols=range(8))
        base_name = os.path.basename(txt_file)
        base_name = base_name.split('.')[0] # odstrani končnico datoteke – če sta ločeni z '.'
        df = df.assign(mesto=base_name)  #dodam novi stolpec = ime mesta
        csv_file = base_name + ".csv"
        path = os.path.join(wd,"zbrani_podatki","CSV",csv_file)
        df.to_csv(path, index=False)