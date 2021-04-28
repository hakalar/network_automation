from pynput.mouse import Button, Controller
import time
import random

# https://nitratine.net/blog/post/simulate-mouse-events-in-python/

mouse = Controller()
print ("Current position: " + str(mouse.position))
mouse.position = (10, 20)

# while True:
#     print(random.randrange(-20,20,1))

while True:
    mouse.move(random.randrange(-20,20,1), random.randrange(-20,20,1))
    time.sleep(5)
    mouse.move(random.randrange(-20,20,1), random.randrange(-20,20,1))
    time.sleep(5)
    mouse.move(random.randrange(-20,20,1), random.randrange(-20,20,1))

