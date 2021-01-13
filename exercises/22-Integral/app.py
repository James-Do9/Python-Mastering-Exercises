def integral(num):
    input_dict = {}
    for i in range(1, num + 1):
        input_dict.update({i : i * i})
    return input_dict

print(integral(10))