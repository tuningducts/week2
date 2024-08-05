DAY_LENGTH = 24
days= 0 

def set_start_time():
    start_time = input("Please enter the current time as a number between 0 - 23: ")
    try:
        start_time = int(start_time)           
    except:
        print("invalid time please enter a digit from 0-23")
        start_time = set_start_time()
    if start_time <=23:
       return start_time
    else:
        start_time = set_start_time()
        return start_time

def set_alarm_length():
    alarm_length = input("Please enter how many hours from now a you want your alarm to go off: ")
    try:
        alarm_length = int(alarm_length)
    except:
        print("invalid input please enter a integer like 2 or 50")
        alarm_length = set_alarm_length()
    return alarm_length

if __name__ == '__main__':
    start_time = set_start_time()
    alarm_length = set_alarm_length()
    alarm_time = start_time

    for hour in range(0,alarm_length):
        alarm_time += 1
        #print(f'{alarm_time} at {hour}')
        if alarm_time == 24:
            alarm_time = 0 
            days +=1
    if days == 0 or days == 1:
        if days == 0:
            days = "Today"
        elif days == 1:
            days = "Tommorrow"
        print(f"Alarm will go of {days} at {alarm_time}")
    else:
        print(f"Alarm will go of in {days} days at {alarm_time}")
