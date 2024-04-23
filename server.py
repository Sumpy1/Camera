import os
import serial
from datetime import datetime
from flask import Flask, render_template, send_file

# Configure serial communication
ser = serial.Serial('/dev/ttyACM0', 9600)  # Change the port accordingly

# Create a Flask app
app = Flask(__name__)

# Define the route for the index page
@app.route('/')
def index():
    # Get the list of image files in the current directory
    image_files = [f for f in os.listdir('.') if f.endswith('.jpg')]
    return render_template('index.html', image_files=image_files)

# Define the route for serving image files
@app.route('/images/<filename>')
def serve_image(filename):
    return send_file(filename)

# Loop to read data from Arduino and take pictures
while True:
    if ser.in_waiting > 0:
        signal = ser.readline().strip().decode('utf-8')
        print(f"Received signal: {signal}")  # Print the received signal
        if signal == '111':
            # Get the current date and time
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

            # Construct the file path for the current directory
            file_name = f"picture_{timestamp}.jpg"
            file_path = os.path.join('.', file_name)

            # Take a picture using Raspberry Pi camera and save to the current directory
            os.system(f'libcamera-jpeg --width 640 --height 480 -o {file_path}')
            print(f"Picture taken and saved to {file_path}")

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
