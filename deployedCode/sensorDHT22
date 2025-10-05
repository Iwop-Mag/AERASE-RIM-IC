import Adafruit_DHT
import time

# DHT22 sensor type
DHT_SENSOR = Adafruit_DHT.DHT22

# GPIO pin where the data pin of DHT22 is connected (e.g., GPIO4)
DHT_PIN = 4

def read_dht22():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f"Temp={temperature:.1f}C  Humidity={humidity:.1f}%")
    else:
        print("Failed to retrieve data from DHT22 sensor")

if __name__ == "__main__":
    while True:
        read_dht22()
        time.sleep(2)