import pandas as pd

df = pd.read_csv("plantSpreadSheet.csv", delimiter=";")

def returnLastRow(passedDf):
    return passedDf.tail(1).index[0]

def returnFirstRow(passedDf):
    return passedDf.head(1).index[0]



lastRow = returnLastRow(df)



#Can use .iloc to get a row of a specific index
#print(df.iloc[[lastRow]])

i = 0
while i <= lastRow:
    print(df.iloc[[i]])
    i += 1
