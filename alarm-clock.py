import time

def alarm_clock(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up!")
            break
        else:
            time.sleep(1)
            
alarm_time = input("What time do you want to set the alarm for? (HH:MM) ")
alarm_clock(alarm_time)
