#include <ESP8266WiFi.h>
#include <WiFiClient.h>

WiFiClient client;

void setup() {
  Serial.begin(115200);
  Serial.setDebugOutput(true);

  WiFi.mode(WIFI_STA);
  WiFi.begin("SSID", "password");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());

  if (client.connect("ctjb.net", 80)) {
    Serial.println("Connected to server");
    client.println("GET /kontakt?do=export_raw HTTP/1.1");
    client.println("Host: ctjb.net");
    client.println("Connection: close");
    client.println();
  } else {
    Serial.println("Connection failed to server");
  }

  delay(500);

  while (client.available()) {
    char c = client.read();
    Serial.print(c);
  }

  delay(500);

  if (!client.connected()) {
    Serial.println();
    Serial.println("Disconnecting");
    client.stop();
  }
}

void loop() {
}
