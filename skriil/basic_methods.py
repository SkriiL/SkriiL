def median(l):
    l = sorted(l)
    if len(l) % 2 == 0:
        med1 = l[int(len(l) / 2)]
        med2 = l[int(len(l) / 2) - 1]
        return (med1 + med2) / 2
    else:
        return l[int(len(l) / 2)]


def mean(l):
    return sum(l) / len(l)


def std(l):
    avg = sum(l) / len(l)
    values = [(x - avg) ** 2 for x in l]
    return (sum(values) / len(values)) ** 0.5


def variance(l):
    avg = sum(l) / len(l)
    values = [(x - avg) ** 2 for x in l]
    return sum(values) / len(values)


def str_to_float(l):
    new = []
    for value in l:
        try:
            new.append(float(value))
        except:
            new.append(value)
    return new