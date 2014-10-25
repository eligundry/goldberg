import random
import time

class Lights():
    red = None
    blue = None
    green = None
    alpha = 100

    def __init__(self):
        self.random_color()

    def random_color(self):
        """
        Sets the RGB color of the lights to a random color
        """
        self.set_color(r=random.randint(0, 255), g=random.randint(0, 255),
                       b=random.randint(0, 255), a=100)

    def get_color(self):
        return {
            'r': self.red,
            'g': self.green,
            'b': self.blue,
            'a': self.alpha
        }

    def set_color(self, r, g, b, a):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a

        # Put logic for changing light color here

        return True

    def is_on(self):
        return self.alpha is not 0

class Plant():
    alive = True
    moisture = None

    def __init__(self):
        self.get_moisture()

    def status(self):
        return {
            'alive': self.alive,
            'moisture': self.get_moisture()
        }

    def water(self):
        """
        Waters the plant with the hose and shit
        """
        return True

    def get_moisture(self):
        """
        Gets the moisture of the soil from the soil hygrometer sensor
        """
        # Dummy value for moisture cause I don't have time to lookup the pinout
        # Logic for moisture module goes here
        self.moisture = random.randint(0, 255)
        return self.moisture

class Pi():
    lights = Lights()
    plant = Plant()

    def __init__(self):
        return
