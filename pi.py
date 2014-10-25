import random

class Lights():
    red = None
    blue = None
    green = None
    interval = 1000
    is_strobbing = False

    def __init__(self):
        self.random_color()

    def random_color(self):
        """
        Sets the RGB color of the lights to a random color
        """
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)

    def get_color(self):
        return {
            'r': self.red,
            'g': self.green,
            'b': self.blue
        }

    def set_color(self, r, g, b):
        self.red = r
        self.blue = g
        self.blue = b

    def start_strobe(self, interval=1000):
        """
        Stobes the LEDs with an optional interval in ms
        """
        self.is_strobbing = True

        # Put logic for strobing lights

        return true

    def stop_strobe(self):
        """
        Stops strobing the lights
        """
        self.is_strobbing = False

        # Put logic for stoping of the strobe lights

        return true

class Pi():
    lights = Lights()

    def __init__(self):
        return
