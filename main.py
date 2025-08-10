import random
import time

class Sensor:
    def __init__(self, name, threshold):
        self.name = name
        self.threshold = threshold

    def read_value(self):
        return random.randint(25, 45) if self.name == "Temperature" else random.uniform(0.5, 12.0)

    def is_critical(self, value):
        return value > self.threshold

temp_sensor = Sensor("Temperature", 35)
current_sensor = Sensor("Current", 10)

data_log = open("data_log.csv", "a")
event_log = open("events_log.csv", "a")

data_log.write("Sensor,Value,Time,Status\n")
event_log.write("Sensor,Value,Time,Status\n")

for i in range(5):
    print("\nReading " + str(i + 1))

    temp_value = temp_sensor.read_value()
    current_value = current_sensor.read_value()
    timestamp = time.strftime("%H:%M:%S")

    print(temp_sensor.name + ": " + str(temp_value) + "°C")
    if temp_sensor.is_critical(temp_value):
        print("CRITICAL")
        status = "CRITICAL"
        event_log.write(temp_sensor.name + "," + str(temp_value) + "," + timestamp + "," + status + "\n")
    else:
        print("OK")
        status = "OK"
    data_log.write(temp_sensor.name + "," + str(temp_value) + "," + timestamp + "," + status + "\n")

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

data_log.close()
event_log.close()
