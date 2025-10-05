import time
import requests
import adafruit_dht
import board
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# DHT22 sensor setup
DHT_PIN = board.D4  # Use board pin notation for compatibility with adafruit_dht
dht_device = adafruit_dht.DHT22(DHT_PIN)

# Blynk setup
BLYNK_TOKEN = "R4vdNzbRI1OvW4iFFNvlGkw87SSiaguH"
BLYNK_URL = "https://blynk.cloud/external/api/update"

# ThingSpeak setup
THINGSPEAK_API_KEY = "H0D24P8IQMPC0UY2"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

def send_to_blynk(temperature, humidity):
    try:
        temp_resp = requests.get(
            BLYNK_URL,
            params={"token": BLYNK_TOKEN, "V0": temperature},
            timeout=5
        )
        hum_resp = requests.get(
            BLYNK_URL,
            params={"token": BLYNK_TOKEN, "V1": humidity},
            timeout=5
        )
        temp_resp.raise_for_status()
        hum_resp.raise_for_status()
        logging.info("Data sent to Blynk successfully.")
    except requests.RequestException as e:
        logging.error(f"Error sending data to Blynk: {e}")

def send_to_thingspeak(temperature, humidity):
    payload = {
        'api_key': THINGSPEAK_API_KEY,
        'field1': temperature,
        'field2': humidity
    }
    try:
        resp = requests.get(THINGSPEAK_URL, params=payload, timeout=5)
        resp.raise_for_status()
        logging.info("Data sent to ThingSpeak successfully.")
    except requests.RequestException as e:
        logging.error(f"Error sending data to ThingSpeak: {e}")

def read_sensor():
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        if humidity is not None and temperature is not None:
            logging.info(f"Temp={temperature:.1f}C  Humidity={humidity:.1f}%")
            return temperature, humidity
        else:
            logging.warning("Sensor returned None values.")
            return None, None
    except RuntimeError as error:
        logging.warning(f"Sensor read error: {error}")
        return None, None
    except Exception as error:
        logging.error(f"Unexpected error: {error}")
        dht_device.exit()
        raise

def main():
    try:
        while True:
            temperature, humidity = read_sensor()
            if temperature is not None and humidity is not None:
                send_to_blynk(temperature, humidity)
                send_to_thingspeak(temperature, humidity)
            else:
                logging.info("Failed to retrieve data from sensor.")
            time.sleep(15)
    except KeyboardInterrupt:
        logging.info("Program terminated by user.")
    finally:
        dht_device.exit()

if __name__ == "__main__":
    main()