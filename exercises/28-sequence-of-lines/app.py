phrase = input("Input words: ")
phrase_list = phrase.split()
convert_list = ""
for i in phrase_list:
    convert_list = convert_list + i.upper() + " "
print(('').join(convert_list))