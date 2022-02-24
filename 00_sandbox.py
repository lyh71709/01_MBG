from datetime import datetime

now = datetime.now()

current_time = now.strftime("%y")
print("Current Time =", current_time)