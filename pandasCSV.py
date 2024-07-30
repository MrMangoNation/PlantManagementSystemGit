import pandas as pd

#Can read csv from excel, need to use ; as a delimiter
df = pd.read_csv("plantSpreadSheet.csv", delimiter=";")

for index, row in df.iterrows():
    print(row.to_list())

PlantList = df["Plant"].to_list()

