#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
    minute = int(secs / 60)
    hour = int(minute / 60)
    return (hour, minute)




#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))