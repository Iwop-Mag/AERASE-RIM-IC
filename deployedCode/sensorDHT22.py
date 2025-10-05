import Adafruit_DHT
from flask import Flask, render_template_string

# DHT22 sensor type
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

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
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return round(temperature, 1), round(humidity, 1)
    else:
        return None, None

@app.route("/")
def index():
    temperature, humidity = get_sensor_data()
    return render_template_string(HTML_TEMPLATE, temperature=temperature, humidity=humidity)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)