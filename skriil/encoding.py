def one_hot_encoding(data):
    content = {}
    for d in data:
        if d not in content:
            content[d] = 0

    new_data = []
    for d in data:
        c = content.copy()
        c[d] = 1
        c_list = []
        for key, value in c.items():
            c_list.append(value)
        new_data.append(c_list)

    return new_data