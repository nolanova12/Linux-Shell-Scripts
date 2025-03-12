#SCMakeyBot Robot Control
#Rasberry Pi Global Setting
from gpiozero import LED
import time 

#Using BCM GPIO3 I/O on BOARD pin 5
red_led = LED(3) # BCM GPIO3 = BOARD 5
def stop_light(_stop_light):
    print(_stop_light)
    
def main():
    print("Welcome to the STEAM Clown Makey Bot")
    while(True):
        print("LED on")
        red_led.on()
        time.sleep(1)
        print("LED off")
        red_led.off()
        time.sleep(1)
    traffic_light = {'red_LED':1, 'yellow_LED':1, 'green_LED':1}
    stop_light(traffic_light)
        
main() 