# pip install psutil
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

print(f"Battery is at {percent}%")
print(f"Plugged in: {plugged}")