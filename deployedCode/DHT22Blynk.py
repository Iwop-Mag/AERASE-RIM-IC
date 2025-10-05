import blynklib
import adafruit_dht
import board
import time

# 🔑 Replace with your Device Auth Token from Blynk Console (Device Info)
BLYNK_AUTH = "xlpN8hJg3oSVPBzgvnH6mrswvbjp1Mp3"

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# Setup DHT22 sensor on GPIO4 (pin 7 on Pi header)
dht_device = adafruit_dht.DHT22(board.D4)

# Virtual Pins in your Blynk Template
VPIN_TEMP = 0   # V1 for Temperature
VPIN_HUM = 1    # V2 for Humidity

print("Starting DHT22 → Blynk bridge...")

while True:
    try:
        blynk.run()  # keep Blynk connection alive

        # Read sensor
        temperature = dht_device.temperature
        humidity = dht_device.humidity

        if temperature is not None and humidity is not None:
            print(f"Temp={temperature:.1f}°C  Humidity={humidity:.1f}%")

            # Send to Blynk Virtual Pins
            blynk.virtual_write(VPIN_TEMP, temperature)
            blynk.virtual_write(VPIN_HUM, humidity)
        else:
            print("Sensor returned None values.")

    except RuntimeError as e:
        # DHT sensors often fail a read; just retry
        print("Sensor read error:", e)

    except Exception as e:
        # Fatal error (e.g. hardware issue)
        print("Unexpected error:", e)
        dht_device.exit()
        raise

    time.sleep(5)  # ThingSpeak requires ≥15s, but Blynk is fine with 5s
