import pandas as pd
import os

path = r"Z:\TM1\TM1 Reports\Actual FYE 2023\Oct 23\for python"
reps = os.listdir(path)

collumns = ['Name']

adf = pd.DataFrame(columns=collumns)
ini = 0
for i in range (len(reps)):
    fname = reps[ini]
    name = os.path.join(path, fname)
    data = {'Name': [fname]}
    curfil = pd.DataFrame(data)
    adf = pd.concat([adf, curfil], ignore_index= True)
    print(ini)
    ini= ini + 1

adf.to_csv(r'Z:\TM1\TM1 Reports\Actual FYE 2023\Oct 23\Names2.csv')