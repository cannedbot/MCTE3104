"""
MCTE3104 - Interfacing Lab
Code that will transmit String through COM-Port.
Transmit '1' to turn on built-in LED
Transmit '0' to turn off built-in LED
"""

import serial
from time import sleep

try:
    ser = serial.Serial('COM6', 9600)
except Exception as e:
    print("[INFO] Error: " + str(e))

while True:
    input_cmd = input("Input 1 or 0: ")
    ser.write(str(input_cmd).encode())
