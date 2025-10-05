import blynklib
import RPi.GPIO as GPIO
import time

# Blynk Auth Token (replace with your actual token from Blynk dashboard)
BLYNK_AUTH = 'xlpN8hJg3oSVPBzgvnH6mrswvbjp1Mp3'

# GPIO setup
LED_PIN = 4  # GPIO pin where LED is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# Handle Blynk virtual pin V0 write event
@blynk.handle_event('write V0')
def write_virtual_pin_handler(pin, value):
    # value is a list of strings, e.g. ['1'] or ['0']
    GPIO.output(LED_PIN, int(value[0]))

try:
    while True:
        blynk.run()
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
