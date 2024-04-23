#define trigPin 6
#define echoPin 5
#define pirPin 3
#define ledPin 13
#define thresholdDistance 15

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT); // Set LED pin as output
}

void loop() {
  long duration, distance;
  int pirState;
  static bool pirMotionDetected = false;
  bool distanceObstacleDetected = false;
  
  // Read PIR sensor
  pirState = digitalRead(pirPin);

  // Read distance sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  
  // Speed of sound in air at room temperature is approximately 343 m/s (or 0.0343 cm/us)
  // Calculate distance in centimeters: distance = (duration * speed of sound) / 2
  distance = (duration * 0.0343) / 2;

  Serial.print("Distance: ");
  Serial.println(distance);
  
  // Check if the distance is less than thresholdDistance
  if (distance < thresholdDistance) {
    Serial.println("Distance sensor detected obstacle"); 
    distanceObstacleDetected = true;
  } else {
    distanceObstacleDetected = false;
  }

  // Check PIR sensor state
  if (pirState == HIGH) {
    Serial.println("PIR sensor detected motion");
    pirMotionDetected = true;
  } else {
    pirMotionDetected = false;
  }
  
  if (pirMotionDetected || distanceObstacleDetected) {
    Serial.println("111");
    // Send signal 1 to Raspberry Pi
    digitalWrite(ledPin, HIGH); // Turn on LED
  } else {
    digitalWrite(ledPin, LOW); // Turn off LED
  }
  
  delay(100); // Adjust delay according to your needs
}
