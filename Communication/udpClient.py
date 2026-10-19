import socket
import json

from config import ESP32_IP, ESP32_PORT


class UDPClient:

    def __init__(self, ip=ESP32_IP, port=ESP32_PORT):

        self.ip = ip
        self.port = port

        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

    def send(self, data):

        message = json.dumps(data)

        print(f"[UDP] {message}")

        self.socket.sendto(
            message.encode(),
            (self.ip, self.port)
        )

    def close(self):

        self.socket.close()