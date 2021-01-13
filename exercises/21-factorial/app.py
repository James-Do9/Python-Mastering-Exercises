# Your code here
def factorial(num):
    new_num = 1
    for i in range(1, num + 1):
        new_num = new_num * i
    return new_num

print(factorial(8))