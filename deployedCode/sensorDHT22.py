import adafruit_dht
import board
from flask import Flask, render_template_string

# Initialize DHT22 sensor on GPIO4
dhtDevice = adafruit_dht.DHT22(board.D4)

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DHT22 Sensor Status</title>
    <meta http-equiv="refresh" content="2">
</head>
<body>
    <h1>DHT22 Sensor Readings</h1>
    {% if temperature is not none and humidity is not none %}
        <p>Temperature: {{ temperature }} &deg;C</p>
        <p>Humidity: {{ humidity }} %</p>
    {% else %}
        <p>Failed to retrieve data from DHT22 sensor</p>
    {% endif %}
</body>
</html>
"""

def get_sensor_data():
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        if temperature is not None and humidity is not None:
            return round(temperature, 1), round(humidity, 1)
        else:
            return None, None
    except RuntimeError as e:
        print(f"Sensor read error: {e}")
        return None, None

@app.route("/")
def index():
    temperature, humidity = get_sensor_data()
    return render_template_string(HTML_TEMPLATE, temperature=temperature, humidity=humidity)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)