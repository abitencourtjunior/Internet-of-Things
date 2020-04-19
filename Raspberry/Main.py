
import time

from Raspberry.Light.LightManager import LightManager

light = LightManager(2)

while True:
    light.turn_off_light()
    time.sleep(2)
    light.turn_on_light()


