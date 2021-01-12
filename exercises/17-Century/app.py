#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.
import math
def century(year):
    right_num = year % 1000
    left_num = year // 100
    if right_num >= 1:
        return left_num + 1
    else:
        return left_num



#Invoke the function with any given year. 
print(century(1801))