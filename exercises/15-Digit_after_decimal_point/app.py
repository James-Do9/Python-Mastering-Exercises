#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
    new_num = int((num * 10) % 10 )
    return new_num



#Invoke the function with a positive real number. ex. 34.33
print(first_digit(111.342))