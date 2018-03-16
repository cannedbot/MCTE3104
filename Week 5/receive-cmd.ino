/*
MCTE3104 - Interfacing Lab
Code that will receive String from COM-Port.
If String equals to '1' turn on built-in LED
If String equals to '0' turn off built-in LED
*/

void setup() {
  Serial.println(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String payload = Serial.readStringUntil('\r\n');
    int cmd = payload.toInt();

    if (cmd == 1) {
      digitalWrite(13, HIGH);
    }
    if (cmd == 0) {
      digitalWrite(13, LOW);
    }
  }
}
