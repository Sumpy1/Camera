# Home Camera Monitoring System

## Libraries required
- pip install pyserial
- pip install flask
- pip install libcamera

## Summary
- Upload the camera.ino file to arduino
- Connect the arduino to raspberry pi to establish serial communicationb via USB or UART
- Establish ssh connection to raspberry pi to access pi Desktop interface (you can also use terminal to access pi)
- Save the camera.py as service in the raspberry pi so that the program will automatically load as soon as it powers up
- Check if the camera is saving files to desktop with time and date
- Use server.py as service to log the pictures in a local server ran on pi
- Connect power source, apply casing and attach to you front door as a home security camera
  
![schema](https://github.com/Sumpy1/Camera/assets/130939290/1b628200-ed04-4326-8213-74c8c428e053)

## System Description
The proposed system is a cost-effective alternative to expensive home security camera systems like Ring. It combines the capabilities of an Arduino and a Raspberry Pi to create a comprehensive home monitoring solution. The system utilizes a Passive Infrared (PIR) motion sensor and an ultrasonic distance sensor (HC-SR04) to detect movement and measure the distance of objects within the monitored area. The Arduino acts as the central control unit, receiving signals from the PIR and distance sensors. When motion is detected within a specified range, the Arduino communicates with the Raspberry Pi through serial communication. Upon receiving the signal, the Raspberry Pi can be configured to capture photo or video footage of the event. The captured media can be stored locally on the Raspberry Pi's memory or uploaded to a remote server or cloud storage for later access. Additionally, the system can be set up to send email notifications with the recorded footage to the user, providing real-time alerts about potential security breaches or unauthorized access. For added convenience and accessibility, the Raspberry Pi can host a local web server, allowing users to monitor the system and view recorded footage from any device connected to their home network. This innovative solution offers a cost-effective alternative to expensive commercial security systems while providing reliable home monitoring capabilities.

## Materials required
- Arduino uno
- Raspberry pi
- HCR ultrasonic sensor
- PIR motion sensor
- Connecting wires
- Power source / battery
- LED
- SD card
- Pi camera

  ![c67c50bf-bf07-49a7-b78f-783d7b2b95ce](https://github.com/Sumpy1/Camera/assets/130939290/9ec389ff-07ac-4c50-933c-cc85f52b444b)

## System Components, Integration & Construction
The system consists of the following main components:
1. Raspberry Pi 3: This is the central processing unit of the system. It acts as the brain, processing the data received from the sensors and performing the desired actions.
2. Arduino Board: An Arduino board, such as the Arduino Uno, is used as an interface between the sensors and the Raspberry Pi. It reads the sensor data and communicates it to the Raspberry Pi via serial communication.
 3. HC-SR04 Ultrasonic Distance Sensor: This sensor is used to measure the distance of objects from the system. It works by emitting ultrasonic sound waves and measuring the time it takes for the waves to bounce back after hitting an object.
4. PIR (Passive Infrared) Motion Sensor: This sensor is used to detect motion within a specific range. It works by sensing the infrared radiation emitted by moving objects, such as humans or animals.
5. Breadboard (optional): A breadboard can be used for prototyping and connecting the components during the initial development phase. However, for a more robust and permanent setup, the components can be directly connected without using a breadboard.
6. Power Supply: The Raspberry Pi can be powered by a battery pack, a power bank, or a regular power source, depending on the desired portability and runtime requirements.
Integration and Construction
1. Raspberry Pi and Arduino Integration: The Raspberry Pi and Arduino are connected via a serial communication interface, such as USB or UART. This allows the Arduino to send sensor data to the Raspberry Pi for processing.
2. Sensor Integration with Arduino: The HC-SR04 ultrasonic distance sensor and the PIR motion sensor are connected to the Arduino board. The Arduino is programmed to read data from these sensors and transmit it to the Raspberry Pi.
3. Raspberry Pi Software: The Raspberry Pi runs a script that receives the sensor data from the Arduino, processes it, and performs the desired actions. These actions can include capturing photos or videos, sending notifications, or logging data to a local or remote server.
4. Power Supply Integration: The Raspberry Pi is connected to a power source. If a battery pack or power bank is used, it should be capable of providing sufficient power for the desired runtime.

## System Functioning
1. Motion Detection: When the PIR motion sensor detects movement within its range, it sends a signal to the Arduino.Using it with a distance sensors maximizes efficiency and also allow larger area to monitor.
2. Distance Measurement: Upon receiving the motion signal, the Arduino triggers the HC-SR04 ultrasonic distance sensor to measure the distance of the detected object.
3. Data Transmission: The Arduino transmits the motion detection signal and the measured distance data to the Raspberry Pi via serial communication.
4. Data Processing: The Raspberry Pi receives the sensor data from the Arduino and processes it according to the programmed logic. This can include capturing photos or videos, sending notifications, or logging data.
5. Action Execution: Based on the processed data, the Raspberry Pi can perform various actions, such as storing the captured media locally, uploading it to a remote server, or sending email notifications with the recorded footage. It also saves the date and time when the footage was recorded.
6. Local Server (optional): The Raspberry Pi can host a local web server, allowing users to monitor the system and view recorded footage from any device connected to their home network.


## References
- Serial communication - https://www.youtube.com/watch?v=jU_b8WBTUew&t=2s
- Flask server - https://www.youtube.com/watch?v=6M3LzGmIAso
- SSH for pi - https://www.youtube.com/watch?v=63yw7b0NuWc&t=19s
- Flash SD card with pi OS - https://www.youtube.com/watch?v=eS-N8NCB9rk

## Open source contributions appreciated
