#include "DHT.h"

#define pinDHT 8
#define pinLight 9
#define pinRele1 12
#define pinRele2 11

DHT coopDHT(pinDHT, DHT11);

float temp = 0;
float hum = 0;
unsigned long previousMillis = 0;  // Stores the last time the method was called
const long interval = 1000;
bool doorOpen = true;
bool light = true;

void processCommand() {
  char c = Serial.read();
  if (c == 'j') {
    String json = "{\"temperature\":" + String(temp) + ", \"humidity\":" + String(hum) + "}";
    Serial.println(json);
  } else if (c == 'o') {
    doorOpen = true;
    serviceOutputs();
  } else if (c == 'c') {
    doorOpen = false;
    serviceOutputs();
  } else if (c == 'l') {
    light = true;
    serviceOutputs();
  } else if (c == 'd') {
    light = false;
    serviceOutputs();
  } else if (c == 's') {
    //String json = "{\"door\":" + String(doorOpen) + ", \"lamp\":" + String(light) + "}";
    String json = "{\"door\":" + String(doorOpen ? "\"open\"" : "\"close\"") + ", \"lamp\":" + String(light ? "\"on\"" : "\"off\"") + "}";
    Serial.println(json);
  }
}

void readDhtData() {
  float value = coopDHT.readTemperature();
  if (!isnan(value))
    temp = value;
  value = coopDHT.readHumidity();
  if (!isnan(value))
    hum = value;
}

void serviceOutputs() {
  if (doorOpen) {
    digitalWrite(pinRele1, HIGH);
    digitalWrite(pinRele2, LOW);
  } else {
    digitalWrite(pinRele1, LOW);
    digitalWrite(pinRele2, HIGH);
  }
  if (light) {
    digitalWrite(pinLight, HIGH);
  } else {
    digitalWrite(pinLight, LOW);
  }
  Serial.println("ok");
}

void setup() {
  
  pinMode(pinLight, OUTPUT);
  pinMode(pinRele1, OUTPUT);
  pinMode(pinRele2, OUTPUT);
  Serial.begin(9600);
  coopDHT.begin();
  serviceOutputs();
}

void loop() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    readDhtData();
  }
  processCommand();
}
