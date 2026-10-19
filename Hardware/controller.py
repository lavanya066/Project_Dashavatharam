from config import COLORS, IR_ADDRESS
import time


class DashavataraController:

    def __init__(self, udp_client):

        self.udp = udp_client

    # -----------------------------
    # LIGHT
    # -----------------------------

    def light(self, color):

        if color not in COLORS:
            raise ValueError(
                f"Unknown color: {color}"
            )

        command = COLORS[color]

        self.udp.send({
            "device": "light",
            "address": IR_ADDRESS,
            "command": command
        })

        print(f"[LIGHT] {color}")

    # -----------------------------
    # SERVO
    # -----------------------------

    def servo(self, channel, angle):

        if not 0 <= channel <= 15:
            raise ValueError(
                f"Invalid PCA9685 channel: {channel}"
            )

        if not 0 <= angle <= 180:
            raise ValueError(
                f"Invalid servo angle: {angle}"
            )

        self.udp.send({
            "device": "servo",
            "channel": channel,
            "angle": angle
        })

        print(
            f"[SERVO] CH{channel} -> {angle}°"
        )
    def smooth_servo(self, channel, start_angle, end_angle, duration):

        steps = abs(end_angle - start_angle)

        if steps == 0:
            self.servo(channel, start_angle)
            return

        delay = duration / steps

        direction = 1 if end_angle > start_angle else -1

        for angle in range(
            start_angle,
            end_angle + direction,
            direction
        ):
            self.servo(channel, angle)
            time.sleep(delay)