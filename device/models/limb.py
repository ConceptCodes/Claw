from machine import Pin

class Limb:
    def __init__(self, gpio_pin: int):
        self.limb = Pin(gpio_pin, Pin.OUT)

    def move(self, degrees: int):
        #convert degrees to duty cycles
        self.limb.duty(degrees)