#ifndef IR_MODULE_H
#define IR_MODULE_H

#include <Arduino.h>
#include <ArduinoJson.h>

namespace IRModule {

    void begin();

    // Process a light command from JSON
    void handleLight(JsonDocument& doc);

}

#endif