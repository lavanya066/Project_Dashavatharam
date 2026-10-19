#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>

#include "IRModule.h"
#include "PCAModule.h"

// ==========================================
// Wi-Fi
// ==========================================

const char* ssid = "Airtel_muke_7514";
const char* password = "air46197";


// ==========================================
// UDP
// ==========================================

WiFiUDP udp;

const int UDP_PORT = 4210;


// ==========================================
// Handle incoming UDP packet
// ==========================================
void handlePackets()
{
  int packetsize=udp.parsePacket();
  if(!packetsize)
  {
    return;
  }
    // --------------------------------------
    // Read packet
    // --------------------------------------

    char buffer[256];
    int len=udp.read(buffer,sizeof(buffer)-1);
    if(len<=0)
    {
      return ;
    }
    buffer[len]='\0';
    Serial.println();
    Serial.println("==============================");
    Serial.print("Received JSON: ");
    Serial.println(buffer);

    // --------------------------------------
    // Parse JSON
    // --------------------------------------

    JsonDocument doc;

    DeserializationError error =
        deserializeJson(doc, buffer);
     if (error) {

        Serial.print("JSON error: ");
        Serial.println(error.c_str());

        return;
    }
    const char *device=doc["device"];
    if(device==nullptr)
    {
      Serial.println("ERROR: No device specified");

        return;
    }
    Serial.print("Device: ");
    Serial.println(device);
    if(strcmp(device,"light")==0)
    {
      Serial.println("Routing to IR module...");

        IRModule::handleLight(doc);
    }
    else if(strcmp(device,"servo")==0)
    {
        Serial.println("Routing to PCA9685...");


        uint8_t channel = doc["channel"];
        int angle = doc["angle"];


        Serial.print("Channel: ");
        Serial.println(channel);

        Serial.print("Angle: ");
        Serial.println(angle);


        PCAModule::setServoAngle(
            channel,
            angle
        );
    }
    else {

        Serial.print("Unknown device: ");
        Serial.println(device);
    }


    Serial.println("==============================");
}

// ==========================================
// SETUP
// ==========================================

void setup() {

    Serial.begin(115200);

    delay(1000);


    Serial.println();
    Serial.println("================================");
    Serial.println("       DASHAVATARA SYSTEM");
    Serial.println("================================");


    // ======================================
    // Start IR module
    // ======================================

    IRModule::begin();


    // ======================================
    // Start PCA9685
    // ======================================

    PCAModule::begin();


    // ======================================
    // Connect Wi-Fi
    // ======================================

    Serial.print("Connecting to WiFi");

    WiFi.begin(
        ssid,
        password
    );


    while (WiFi.status() != WL_CONNECTED) {

        delay(500);

        Serial.print(".");
    }


    Serial.println();

    Serial.println("WiFi connected!");


    Serial.print("ESP32 IP address: ");

    Serial.println(
        WiFi.localIP()
    );


    // ======================================
    // Start UDP
    // ======================================

    udp.begin(UDP_PORT);


    Serial.print("UDP server started on port ");

    Serial.println(UDP_PORT);


    Serial.println();
    Serial.println("================================");
    Serial.println("       SYSTEM READY");
    Serial.println("================================");
}


// ==========================================
// LOOP
// ==========================================

void loop() {

    handlePackets();

}