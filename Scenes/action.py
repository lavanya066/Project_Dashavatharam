import time
import subprocess
import threading

class Action:

    def execute(self, controller):
        raise NotImplementedError

class LightAction(Action):

    def __init__(self, color):

        self.color = color

    def execute(self, controller):

        controller.light(self.color)

class ServoAction(Action):

    def __init__(self, channel, angle):

        self.channel = channel
        self.angle = angle

    def execute(self, controller):

        controller.servo(
            self.channel,
            self.angle
        )

class WaitAction(Action):

    def __init__(self, duration):

        self.duration = duration

    def execute(self, controller):

        time.sleep(self.duration)

class SoundAction(Action):

    def __init__(self, filename):
        self.filename = filename

    def execute(self, controller):

        print(f"[SOUND] Playing: {self.filename}")

        subprocess.Popen([
            "afplay",
            self.filename
        ])
class SmoothServoAction(Action):

    def __init__(self, channel, start_angle, end_angle, duration):
        self.channel = channel
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.duration = duration

    def execute(self, controller):
        controller.smooth_servo(
            self.channel,
            self.start_angle,
            self.end_angle,
            self.duration
        )
        

class LightingSequenceAction(Action):

    def __init__(self, colors, duration, interval=0.5):
        self.colors = colors
        self.duration = duration
        self.interval = interval

    def execute(self, controller):

        start_time = time.time()
        index = 0

        while time.time() - start_time < self.duration:

            color = self.colors[index % len(self.colors)]

            controller.light(color)

            index += 1

            time.sleep(self.interval)


# ============================================================
# PARALLEL ACTION
# ============================================================

class ParallelAction(Action):

    def __init__(self, actions):
        self.actions = actions

    def execute(self, controller):

        threads = []

        for action in self.actions:

            thread = threading.Thread(
                target=action.execute,
                args=(controller,)
            )

            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()