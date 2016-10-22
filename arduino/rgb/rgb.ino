const int RED = 15;
const int GREEN = 13;
const int BLUE = 12;

void setup() {
}

void loop() {
  analogWrite(RED, 1023);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 0);
  delay(1000);

  analogWrite(RED, 0);
  analogWrite(GREEN, 1023);
  analogWrite(BLUE, 0);
  delay(1000);

  analogWrite(RED, 0);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 1023);
  delay(1000);
}
