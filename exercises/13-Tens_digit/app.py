#Complete the function to return the tens digit of a given interger
def tens_digit(num):
    if num > 9:
        new_num = num % 100
        left_num = new_num //10
        return left_num




#Invoke the function with any interger.
print(tens_digit(1234))