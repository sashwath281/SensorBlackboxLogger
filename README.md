# Sensor Blackbox Logger

A Python project that simulates and logs sensor data like a blackbox system for hardware devices.

---

## Features

- Simulates **Temperature** and **Current** sensor readings. 
- Logs all readings to **data_log.csv**.
- Logs all critical readings to **events_log.csv**.
- Plots time vs sensor values with Matplotlib.
- Saves the graphs as **temp_graph.png** and **current_graph.png**.

---

## Sample Output

Temperature Graph  
![Temperature Graph](temp_graph.png)

Current Graph  
![Current Graph](current_graph.png)

---

## How It Works

1. Runs a sensor simulator using Python classes.
2. Generates random temperature and current readings.
3. Flags readings above the pre-defined thresholds as "CRITICAL".
4. Saves logs and graphs for later analysis or monitoring.

## Run the Simulation
python main.py

## Plot Temperature Data
python plot_temperature.py

## Plot Current Data
python plot_current.py

---

## Future Extensions

- Replace random values with **Arduino sensor data via pySerial**.
- Trigger alerts using email, SMS, or IFTTT.
- Add a GUI (using Tkinter) or web interface (Flask)


