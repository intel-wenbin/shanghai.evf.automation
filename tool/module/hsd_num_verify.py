import pandas as pd
import numpy as np


def hsd_verify(file1, file2):
    df1 = pd.read_csv(file1, usecols=["Configuration", "Friendly Name"])
    df2 = pd.read_excel(file2, sheet_name="VV Bring Up Plan", usecols=["System ID", "HSD-ES"])
    print("********************************Platform HSD number verification********************************")
    empty_friendly_name = []
    empty_system_id = []
    for i in range(len(df1['Friendly Name'])):
        if np.isnan(df1['Configuration'][i]):
            empty_friendly_name.append(df1['Friendly Name'][i])
        for j in range(len(df2['System ID'])):
            if np.isnan(df2['HSD-ES'][j]):
                empty_system_id.append(str(df2['System ID'][j]))
            elif df1['Friendly Name'][i] == df2['System ID'][j]:
                if int(df1['Configuration'][i]) == int(df2['HSD-ES'][j]):
                    passed_id = str(df1['Friendly Name'][i])
                    print(passed_id + " has passed the check .")
                else:
                    failed_id = str(df1['Friendly Name'][i])
                    print(failed_id + " failed the check .")
    ids_1 = list(set(empty_system_id))
    ids_2 = list(set(empty_friendly_name))
    for i in range(len(ids_1)):
        print(ids_1[i] + " has no HSD-ES info .")
    for i in range(len(ids_2)):
        print(ids_2[i] + " has no Configuration info .")
