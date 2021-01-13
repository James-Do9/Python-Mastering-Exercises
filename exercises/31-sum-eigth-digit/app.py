string = ""
for i in range(1000, 3001):
    if i >= 1000 and i <= 3000 and i % 2 == 0:
        string = string + str(i) + ","
    if i == 3000:
        string = string + str(i)
    print( "".join(string))