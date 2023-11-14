import pandas as pd
import os

path = r"Z:\TM1\TM1 Reports\Actual FYE 2023\Python\Files"
reps = os.listdir(path)

collumns = ['Year', 'Month', 'Acct', 'Desc', 'Bal','Name']

adf = pd.DataFrame(columns=collumns)
ini = 0
for i in range (len(reps)):
    fname = reps[ini]
    name = os.path.join(path, fname)
    curfil = pd.read_csv(name, encoding='cp1252', converters={2:str})
    curfil = curfil.iloc[:, : 5]
    fi = 1
    for i in range (len(curfil.index)):
        try:
            y,m,a,d,b = curfil.iloc[fi]
            data = {'Year':[y],
                    'Month':[m],
                    'Acct':[a],
                    'Desc':[d],
                    'Bal':[b],
                    'Name':[fname]}
            data = pd.DataFrame(data)
            adf = pd.concat([adf,data], ignore_index= True)
            fi = fi + 1
        except:

            data = {'Year':["ERROR"],
                    'Month':["ERROR"],
                    'Acct':["ERROR"],
                    'Desc':["ERROR"],
                    'Bal':["ERROR"],
                    'Name':[fname]}
            data = pd.DataFrame(data)
            adf = pd.concat([adf,data], ignore_index= True)
            fi = fi + 1
    print(ini)
    ini= ini + 1

adf.to_csv(r'Z:\TM1\TM1 Reports\Actual FYE 2023\Python\FullConsolidated1.csv')