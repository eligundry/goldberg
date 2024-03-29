import RPi.GPIO as GPIO
import random
import time

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

RED, GREEN, BLUE = {}, {}, {}

RED[0]   = GPIO.PWM(26, 100)
RED[1]   = GPIO.PWM(23, 100)
GREEN[0] = GPIO.PWM(24, 100)
GREEN[1] = GPIO.PWM(21, 100)
BLUE[0]  = GPIO.PWM(22, 100)
BLUE[1]  = GPIO.PWM(19, 100)

RED[0].start(0)
RED[1].start(0)
GREEN[0].start(0)
GREEN[1].start(0)
BLUE[0].start(0)
BLUE[1].start(0)

class Lights:
    def __init__(self, strand_num):
        self.red = 0
        self.blue = 0
        self.green = 0
        self.alpha = 0.0
        self.strand_num = strand_num

    def __exit__(self, type, value, traceback):
        RED[self.strand_num].stop()
        GREEN[self.strand_num].stop()
        BLUE[self.strand_num].stop()

        GPIO.output(26, 0)
        GPIO.output(24, 0)
        GPIO.output(22, 0)
        GPIO.output(23, 0)
        GPIO.output(21, 0)
        GPIO.output(19, 0)

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
        """
        Changes color and opacity of the lights
        """
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a

        temp = {
            'red': int(((self.red / 255.0) * 100) * self.alpha),
            'green': int(((self.green / 255.0) * 100) * self.alpha),
            'blue': int(((self.blue / 255.0) * 100) * self.alpha)
        }

        RED[self.strand_num].ChangeDutyCycle(temp['red'])
        GREEN[self.strand_num].ChangeDutyCycle(temp['green'])
        BLUE[self.strand_num].ChangeDutyCycle(temp['blue'])

    def fade_in(self, r, g, b, a, t):
        r = int(((r/255.0)*100)*a)
        g = int(((g/255.0)*100)*a)
        b = int(((b/255.0)*100)*a)
        a = int(a*100)
        for i in range(0, a, 2):
            if i < r:
                    RED[self.strand_num].ChangeDutyCycle(i)
            if i < g:
                    GREEN[self.strand_num].ChangeDutyCycle(i)
            if i < b:
                    BLUE[self.strand_num].ChangeDutyCycle(i)

            time.sleep(t / 50.0)


    def fade_out(self, r, g, b, a, t):
        r = int(((r/255.0)*100)*a)
        g = int(((g/255.0)*100)*a)
        b = int(((b/255.0)*100)*a)
        a = int(a*100)
        i = 0
        while i < 100:
        # for i in range(100, a, -2):
            RED[self.strand_num].ChangeDutyCycle(100 - i)
            GREEN[self.strand_num].ChangeDutyCycle(100 - i)
            BLUE[self.strand_num].ChangeDutyCycle(100 - i)

            print { self.strand_num, r, g, b, i }
            i += 1

            time.sleep(t / 50.0)

    def toggle_power(self):
        pass

    def light_show(self):
        pass

# Plant GPIO
GPIO.setup(16, GPIO.IN)
GPIO.setup(10, GPIO.OUT)

class Plant:
    def __init__(self):
        self.alive = True
        self.moisture = None
        self.get_moisture()

    def status(self):
        return {
            'alive': self.alive,
            'moisture': self.get_moisture()
        }

    def water(self, duration=3):
        """
        Waters the plant with the hose with optional time in seconds
        """
        GPIO.output(10, 1)
        time.sleep(duration)
        GPIO.output(10, 0)

        return True

    def get_moisture(self):
        """
        Gets the moisture of the soil from the soil hygrometer sensor
        """
        self.moisture = GPIO.input(16)
        return self.moisture == 1

# SnackBox GPIO
GPIO.setup(3, GPIO.OUT)

class SnackBox:
    def __init__(self):
        self.candy = True

    def disperse(self):
        """
        Drops a candy from it's flipper for all the children to enjoy
        """
        GPIO.output(3, 1)
        time.sleep(1)
        GPIO.output(3, 0)

class Pi:
    def __init__(self):
        self.light = [ Lights(0), Lights(1) ]
        self.plant = Plant()
        self.snack_box = SnackBox()
