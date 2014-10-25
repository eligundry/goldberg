import RPi.GPIO as GPIO
import random
import time

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

RED = GPIO.PWM(26, 100)
GREEN = GPIO.PWM(24, 100)
BLUE = GPIO.PWM(22, 100)

RED.start(0)
GREEN.start(0)
BLUE.start(0)

class Lights():
    red = None
    blue = None
    green = None
    alpha = 1.0

    def __init__(self):
        self.random_color()

    def random_color(self):
        """
        Sets the RGB color of the lights to a random color
        """
        self.set_color(r=random.randint(0, 255), g=random.randint(0, 255),
                       b=random.randint(0, 255), a=1.0)

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

        temp = {
            'red': int(((self.red / 255.0) * 100) * self.alpha),
            'green': int(((self.green / 255.0) * 100) * self.alpha),
            'blue': int(((self.blue / 255.0) * 100) * self.alpha)
        }

        RED.ChangeDutyCycle(temp['red'])
        GREEN.ChangeDutyCycle(temp['green'])
        BLUE.ChangeDutyCycle(temp['blue'])

        return True

    def lights_on(self):
        self.set_color(a=1.0)

    def lights_off(self):
        self.set_color(0.0)

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
