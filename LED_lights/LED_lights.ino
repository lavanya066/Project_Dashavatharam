#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>
#include <IRremote.hpp>

#define IR_SEND_PIN 25

const char* ssid = "Airtel_muke_7514";
const char* password = "air46197";

WiFiUDP udp;

const int UDP_PORT = 4210;


void handleLight() {

  int packetSize = udp.parsePacket();

  if (packetSize) {

    char buffer[256];

    int len = udp.read(buffer, sizeof(buffer) - 1);

    if (len > 0) {
      buffer[len] = '\0';
    }

    Serial.print("Received JSON: ");
    Serial.println(buffer);


    // Parse JSON
    JsonDocument doc;

    DeserializationError error =
        deserializeJson(doc, buffer);

    if (error) {

      Serial.print("JSON error: ");
      Serial.println(error.c_str());

      return;
    }


    // Extract values
    uint16_t address = doc["address"];
    uint8_t command = doc["command"];


    Serial.print("Address: 0x");
    Serial.println(address, HEX);

    Serial.print("Command: 0x");
    Serial.println(command, HEX);


    // Send IR
    IrSender.sendNEC(address, command, 2);

    Serial.println("IR SENT");
  }
}


void setup() {

  Serial.begin(115200);


  // Start IR transmitter
  IrSender.begin(IR_SEND_PIN, DISABLE_LED_FEEDBACK);


  // Connect to WiFi
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");


  while (WiFi.status() != WL_CONNECTED) {

    delay(500);

    Serial.print(".");
  }


  Serial.println();

  Serial.println("WiFi connected!");


  Serial.print("ESP32 IP address: ");

  Serial.println(WiFi.localIP());


  // Start UDP server
  udp.begin(UDP_PORT);

  Serial.print("UDP server started on port ");

  Serial.println(UDP_PORT);
}


void loop() {

  handleLight();
}