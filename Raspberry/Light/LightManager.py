import RPi.GPIO as GPIO


class LightManager:

    def __init__(self, number_output):
        self._number_output = number_output
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(number_output, GPIO.OUT)

    def turn_on_light(self):
        GPIO.output(self._number_output, 1)
        return

    def turn_off_light(self):
        GPIO.output(self._number_output, 0)
        return

    def clear_gpio(self):
        GPIO.cleanup()
        return
