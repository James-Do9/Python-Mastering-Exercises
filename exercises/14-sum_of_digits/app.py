#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
    first_digit = num // 100
    second_digit = num % 100 // 10
    third_digit = num % 10
    return first_digit + second_digit + third_digit


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))