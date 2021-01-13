phrase_list = input("Input sentence: ")
letter_counter = 0
number_counter = 0
for content in phrase_list:
    if content.isdigit():
        number_counter = number_counter + 1
    elif content.isalpha():
        letter_counter = letter_counter + 1
    else:
        continue
print("Letter:", letter_counter, "Number:", number_counter)
