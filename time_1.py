# Aizhamal Rysbaeva
# Oct 15th, 2024

# The program asks the user for the current time and a wait time
# adds them together
# prints the final time after waitint

current_time_str = input("What is the current time (in hours 0-23)? ")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
print(final_time_int)
