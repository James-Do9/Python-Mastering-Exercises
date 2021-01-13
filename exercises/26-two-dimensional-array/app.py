def some_function(x, y):
    array = []
    for i in range(0, x):
        row = []
        for j in range (0, y):
            row.append(j*i)
        array.append(row)
    return array

print(some_function(3, 5))