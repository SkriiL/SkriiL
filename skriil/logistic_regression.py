from skriil.errors import InvalidDataError, PredictionError
import pickle
import numpy as np


class LogisticRegression:
    def __init__(self):
        self.w = np.array([])
        self.b = 0

    @staticmethod
    def throw_exceptions(x, y):
        if len(x) == 0 or len(y) == 0:
            raise InvalidDataError("x or y parameter is missing!")
        if len(x) != len(y):
            raise InvalidDataError("length of x and y has to be the same!")

    @staticmethod
    def s(x):
        return 1 / (1 + np.exp(-x))

    def f(self, w, b, xs):
        rs = []
        for x in xs:
            sum = 0
            for i in range(0, len(w)):
                sum += w[i] * x[i]
            r = self.s(sum + b)
            rs.append(r)
        return np.array(rs)

    def j(self, w, b, x, y):
        return -np.mean(y * np.log(self.f(w, b, x)) + (1 - y) * np.log(1 - self.f(w, b, x)))

    def j_ableitung_w(self, w, b, x, y):
        rs = []
        for i in range(0, len(w)):
            rs.append(np.mean(x[:, i] * (self.f(w, b, x) - y)))
        return np.array(rs)

    def j_ableitung_b(self, w, b, x, y):
        return np.mean(self.f(w, b, x) - y)

    def train(self, x, y, rate=0.05, amount=5000):
        w = np.array([1.0, 1.0])
        b = 1
        for i in range(0, amount):
            dw = self.j_ableitung_w(w, b, x, y)
            db = self.j_ableitung_b(w, b, x, y)
            w -= rate * dw
            b -= rate * db

        self.w = w
        self.b = b

    def predict(self, xs, rounded=True):
        predicted = self.f(self.w, self.b, xs)
        if rounded:
            for i in range(0, len(predicted)):
                predicted[i] = round(predicted[i])
            return np.array(predicted)
        else:
            return np.array(predicted)

    def save(self, file):
        pickle.dump(self, open(file, "wb"))

    def load(self, file):
        loaded = pickle.load(open(file, "rb"))
        self.w = loaded.w
        self.b = loaded.b
