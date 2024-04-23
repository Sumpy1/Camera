import serial
import os
from datetime import datetime

# Configure serial communication
ser = serial.Serial('/dev/ttyACM0', 9600)  # Change the port accordingly

# Loop to read data from Arduino
while True:
    if ser.in_waiting > 0:
        signal = ser.readline().strip().decode('utf-8')
        print(f"Received signal: {signal}")  # Print the received signal
        if signal == '111':
            # Get the current date and time
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

            # Construct the file path for the desktop
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            file_name = f"picture_{timestamp}.jpg"
            file_path = os.path.join(desktop_path, file_name)

            # Take a picture using Raspberry Pi camera and save to the desktop
            os.system(f'libcamera-jpeg --width 640 --height 480 -o {file_path}')
            print(f"Picture taken and saved to {file_path}")

