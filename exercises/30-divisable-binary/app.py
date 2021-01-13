num = input("Input numbers: ")
num_splited = (num.split(","))
num_list = []
string = ""
for i in range(0, len(num_splited)):
    if int(num_splited[i]) % 5 == 0:
        string = string + num_splited[i] + ","

print(('').join(string))