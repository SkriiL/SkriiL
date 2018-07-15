from skriil.linear_model import LinearRegression
from skriil.file_reader import read_csv
import pandas as pd

#df = pd.read_csv("skriil/autos_prepared.csv")
#x = df[["kilometer"]].values
#y = df[["price"]].values

data = read_csv("skriil/autos_prepared.csv")
x = data["kilometer"]
y = data["price"]

model = LinearRegression()
model.train(x, y)
print(model.predict([[0]]))
