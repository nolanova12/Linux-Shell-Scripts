#SCMakeyBot Robot Control
#Rasberry Pi Global Setting
from gpiozero import LED
import time 

#Rasberry Pi Pins
#Using BCM GPIO3 I/O on BOARD pin 5
red_led = LED(3) # BCM GPIO3 = BOARD 5
yellow_led = LED(5)
green_led = LED(12)

print("Type the number between 1(for on) or 0(for off) for the light: red")
x = input()

print("Type the number between 1(for on) or 0(for off) for the light: yellow")
y = input()

print("Type the number between 1(for on) or 0(for off) for the light: green")
z = input()

def stop_light(traffic_status):
    print(traffic_status)
    red = traffic_status['red_LED']
    #red,yellow,green = traffic_status
    print(red)
    if(int(red) == 1):
        red_led.on()
    else:
        red_led.off()

def slow_light(traffic_status):
    yellow = traffic_status['yellow_LED']
    #red,yellow,green = traffic_status
    print(yellow)
    if(int(yellow) == 1):
        yellow_led.on()
    else:
        yellow_led.off()
        
def go_light(traffic_status):
    print(traffic_status)
    green = traffic_status['green_LED']
    #red,yellow,green = traffic_status
    print(green)
    if(int(green) == 1):
        green_led.on()
    else:
        green_led.off()
    
def main():
    print("Welcome to the STEAM Clown Makey Bot")
#    while(True):
 #       print("LED on")
  #      red_led.on()
   #     time.sleep(1)
    #    print("LED off")
     #   red_led.off()
      #  time.sleep(1)
    traffic_light = {'red_LED':x, 'yellow_LED':y, 'green_LED':z}
    stop_light(traffic_light)
  #  slow_light(traffic_light)
  #  go_light(traffic_light)
        
main() 