#ifndef PCA_MODULE_H
#define PCA_MODULE_H

#include <Arduino.h>

namespace PCAModule {

    // Initialize PCA9685
    void begin();

    // Move a servo connected to a PCA9685 channel
    void setServoAngle(uint8_t channel, int angle);

}

#endif