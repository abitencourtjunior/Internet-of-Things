
import time

from Light.LightManager import LightManager

light = LightManager(2)
try:
    print(f"Run function - {LightManager.__name__.title()}")

    while True:
        light.turn_off_light()
        time.sleep(2)
        light.turn_on_light()
        time.sleep(5)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")

except:
   print("Bug of Hardware ?")

finally:
    print("Clear GPIO")
    light.clear_gpio()


