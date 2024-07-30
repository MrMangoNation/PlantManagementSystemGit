import pandas as pd

#Can read csv from excel, need to use ; as a delimiter
df = pd.read_csv("plantSpreadSheet.csv", delimiter=";")

df.set_index("Plant", inplace=True)
result = df.loc["Spinach"]
print(df)
print(type(result))

