from skriil.errors import InvalidDataError, PredictionError
from skriil.basic_methods import mean
from sklearn.preprocessing import StandardScaler
import numpy as np


class LinearRegression:
    def __init__(self):
        self.scaler = StandardScaler()
        self.x = []
        self.y = []
        self.a = 0
        self.b = 0

    @staticmethod
    def throw_exceptions(x, y):
        if len(x) == 0 or len(y) == 0:
            raise InvalidDataError("x or y parameter is missing!")
        if len(x) != len(y):
            raise InvalidDataError("length of x and y has to be the same!")

    @staticmethod
    def f(a, b, x):
        return a * x + b

    @staticmethod
    def j(a, b, x, y):
        return mean((y - (a * x + b)) ** 2)

    @staticmethod
    def j_ableitung_a(a, b, x, y):
        return mean(-2 * x * (-a * x - b + y))

    @staticmethod
    def j_ableitung_b(a, b, x, y):
        return mean(-2 * (-a * x - b + y))

    def scale_data(self, x):
        x = self.scaler.transform(x)
        return x

    def undo_scale(self, x):
        x = self.scaler.inverse_transform(x)
        return x

    def train(self, x, y):
        #self.throw_exceptions(x=x, y=y)
        self.scaler.fit(x)
        x = self.scale_data(x=x)
        a = 1
        b = 1
        rate = 0.005
        for i in range(0, 500):
            da = self.j_ableitung_a(a, b, x, y)
            db = self.j_ableitung_b(a, b, x, y)
            a -= rate * da
            b -= rate * db
        self.a = a
        self.b = b

    def predict(self, xl):
        xl = self.scale_data(x=xl)
        predicted = []
        for x in xl:
            predicted.append(self.a * x + self.b)
        return predicted

    def score(self, xs, ys):
        y_avg = mean(ys)
        sum_pred = 0
        sum_avg = 0
        for i in range(0, len(xs)):
            sum_pred += (ys[i] - self.predict([xs[i]])[0]) ** 2
            sum_avg += (ys[i] - y_avg) ** 2
        r2 = 1 - sum_pred / sum_avg
        return r2


