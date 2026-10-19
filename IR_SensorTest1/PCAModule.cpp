#include "PCAModule.h"

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


namespace PCAModule {

    // ==========================================
    // PCA9685
    // ==========================================

    Adafruit_PWMServoDriver pwm(0x40);


    // ==========================================
    // ESP32 I2C pins
    // ==========================================

    const int SDA_PIN = 21;
    const int SCL_PIN = 22;


    // ==========================================
    // SG90 PWM limits
    // ==========================================

    const int SERVO_MIN = 200;
    const int SERVO_MAX = 500;


    // ==========================================
    // Convert angle to PWM
    // ==========================================

    int angleToPulse(int angle)
    {
        // Keep angle between 0 and 180
        angle = constrain(angle, 0, 180);

        return map(
            angle,
            0,
            180,
            SERVO_MIN,
            SERVO_MAX
        );
    }


    // ==========================================
    // Initialize PCA9685
    // ==========================================

    void begin()
    {
        Serial.println("Starting PCA9685...");

        // Start I2C
        Wire.begin(
            SDA_PIN,
            SCL_PIN
        );

        // Start PCA9685
        pwm.begin();

        // SG90 uses 50 Hz
        pwm.setPWMFreq(50);

        delay(500);

        Serial.println("PCA9685 ready");
    }


    // ==========================================
    // Set servo angle
    // ==========================================

    void setServoAngle(
        uint8_t channel,
        int angle
    )
    {
        // ======================================
        // Check channel
        // ======================================

        if (channel > 15)
        {
            Serial.print("ERROR: Invalid PCA9685 channel: ");
            Serial.println(channel);

            return;
        }


        // ======================================
        // Check angle
        // ======================================

        if (angle < 0 || angle > 180)
        {
            Serial.print("ERROR: Invalid servo angle: ");
            Serial.println(angle);

            return;
        }


        // ======================================
        // Convert angle → PWM
        // ======================================

        int pulse = angleToPulse(angle);


        // ======================================
        // Send PWM
        // ======================================

        pwm.setPWM(
            channel,
            0,
            pulse
        );


        // ======================================
        // Debug
        // ======================================

        Serial.print("Servo CH");
        Serial.print(channel);

        Serial.print(" -> ");
        Serial.print(angle);

        Serial.print(" degrees | PWM = ");
        Serial.println(pulse);
        
    }

}