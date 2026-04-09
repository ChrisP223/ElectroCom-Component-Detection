#include <Servo.h>

Servo panServo;
Servo tiltServo;

int panAngle  = 90;
int tiltAngle = 90;

void setup() {
  Serial.begin(9600);
  panServo.attach(9);
  tiltServo.attach(10);
  panServo.write(panAngle);
  tiltServo.write(tiltAngle);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int commaIndex = data.indexOf(',');
    if (commaIndex > 0) {
      int newPan  = data.substring(0, commaIndex).toInt();
      int newTilt = data.substring(commaIndex + 1).toInt();

      newPan  = constrain(newPan,  30, 150);
      newTilt = constrain(newTilt, 30, 150);

      panAngle  += constrain(newPan  - panAngle,  -3, 3);
      tiltAngle += constrain(newTilt - tiltAngle, -3, 3);

      panServo.write(panAngle);
      tiltServo.write(tiltAngle);
    }
  }
}