#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    first_hour_in_seconds = hr1 * 3600
    first_minute_in_seconds = min1 * 60
    first_all_seconds = first_hour_in_seconds + first_minute_in_seconds + sec1
    second_hour_in_seconds = hr2 * 3600
    second_minute_in_seconds = min2 * 60
    second_all_seconds = second_hour_in_seconds + second_minute_in_seconds + sec2
    return second_all_seconds - first_all_seconds


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))