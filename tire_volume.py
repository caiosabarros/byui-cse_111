import math

w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

result = ((math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000)  

print("The approximate volume is: {volume:.2f} liters".format(volume=result))

# Gets the current date from the computer’s operating system.
from datetime import datetime
current_datetime = datetime.now()
print(f"{current_datetime:%Y-%m-%d}")

# Opens a text file named volumes.txt for appending.
with open("volumes.txt", mode="at") as volumes_file:
    # Appends to the end of the volumes.txt file one line of text that contains the following five values:
    # current date
    print(f"current date: {current_datetime}", file=volumes_file)
    # width of the tire
    print(f"width of the tire: {w}", file=volumes_file)
    # aspect ratio of the tire
    print(f"aspect ratio of the tire: {a}", file=volumes_file)
    # diameter of the wheel
    print(f"diameter of the wheel: {d}", file=volumes_file)
    # volume of the tire
    print(f"volume of the tire: {round(result, 2)}", file=volumes_file)

# Additional feature: Logs volumes.txt onto the terminal:

import subprocess 
print(" ")
print("File volumes.txt:")
print(" ")
subprocess.run(["cat", "volumes.txt"])