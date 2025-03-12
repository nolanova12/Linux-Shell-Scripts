from gpiozero import LED
import time

blink_led = LED(14)

while(True):
    print("LED on")
    blink_led.on()
    time.sleep(1)
    print("LED off")
    blink_led.off()
    time.sleep(1)
print('Done')




from gpiozero import LED
from gpiozero import Button
import time

print(dir(Button))

#Using BCM GPIO3 I/O on BOARD pin 5
red_led = LED(3) # BCM GPIO3 = BOARD 5
red_button = Button(7, pull_up = True, bounce_time)
While(True):
    #if(red_button.is_pressed):
    if(red_button.value == 1):
        print("Switch is pressed")
    else: