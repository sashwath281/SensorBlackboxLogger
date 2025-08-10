import matplotlib.pyplot as plt
import csv

times = []
currents = []

with open("data_log.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if row[0] == "Current":
            print("Found Current:", row)
            times.append(row[2])
            currents.append(float(row[1]))

if len(times) == 0:
    print("No 'Current' readings found in data_log.csv.")
else:
    plt.figure(figsize=(10, 5))
    plt.plot(times, currents, marker='o', linestyle='-', color='blue')
    plt.title("Current Readings Over Time")
    plt.xlabel("Time")
    plt.ylabel("Current (A)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("current_graph.png")
    plt.show()

