#This code will fetch all the data of the specified rows by passing parameters

import pandas as pd

def data_fetch(column_name,value):
    fns = pd.read_excel('C:\\Users\\158410\\OneDrive - Arrow Electronics, Inc\\Documents\\Sample1.xlsx')
    specified_row=fns.loc[fns[column_name] == value]
    specified_row.to_excel('C:\\Users\\158410\\OneDrive - Arrow Electronics, Inc\\Desktop\\Task1.xlsx', index=False)
data_fetch('Business Unit','Manufacturing')