import time

def structured_time(input_mins, input_secs):
    if(input_mins > 0):
        return f"{input_mins:02}:{input_secs:02}"
    elif(input_secs > 0):
        return f"{input_secs:02}"
    else:
        print("invalid input")

def mins_countdown(time_mins, time_secs):
    if(time_secs==0):
        time_mins-=1
        time_secs+=59
    
    return time_mins, time_secs

def secs_countdown(time_secs):
    if(time_secs!=0):
        time_secs-=1
    
    return time_secs

def timer(input_mins, input_secs, total_secs):
    time_mins = input_mins
    time_secs = input_secs

    while(total_secs>0):
        time.sleep(1)
        total_secs-=1
        time_secs = secs_countdown(time_secs)
        time_mins, time_secs = mins_countdown(time_mins, time_secs)
        print(f"{time_mins:02}:{time_secs:02} ({total_secs})", end='\r')

def pomodoro_timer(work_mins, work_secs, work_total_secs, short_break_mins, short_break_secs, short_break_total_secs, long_break_mins, long_break_secs, long_break_total_secs, sets, reps):
    while(sets>0):
        while(reps>0):
            print("Time to work!")
            timer(work_mins, work_secs, work_total_secs)
            print(f"Break time! ({reps} reps more before long break)")
            timer(short_break_mins, short_break_secs, short_break_total_secs)
            reps-=1
        print(f"long break time! {sets} sets left!")
        timer(long_break_mins, long_break_secs, long_break_total_secs)
        sets-=1



def main():
    print("Enter work time")
    work_mins = int(input("Minutes: "))
    work_secs = int(input("Seconds: "))

    print("Enter break time")
    short_break_mins = int(input("Minutes: " ))
    short_break_secs = int(input("Seconds: "))

    print("Reps per set")
    reps = int(input("Enter number of repetitions per set: "))

    print("Enter long break time:")
    long_break_mins = int(input("Minutes: " ))
    long_break_secs = int(input("Seconds: "))

    print("Sets")
    sets = int(input("Enter total amount of sets: "))

    print("\n\n")

    work_total_secs = work_secs+work_mins*60
    short_break_total_secs = short_break_secs+short_break_mins*60
    long_break_total_secs = long_break_secs+long_break_mins*60

    pomodoro_timer(work_mins, work_secs, work_total_secs, short_break_mins, short_break_secs, short_break_total_secs, long_break_mins, long_break_secs, long_break_total_secs, sets, reps)
    

main()