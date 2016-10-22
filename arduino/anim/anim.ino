const int PHOTO = A0;
const int BUTTON = 4;
const int RED = 15;
const int GREEN = 13;
const int BLUE = 12;

float t = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.print("button: ");
  Serial.print(digitalRead(BUTTON));
  Serial.print(" photo: ");
  Serial.println(analogRead(PHOTO));
  analogWrite(RED,   int(cos(0.3 * t) * 450 + 500));
  analogWrite(GREEN, int(cos(0.5 * t) * 450 + 500));
  analogWrite(BLUE,  int(cos(0.7 * t) * 450 + 500));
  delay(10);
  t += 0.01;
}

