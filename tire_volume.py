import math

w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

result = ((math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000)  

print("The approximate volume is: {volume:.2f} liters".format(volume=result))
