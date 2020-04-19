
import time

from Light.LightManager import LightManager

light_one = LightManager(2)
light_two = LightManager(3)
try:
    print(f"Run function - {LightManager.__name__.title()}")

    while True:
        light_one.turn_off_light()
        time.sleep(2)
        light_two.turn_on_light()
        time.sleep(2)
        light_one.turn_on_light()
        time.sleep(2)
        light_two.turn_off_light()
        time.sleep(2)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")

except:
   print("Bug of Hardware ?")

finally:
    print("Clear GPIO")
    light_one.clear_gpio()
    light_two.clear_gpio()


