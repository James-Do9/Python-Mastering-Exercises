def list_touple(tuple_input):
    string = ''
    for i in tuple_input:
        if tuple_input.index(i) == len(tuple_input) - 1:
            string = string + (f"\'{str(i)}\'")
        else:
            string = string + (f"\'{str(i)}\'") + ','
    return string

num_list = [34,67,55,33,12,98]
print(list_touple(tuple(num_list)))