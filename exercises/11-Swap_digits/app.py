#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
    left_num = str(num // 10)
    right_num = str(num % 10)
    return (right_num) + (left_num)



#Invoke the function with any two digit interger as its argument
print(swap_digits(13))

