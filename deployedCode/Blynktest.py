import blynklib
import time

# Blynk authentication token
BLYNK_AUTH = 'Your_Blynk_Auth_Token'

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

try:
    print("Starting Blynk...")
    while True:
        blynk.run()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting...")
