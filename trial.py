import subprocess
import os

sounds = [
    # "Matsya",
    # "Kurma",
    # "Varaha",
    # "Narasimha",
    # "Vamana",
    "Parashurama",
    # "Rama",
    # "Krishna",
    # "Balarama",
    # "Kalki"
]

for name in sounds:
    filename = f"Music/{name}.mp3"

    if not os.path.exists(filename):
        print(f"❌ Missing: {filename}")
        continue

    print(f"▶ Playing {name}")
    subprocess.run(["afplay", filename])

print("\nAll sounds tested.")