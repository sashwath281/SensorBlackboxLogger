import matplotlib.pyplot as plt
import csv

times = []
temps = []

with open("data_log.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        times.append(row[2])
        temps.append(int(row[1]))

plt.figure(figsize=(10, 5))
plt.plot(times, temps, marker='o', color='red')
plt.title("Temperature Readings Over Time")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("temp_graph.png")
plt.show()

