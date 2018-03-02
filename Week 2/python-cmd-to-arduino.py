"""
MCTE3104 - Interfacing Lab
Code that will transmit String through COM-Port.
Transmit '1' to turn on built-in LED
Transmit '0' to turn off built-in LED
"""

import serial
from time import sleep

try:
    ser = serial.Serial('COM5', 9600)
except Exception as e:
    print(e)

while True:
    ser.write(str(1).encode())
    sleep(1)

    ser.write(str(0).encode())
    sleep(1)
