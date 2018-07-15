import numpy as np

def read_csv(csv, separator=","):
    raw_data = []
    data = {}
    with open(csv, "r") as file:
        for line in file:
            raw_data.append(line.strip().split(separator))

    raw_data = convert_to_int(raw_data)
    for name in raw_data[0]:
        data[name] = []

    for i in range(1, len(raw_data)):
        for j in range(0, len(raw_data[i])):
            data[raw_data[0][j]].append(raw_data[i][j])

    for key, value in data.items():
        data[key] = [[x] for x in value]
        data[key] = np.array(value)

    dataObj = Data(data)
    return dataObj


def convert_to_int(data):
    new_data = data
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            try:
                new_data[i][j] = float(new_data[i][j])
            except:
                new_data[i][j] = new_data[i][j]
    return new_data


class Data:
    def __init__(self, data):
        self.data = data

    def get_values(self, keys):
        if len(keys) == 1:
            data = []
            for value in self.data[keys[0]]:
                data.append(value)
            return np.array(data)
        else:
            data = []
            for i in range(0, len(self.data[keys[0]])):
                data.append([])
                for key in keys:
                    data[i].append(self.data[key][i])
            return np.array(data)