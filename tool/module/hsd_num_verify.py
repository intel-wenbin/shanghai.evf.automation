import pandas as pd
import numpy as np


def hsd_verify(file1, file2):
    df1 = pd.read_csv(file1, usecols=["Configuration", "Friendly Name"])
    df2 = pd.read_excel(file2, sheet_name="VV Bring Up Plan", usecols=["System ID", "HSD-ES"])
    print("********************************Platform HSD number verification********************************")
    empty_system_id = []
    for i in range(len(df1['Configuration'])):
        for j in range(len(df2['HSD-ES'])):
            if np.isnan(df2['HSD-ES'][j]):
                empty_system_id.append(str(df2['System ID'][j]))
            elif int(df1['Configuration'][i]) == int(df2['HSD-ES'][j]) and df1['Friendly Name'][i] == df2['System ID'][
                j]:
                passed_id = str(df1['Friendly Name'][i])
                print(passed_id + " has passed the check .")
    ids = list(set(empty_system_id))
    for i in range(len(ids)):
        print(ids[i] + " has no HSD-ES info .")
