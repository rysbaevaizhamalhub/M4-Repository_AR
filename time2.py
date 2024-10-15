# Aizhamal Rysbaeva
# Oct 15th, 2024

# The program takes the current time and a wait time as input
# adds them together, and prints the time when the alarm will go off
str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
