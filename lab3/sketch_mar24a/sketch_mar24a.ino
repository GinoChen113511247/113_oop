const int ledPin = 13;
bool ledState = false;
int fakeButton = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  

    if (command == '1') {
      ledState = true;
    } else if (command == '0') {
      ledState = false;
    }

    digitalWrite(ledPin, ledState ? HIGH : LOW);
  }


  Serial.print("LED: ");
  Serial.print(ledState ? "ON" : "OFF");
  Serial.print(" | Button: ");
  Serial.println(fakeButton ? "PRESSED" : "RELEASED");
  
  delay(500); 
}
