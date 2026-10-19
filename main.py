from Communication.udpClient import UDPClient
from Hardware.controller import DashavataraController
from Scenes.action import LightAction, ServoAction, WaitAction,SoundAction,SmoothServoAction,LightingSequenceAction,ParallelAction
from Scenes.Avatar import Avatar
from Show.dasavatharaShow import DashavataraShow
from config import ESP32_IP, ESP32_PORT
from config import SERVO_CHANNELS
from config import SOUNDS

# ============================================================
# CREATE AVATARS
# ============================================================
def create_matsya():

    matsya = Avatar(
        "MATSYA",
        [

            SoundAction(SOUNDS["MATSYA"]),

            # ============================================
            # 0s → 15s
            # SERVO: 0° → 180°
            # LIGHTS: FAST OCEAN / WATER MOVEMENT
            # ============================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["MATSYA"],
                    180,
                    0,
                    13
                ),

                LightingSequenceAction(
                    [
                        "BLUE",
                        "SKY_BLUE",
                        "GREENISH_BLUE",
                        "TURQUOISE",
                        "BLUE",
                        "GREENISH_BLUE_2",
                        "SKY_BLUE",
                        "TURQUOISE"
                    ],
                    duration=15,
                    interval=0.5
                )
            ]),
            ParallelAction([

                ServoAction(
                    SERVO_CHANNELS["MATSYA"],
                    0
                ),

                LightingSequenceAction(
                    [
                        "BLUE",
                        "SKY_BLUE",
                        "GREENISH_BLUE",
                        "TURQUOISE",
                        "BLUE",
                        "GREENISH_BLUE_2",
                        "SKY_BLUE",
                        "TURQUOISE"
                    ],
                    duration=4,
                    interval=0.5
                )
            ]),

            # ============================================
            # 15s → 30s
            # SERVO: 180° → 0°
            # LIGHTS: FAST RETURN / OCEAN WAVES
            # ============================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["MATSYA"],
                    0,
                    180,
                    13
                ),

                LightingSequenceAction(
                    [
                        "TURQUOISE",
                        "SKY_BLUE",
                        "BLUE",
                        "GREENISH_BLUE_2",
                        "TURQUOISE",
                        "GREENISH_BLUE",
                        "SKY_BLUE",
                        "BLUE"
                    ],
                    duration=15,
                    interval=0.5
                )
            ])
        ]
    )

    return matsya

def create_kurma():

    kurma = Avatar(
        "KURMA",
        [

            SoundAction(SOUNDS["KURMA"]),

            # ============================================
            # 0s → 15s
            # SERVO: 0° → 180°
            # COSMIC CHURNING BEGINS
            # ============================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["KURMA"],
                    180,
                    0,
                    13
                ),

                LightingSequenceAction(
                    [
                        "GREEN",
                        "GREENISH_BLUE",
                        "TURQUOISE",
                        "SKY_BLUE",
                        "GREENISH_BLUE_2",
                        "TURQUOISE"
                    ],
                    duration=13,
                    interval=0.5
                )
            ]),
            ParallelAction([
                ServoAction(
                    SERVO_CHANNELS["KURMA"],
                    0
                ),
                LightingSequenceAction(
                    [
                        "GREEN",
                        "GREENISH_BLUE",
                        "TURQUOISE",
                        "SKY_BLUE",
                        "GREENISH_BLUE_2",
                        "TURQUOISE"
                    ],
                    duration=4,
                    interval=0.4
                )
            ]),

            # ============================================
            # 15s → 30s
            # SERVO: 180° → 0°
            # SECOND COSMIC CHURN
            # ============================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["KURMA"],
                    0,
                    180,
                    13
                ),

                LightingSequenceAction(
                    [
                        "TURQUOISE",
                        "SKY_BLUE",
                        "GREENISH_BLUE_2",
                        "GREENISH_BLUE",
                        "TURQUOISE",
                        "GREEN"
                    ],
                    duration=13,
                    interval=0.4
                )
            ])
        ]
    )

    return kurma


def create_narasimha():

    narasimha = Avatar(
        "NARASIMHA",
        [

            SoundAction(SOUNDS["NARASIMHA"]),

            ParallelAction([

                # Servo:
                # 0° → 180° over 19.5 seconds
                SmoothServoAction(
                    SERVO_CHANNELS["NARASIMHA"],
                    180,
                    0,
                    17.5
                ),

                # Lights:
                # Rapid flashing for 19.5 seconds
                LightingSequenceAction(
                    [
                        "RED",
                        "ORANGE_RED",
                        "RED",
                        "ORANGE",
                        "ORANGE_RED"
                    ],
                    duration=17.5,
                    interval=0.4
                )
            ]),
            ParallelAction([
                ServoAction(
                    SERVO_CHANNELS["NARASIMHA"],
                    0
                ),
                LightingSequenceAction(
                    [
                        "RED",
                        "ORANGE_RED",
                        "RED",
                        "ORANGE",
                        "ORANGE_RED"
                    ],
                    duration=4,
                    interval=0.4
                )
            ]),
            

            ParallelAction([

                # Servo:
                # 180° → 0° over 19.5 seconds
                SmoothServoAction(
                    SERVO_CHANNELS["NARASIMHA"],
                    0,
                    180,
                    17.5
                ),

                # Lights:
                # Rapid flashing
                LightingSequenceAction(
                    [
                        "ORANGE_RED",
                        "RED",
                        "ORANGE",
                        "RED",
                        "ORANGE_RED"
                    ],
                    duration=17.5,
                    interval=0.3
                )
            ])
        ]
    )

    return narasimha
def create_vamana():

    vamana = Avatar(
        "VAMANA",
        [

            SoundAction(SOUNDS["VAMANA"]),

            # ============================================
            # 0s → 15s
            # VAMANA → TRIVIKRAMA
            # SERVO: 0° → 180°
            # ============================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["VAMANA"],
                    0,
                    180,
                    13
                ),

                LightingSequenceAction(
                    [
                        "YELLOW_ORANGE",
                        "LEMON_YELLOW",
                        "YELLOW_ORANGE",
                        "LEMON_YELLOW",
                        "ORANGE",
                        "LEMON_YELLOW",
                        "YELLOW_ORANGE"
                    ],
                    duration=13,
                    interval=0.4
                )
            ]),
            ParallelAction([
                ServoAction(
                    SERVO_CHANNELS["VAMANA"],
                    180
                ),
                LightingSequenceAction(
                    [
                        "YELLOW_ORANGE",
                        "LEMON_YELLOW",
                        "YELLOW_ORANGE",
                        "LEMON_YELLOW",
                        "ORANGE",
                        "LEMON_YELLOW",
                        "YELLOW_ORANGE"
                    ],
                    duration=4,
                    interval=0.4
                )
            ]),

            # ============================================
            # 15s → 30s
            # TRIVIKRAMA → SACRED CALM
            # SERVO: 180° → 0°
            # ============================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["VAMANA"],
                    180,
                    0,
                    13
                ),

                LightingSequenceAction(
                    [
                        "LEMON_YELLOW",
                        "YELLOW_ORANGE",
                        "LEMON_YELLOW",
                        "ORANGE",
                        "YELLOW_ORANGE",
                        "LEMON_YELLOW",
                        "YELLOW_ORANGE"
                    ],
                    duration=13,
                    interval=0.45
                )
            ])
        ]
    )

    return vamana
def create_varaha():

    varaha = Avatar(
        "VARAHA",
        [

            SoundAction(SOUNDS["VARAHA"]),

            # ============================================
            # 0s → 15s
            # PRIMORDIAL OCEAN → VARAHA EMERGES
            # SERVO: 0° → 180°
            # ============================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["VARAHA"],
                    0,
                    180,
                    15
                ),

                LightingSequenceAction(
                    [
                        "ORANGE",
                        "YELLOW_ORANGE",
                        "ORANGE",
                        "ORANGE_RED",
                        "YELLOW_ORANGE",
                        "ORANGE",
                        "LEMON_YELLOW",
                        "ORANGE_RED"
                    ],
                    duration=15,
                    interval=0.45
                )
            ]),

            # ============================================
            # 15s → 30s
            # BHUDEVI LIFTED → DIVINE CALM
            # SERVO: 180° → 0°
            # ============================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["VARAHA"],
                    180,
                    0,
                    15
                ),

                LightingSequenceAction(
                    [
                        "ORANGE_RED",
                        "ORANGE",
                        "LEMON_YELLOW",
                        "YELLOW_ORANGE",
                        "ORANGE",
                        "ORANGE_RED",
                        "YELLOW_ORANGE",
                        "ORANGE"
                    ],
                    duration=15,
                    interval=0.4
                )
            ])
        ]
    )

    return varaha
def create_parashurama():

    parashurama = Avatar(
        "PARASHURAMA",
        [

            SoundAction(SOUNDS["PARASHURAMA"]),

            # ==================================================
            # 0s → 24s
            # DIVINE WARRIOR AWAKENING
            # SERVO: 0° → 180°
            # LIGHTS: FAST LIGHTNING
            # ==================================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["PARASHURAMA"],
                    0,
                    180,
                    24
                ),

                LightingSequenceAction(
                    [
                        "GREEN",
                        "TURQUOISE",
                        "GREEN",
                        "LEMON_YELLOW",
                        "TURQUOISE",
                        "GREEN",
                        "LEMON_YELLOW",
                        "GREEN",
                        "TURQUOISE",
                    ],
                    duration=24,
                    interval=0.3
                )
            ]),

            # ==================================================
            # 24s → 48s
            # DIVINE AXE FURY → FINAL STRIKE
            # SERVO: 180° → 0°
            # LIGHTS: EXTREME LIGHTNING
            # ==================================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["PARASHURAMA"],
                    180,
                    0,
                    24
                ),

                LightingSequenceAction(
                    [
                        "LEMON_YELLOW",
                        "GREEN",
                        "LEMON_YELLOW",
                        "TURQUOISE",
                        "LEMON_YELLOW",
                        "GREEN",
                        "LEMON_YELLOW",
                        "TURQUOISE",
                        "GREEN",
                    ],
                    duration=24,
                    interval=0.2
                )
            ])
        ]
    )

    return parashurama

def create_rama():

    rama = Avatar(
        "RAMA",
        [

            SoundAction(SOUNDS["RAMA"]),

            # ==================================================
            # 0s → 29s
            # SERENE BEGINNING → BOW DRAW → DIVINE ARROW
            # SERVO: 0° → 180°
            # ==================================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["RAMA"],
                    0,
                    180,
                    33.5
                ),

                LightingSequenceAction(
                    [
                        "SKY_BLUE",
                        "GREENISH_BLUE",
                        "SKY_BLUE",
                        "GREENISH_BLUE",
                        "SKY_BLUE",
                        "LEMON_YELLOW",
                        "SKY_BLUE",
                        "GREENISH_BLUE",
                    ],
                    duration=33.5,
                    interval=0.5
                )
            ]),

            # ==================================================
            # 29s → 58s
            # VICTORY → DHARMA RESTORED → SACRED ENDING
            # SERVO: 180° → 0°
            # ==================================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["RAMA"],
                    180,
                    0,
                    33.5
                ),

                LightingSequenceAction(
                    [
                        "LEMON_YELLOW",
                        "SKY_BLUE",
                        "GREENISH_BLUE",
                        "SKY_BLUE",
                        "LEMON_YELLOW",
                        "SKY_BLUE",
                        "GREENISH_BLUE",
                        "SKY_BLUE",
                    ],
                    duration=33.5,
                    interval=0.5
                )
            ])
        ]
    )

    return rama


def create_krishna():

    krishna = Avatar(
        "KRISHNA",
        [

            SoundAction(SOUNDS["KRISHNA"]),

            # ==================================================
            # 0s → 22s
            # PLAYFUL VRINDAVAN → DIVINE FLUTE PEAK
            # SERVO: 0° → 180°
            # ==================================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["KRISHNA"],
                    0,
                    180,
                    20
                ),

                LightingSequenceAction(
                    [
                        "BLUE",
                        "PURPLE",
                        "PINK",
                        "BABY_PINK",
                        "VIOLET",
                        "BLUE",
                        "PINK",
                        "PURPLE",
                    ],
                    duration=20,
                    interval=0.4
                )
            ]),
            ParallelAction([
                ServoAction(
                    SERVO_CHANNELS["KRISHNA"],
                    180
                ),
                LightingSequenceAction(
                    [
                        "PINK",
                        "PURPLE",
                        "BLUE",
                        "BABY_PINK",
                        "VIOLET",
                        "PINK",
                        "LEMON_YELLOW",
                        "BLUE",
                    ],
                    duration=4,
                    interval=0.4
                )
            ]),

            # ==================================================
            # 22s → 44s
            # RADHA → PLAYFUL FLOURISH → FLUTE ENDING
            # SERVO: 180° → 0°
            # ==================================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["KRISHNA"],
                    180,
                    0,
                    20
                ),

                LightingSequenceAction(
                    [
                        "PINK",
                        "PURPLE",
                        "BLUE",
                        "BABY_PINK",
                        "VIOLET",
                        "PINK",
                        "LEMON_YELLOW",
                        "BLUE",
                    ],
                    duration=20,
                    interval=0.4
                )
            ])
        ]
    )

    return krishna

def create_balarama():

    balarama = Avatar(
        "BALARAMA",
        [

            SoundAction(SOUNDS["BALARAMA"]),

            # ==================================================
            # 0s → 12s
            # STRENGTH AWAKENS → PLOUGH RISES
            # SERVO: 0° → 180°
            # ==================================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["BALARAMA"],
                    0,
                    180,
                    12
                ),

                LightingSequenceAction(
                    [
                        "PURPLE",
                        "VIOLET",
                        "PURPLE",
                        "VIOLET",
                        "PURPLE",
                        "VIOLET",
                        "LEMON_YELLOW",
                    ],
                    duration=12,
                    interval=0.4
                )
            ]),

            # ==================================================
            # 12s → 24s
            # PLOUGH SWING → VICTORIOUS STANCE
            # SERVO: 180° → 0°
            # ==================================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["BALARAMA"],
                    180,
                    0,
                    12
                ),

                LightingSequenceAction(
                    [
                        "VIOLET",
                        "PURPLE",
                        "VIOLET",
                        "PURPLE",
                        "LEMON_YELLOW",
                        "VIOLET",
                        "PURPLE",
                    ],
                    duration=12,
                    interval=0.35
                )
            ])
        ]
    )

    return balarama

def create_kalki():

    kalki = Avatar(
        "KALKI",
        [

            SoundAction(SOUNDS["KALKI"]),

            # ==================================================
            # 0s → 23s
            # DARKNESS → KALKI ARRIVES
            # SERVO: 0° → 180°
            # ==================================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["KALKI"],
                    0,
                    180,
                    23
                ),

                LightingSequenceAction(
                    [
                        "VIOLET",
                        "RED",
                        "VIOLET",
                        "ORANGE_RED",
                        "RED",
                        "VIOLET",
                        "ORANGE_RED",
                        "RED",
                        "LEMON_YELLOW",
                    ],
                    duration=23,
                    interval=0.35
                )
            ]),

            # ==================================================
            # 23s → 46s
            # DIVINE STRIKES → VICTORY → NEW AGE
            # SERVO: 180° → 0°
            # ==================================================

            ParallelAction([

                SmoothServoAction(
                    SERVO_CHANNELS["KALKI"],
                    180,
                    0,
                    23
                ),

                LightingSequenceAction(
                    [
                        "RED",
                        "ORANGE_RED",
                        "LEMON_YELLOW",
                        "RED",
                        "VIOLET",
                        "ORANGE_RED",
                        "LEMON_YELLOW",
                        "RED",
                        "VIOLET",
                    ],
                    duration=23,
                    interval=0.25
                )
            ])
        ]
    )

    return kalki

def create_avatars():

    # ============================================================
    # AVATAR DEFINITIONS
    # ============================================================


    # ------------------------------------------------------------
    # 1. MATSYA
    # ------------------------------------------------------------

    matsya = create_matsya()


    # ------------------------------------------------------------
    # 2. KURMA
    # ------------------------------------------------------------

    kurma = create_kurma()


    # ------------------------------------------------------------
    # 3. VARAHA
    # ------------------------------------------------------------

    varaha = create_varaha()


    # ------------------------------------------------------------
    # 4. NARASIMHA
    # ------------------------------------------------------------

    narasimha = create_narasimha()


    # ------------------------------------------------------------
    # 5. VAMANA
    # ------------------------------------------------------------

    vamana = create_vamana()


    # ------------------------------------------------------------
    # 6. PARASHURAMA
    # ------------------------------------------------------------

    parashurama = create_parashurama()


    # ------------------------------------------------------------
    # 7. RAMA
    # ------------------------------------------------------------

    rama = create_rama()


    # ------------------------------------------------------------
    # 8. KRISHNA
    # ------------------------------------------------------------

    krishna = create_krishna()
    # ------------------------------------------------------------
    # 9. BALARAMA
    # ------------------------------------------------------------

    balarama = create_balarama()

    # ------------------------------------------------------------
    # 10. KALKI
    # ------------------------------------------------------------

    kalki = create_kalki()

    return [
    matsya,
    kurma,
    varaha,
    narasimha,
    vamana,
    parashurama,
    rama,
    balarama,
    krishna,
    kalki
]

def main():

    print()
    print("========================================")
    print("       DASHAVATARA CONTROLLER")
    print("========================================")
    
    # --------------------------------------------------------
    # 1. CREATE UDP COMMUNICATION
    # --------------------------------------------------------
    udp_client = UDPClient(ESP32_IP, ESP32_PORT)

    # --------------------------------------------------------
    # 2. CREATE HARDWARE CONTROLLER
    # --------------------------------------------------------
    hardware_controller = DashavataraController(udp_client)

    # --------------------------------------------------------
    # 3. CREATE SHOW
    # --------------------------------------------------------
    show = DashavataraShow(hardware_controller)

    # --------------------------------------------------------
    # 4. CREATE AVATARS
    # --------------------------------------------------------
    avatars = create_avatars()

    for avatar in avatars:
        show.add_avatar(avatar)

    try:

        show.play()

    except KeyboardInterrupt:

        print()
        print("Show stopped by user.")

    finally:

        udp_client.close()

        print()
        print("UDP connection closed.")
# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()
