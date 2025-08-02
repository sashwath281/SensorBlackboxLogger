import random
import time

# Step 1: Sensor class
class Sensor:
    def __init__(self, name, threshold):
        self.name = name
        self.threshold = threshold

    def read_value(self):
        return random.randint(25, 45)

    def is_critical(self, value):
        return value > self.threshold

# Step 2: Create sensors
temp_sensor = Sensor("Temperature", 35)
current_sensor = Sensor("Current", 10)

# Step 3: Open both log files in append mode
data_log = open("data_log.csv", "a")
event_log = open("events_log.csv", "a")

# Optional: Write headers if the files are empty
data_log.write("Sensor,Value,Time,Status\n")
event_log.write("Sensor,Value,Time,Status\n")

# Read and log 5 times
for i in range(5):
    print("\nReading " + str(i + 1))

    # Read values
    temp_value = temp_sensor.read_value()
    current_value = current_sensor.read_value()

    # Get current time
    timestamp = time.strftime("%H:%M:%S")

    # ----- Temperature -----
    print(temp_sensor.name + ": " + str(temp_value) + "°C")
    if temp_sensor.is_critical(temp_value):
        print("CRITICAL")
        status = "CRITICAL"
        event_log.write(temp_sensor.name + "," + str(temp_value) + "," + timestamp + "," + status + "\n")
    else:
        print("OK")
        status = "OK"
    data_log.write(temp_sensor.name + "," + str(temp_value) + "," + timestamp + "," + status + "\n")

    # ----- Current -----
    print(current_sensor.name + ": " + str(current_value) + "A")
    if current_sensor.is_critical(current_value):
        print("CRITICAL")
        status = "CRITICAL"
        event_log.write(current_sensor.name + "," + str(current_value) + "," + timestamp + "," + status + "\n")
    else:
        print("OK")
        status = "OK"
    data_log.write(current_sensor.name + "," + str(current_value) + "," + timestamp + "," + status + "\n")

    time.sleep(1)

# Close both files
data_log.close()
event_log.close()
