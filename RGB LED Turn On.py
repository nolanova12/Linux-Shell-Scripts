import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for RGB channels
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

# Set up each pin as an output
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Set the PWM for each color pin (using a frequency of 100Hz)
red_pwm = GPIO.PWM(RED_PIN, 100)
green_pwm = GPIO.PWM(GREEN_PIN, 100)
blue_pwm = GPIO.PWM(BLUE_PIN, 100)

# Start PWM with 0% duty cycle (off)
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

# Function to set color
def set_color(red, green, blue):
    red_pwm.ChangeDutyCycle(red)
    green_pwm.ChangeDutyCycle(green)
    blue_pwm.ChangeDutyCycle(blue)

try:
    # Example: set to red
    set_color(100, 0, 0)
    time.sleep(2)
    
    # Example: set to green
    set_color(0, 100, 0)
    time.sleep(2)
    
    # Example: set to blue
    set_color(0, 0, 100)
    time.sleep(2)

    # Example: set to purple (red + blue)
    set_color(100, 0, 100)
    time.sleep(2)

    # Example: set to white (all colors at full brightness)
    set_color(100, 100, 100)
    time.sleep(2)

finally:
    # Cleanup the GPIO setup
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()

