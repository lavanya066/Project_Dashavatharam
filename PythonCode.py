import time
import socket
import json

# ==========================================
# ESP32 NETWORK SETTINGS
# ==========================================

ESP32_IP = "192.168.1.39"
ESP32_PORT = 4210


# ==========================================
# UDP SOCKET
# ==========================================

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)


# ==========================================
# LIGHT COLORS
# ==========================================

COLORS = {
    "RED": 0x04,
    "ORANGE_RED": 0x08,
    "ORANGE": 0x0C,
    "YELLOW_ORANGE": 0x10,
    "LEMON_YELLOW": 0x14,

    "GREEN": 0x05,
    "GREENISH_BLUE": 0x09,
    "SKY_BLUE": 0x0D,
    "TURQUOISE": 0x11,
    "GREENISH_BLUE_2": 0x15,

    "BLUE": 0x06,
    "PURPLE": 0x0A,
    "VIOLET": 0x0E,
    "PINK": 0x12,
    "BABY_PINK": 0x16,
}


# ==========================================
# SEND LIGHT COMMAND
# ==========================================

def send_color(color):

    command = COLORS[color]

    data = {
        "device": "light",
        "address": 0xEF00,
        "command": command
    }

    message = json.dumps(data)

    print(f"LIGHT -> {color}")

    sock.sendto(
        message.encode(),
        (ESP32_IP, ESP32_PORT)
    )


# ==========================================
# SEND SERVO COMMAND
# ==========================================

def send_servo(channel, angle):

    data = {
        "device": "servo",
        "channel": channel,
        "angle": angle
    }

    message = json.dumps(data)

    print(f"SERVO CH{channel} -> {angle}°")

    sock.sendto(
        message.encode(),
        (ESP32_IP, ESP32_PORT)
    )


# ==========================================
# RUN AN AVATAR SCENE
# ==========================================

def run_avatar(name, color1, color2, servo_movements,
               scene_time=8, color_interval=1):

    print()
    print("================================")
    print(f"           {name}")
    print("================================")

    start_time = time.time()

    color_toggle = True
    movement_index = 0

    next_color_time = 0
    next_movement_time = 0

    while time.time() - start_time < scene_time:

        current_time = time.time()

        # ----------------------------------
        # LIGHT
        # ----------------------------------

        if current_time >= next_color_time:

            if color_toggle:
                send_color(color1)
            else:
                send_color(color2)

            color_toggle = not color_toggle

            next_color_time = current_time + color_interval


        # ----------------------------------
        # SERVO
        # ----------------------------------

        if current_time >= next_movement_time:

            angle = servo_movements[movement_index]

            send_servo(0, angle)

            movement_index += 1

            if movement_index >= len(servo_movements):
                movement_index = 0

            next_movement_time = current_time + 1


        # Small loop delay
        time.sleep(0.05)


# ==========================================
# AVATARS
# ==========================================


# ------------------------------------------
# 1. MATSYA
# ------------------------------------------

def matsya():

    run_avatar(
        name="MATSYA",
        color1="BLUE",
        color2="SKY_BLUE",

        servo_movements=[
            30,
            60,
            30,
            60
        ],

        scene_time=8,
        color_interval=1
    )


# ------------------------------------------
# 2. KURMA
# ------------------------------------------

def kurma():

    run_avatar(
        name="KURMA",
        color1="GREEN",
        color2="GREENISH_BLUE",

        servo_movements=[
            60,
            90,
            60,
            90
        ],

        scene_time=8,
        color_interval=1
    )


# ------------------------------------------
# 3. VARAHA
# ------------------------------------------

def varaha():

    run_avatar(
        name="VARAHA",
        color1="ORANGE",
        color2="YELLOW_ORANGE",

        servo_movements=[
            90,
            120,
            90,
            120
        ],

        scene_time=8,
        color_interval=1
    )


# ------------------------------------------
# 4. NARASIMHA
# ------------------------------------------

def narasimha():

    run_avatar(
        name="NARASIMHA",
        color1="RED",
        color2="ORANGE_RED",

        servo_movements=[
            90,
            150,
            90,
            150
        ],

        scene_time=8,
        color_interval=0.5
    )


# ------------------------------------------
# 5. VAMANA
# ------------------------------------------

def vamana():

    run_avatar(
        name="VAMANA",
        color1="YELLOW_ORANGE",
        color2="LEMON_YELLOW",

        servo_movements=[
            45,
            90,
            45,
            90
        ],

        scene_time=8,
        color_interval=1
    )


# ------------------------------------------
# 6. PARASHURAMA
# ------------------------------------------

def parashurama():

    run_avatar(
        name="PARASHURAMA",
        color1="GREEN",
        color2="TURQUOISE",

        servo_movements=[
            90,
            135,
            90,
            135
        ],

        scene_time=8,
        color_interval=0.75
    )


# ------------------------------------------
# 7. RAMA
# ------------------------------------------

def rama():

    run_avatar(
        name="RAMA",
        color1="SKY_BLUE",
        color2="GREENISH_BLUE",

        servo_movements=[
            60,
            120,
            60,
            120
        ],

        scene_time=8,
        color_interval=1
    )


# ------------------------------------------
# 8. KRISHNA
# ------------------------------------------

def krishna():

    run_avatar(
        name="KRISHNA",
        color1="BLUE",
        color2="PURPLE",

        servo_movements=[
            45,
            135,
            45,
            135
        ],

        scene_time=8,
        color_interval=0.75
    )


# ------------------------------------------
# 9. BUDDHA
# ------------------------------------------

def buddha():

    run_avatar(
        name="BUDDHA",
        color1="PURPLE",
        color2="VIOLET",

        servo_movements=[
            75,
            90,
            75,
            90
        ],

        scene_time=8,
        color_interval=1.5
    )


# ------------------------------------------
# 10. KALKI
# ------------------------------------------

def kalki():

    run_avatar(
        name="KALKI",
        color1="VIOLET",
        color2="RED",

        servo_movements=[
            90,
            180,
            90,
            180
        ],

        scene_time=8,
        color_interval=0.5
    )


# ==========================================
# DASHAVATARA SHOW
# ==========================================

print()
print("================================")
print("      DASHAVATARA SHOW")
print("================================")

matsya()
kurma()
varaha()
narasimha()
vamana()
parashurama()
rama()
krishna()
buddha()
kalki()


# ==========================================
# CLOSE SOCKET
# ==========================================

sock.close()

print()
print("================================")
print("       SHOW COMPLETE")
print("================================")