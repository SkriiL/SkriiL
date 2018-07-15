from skriil.linear_model import LinearRegression
from skriil.logistic_regression import LogisticRegression
from skriil.file_reader import read_csv
import pandas as pd
import numpy as np

#x_train = np.array([
#    [0.0, 0.0],
#    [0.0, 1.0],
#    [1.0, 0.0],
#    [1.0, 1.0]
#])
#
#y_train = np.array([
#    0.0,
#    0.0,
#    0.0,
#    1.0
#])

data = read_csv("classification.csv")
x = data.get_values(["age", "interest"])
y = data.get_values(["success"])

model = LogisticRegression()
#model.train(x, y, rate=0.1)
#model.save("test")
model.load("test")

print(model.predict([[21, 70]], rounded=False))