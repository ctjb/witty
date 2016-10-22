const int PHOTO = A0;
const int BUTTON = 4;
const int RED = 15;
const int GREEN = 13;
const int BLUE = 12;

int which = 0;

void setup() {
}

void loop() {
  int light = analogRead(PHOTO);
  int button = digitalRead(BUTTON);

  if (button == 0 || light < 700) {
    analogWrite(RED,   (which == 0) ? 1023 : 0);
    analogWrite(GREEN, (which == 1) ? 1023 : 0);
    analogWrite(BLUE,  (which == 2) ? 1023 : 0);
    which = (which + 1) % 3;
    delay(300);
  }

}

