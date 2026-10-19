#include "IRModule.h"

#include <IRremote.hpp>

namespace IRModule {

    // =========================
    // IR transmitter
    // =========================

    const int IR_SEND_PIN = 25;


    // =========================
    // Initialize IR
    // =========================

    void begin() {

        IrSender.begin(
            IR_SEND_PIN,
            DISABLE_LED_FEEDBACK
        );

        Serial.println("IR module ready");
    }


    // =========================
    // Handle LIGHT command
    // =========================

    void handleLight(JsonDocument& doc) {

        // Extract address and command
        uint16_t address = doc["address"];
        uint8_t command = doc["command"];


        Serial.print("Address: 0x");
        Serial.println(address, HEX);


        Serial.print("Command: 0x");
        Serial.println(command, HEX);


        // Send the exact NEC command
        IrSender.sendNEC(
            address,
            command,
            2
        );


        Serial.println("IR SENT");
    }

}