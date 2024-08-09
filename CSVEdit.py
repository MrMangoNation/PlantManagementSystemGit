import pandas as pd

df = pd.read_csv("plantSpreadSheet.csv", delimiter=";")

def returnLastRow(passedDf):
    return passedDf.tail(1).index[0]

def returnFirstRow(passedDf):
    return passedDf.head(1).index[0]



lastRow = returnLastRow(df)




print(lastRow)


