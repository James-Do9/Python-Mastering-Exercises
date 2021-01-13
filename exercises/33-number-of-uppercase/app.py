phrase_list = input("Input sentence: ")
lower_counter = 0
upper_counter = 0
for content in phrase_list:
    if content.isupper():
        upper_counter = upper_counter + 1
    elif content.islower():
        lower_counter = lower_counter + 1
    else:
        continue
print("Lowercase:", lower_counter, "Uppercase:", upper_counter)
