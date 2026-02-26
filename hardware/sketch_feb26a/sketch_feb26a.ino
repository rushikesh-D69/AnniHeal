#include <ArduinoJson.h>

void setup() {
  Serial.begin(115200);
}

void loop() {
  float temperature = random(360, 390) / 10.0;
  float gas = random(150, 300);
  float moisture = random(40, 80);

  StaticJsonDocument<200> doc;

  doc["temperature"] = temperature;
  doc["gas"] = gas;
  doc["moisture"] = moisture;

  serializeJson(doc, Serial);
  Serial.println();

  delay(2000);
}