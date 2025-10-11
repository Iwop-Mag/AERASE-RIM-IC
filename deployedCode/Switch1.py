import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import json

# ThingsBoard setup
THINGSBOARD_HOST = "thingsboard.cloud"   # or your server
ACCESS_TOKEN = "rjrzaho1k6mvyij8ogc1"

# GPIO setup
SWITCH_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    # Subscribe to RPC requests
    client.subscribe("v1/devices/me/rpc/request/+")
    
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    method = data.get("method")
    params = data.get("params")
    
    if method == "setState":
        if params:
            GPIO.output(SWITCH_PIN, GPIO.HIGH)
            print("Switch 1 ON")
        else:
            GPIO.output(SWITCH_PIN, GPIO.LOW)
            print("Switch 1 OFF")
            
    response_topic = msg.topic.replace("request", "response")
    client.publish(response_topic, json.dumps({"result": "ok"}))


client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.on_connect = on_connect
client.on_message = on_message

client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_forever()