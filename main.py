from machine import Pin
import utime as time
from dht import DHT11
import time
import ubinascii
from simple import MQTTClient
import machine
from variables import Adafruit_username
from variables import Adafruit_password
import json

#Default MQTT_BROKER to connect to
Client_ID = ubinascii.hexlify(machine.unique_id())
MQTT_Broker = "io.adafruit.com"
Port = 1883
Publish_topic = b"kallebus/feeds/humandtemp.hum"
Publish_topic2 = b"kallebus/feeds/humandtemp.temp"
Threshhold_topic = "kallebus/feeds/thresh hold"
Subscribe_topic = b"kallebus/feeds/led"
last_publish = time.time()
publish_interval = 5
led = machine.Pin("LED",machine.Pin.OUT)
# The GPIO number is 13 which is equal to the pin number 17
pin = Pin(13, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

def sub_cb(topic, msg):
     print((topic, msg))
     if msg.decode() == "ON":
          led.value(1)
     else:
          led.value(0)

def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()

def main():
    print(f"Begin connection with MQTT Broker :: {MQTT_Broker}")
    mqttClient = MQTTClient(Client_ID, MQTT_Broker, Port, Adafruit_username, Adafruit_password, keepalive=60)
    mqttClient.set_callback(sub_cb)
    mqttClient.connect()
    mqttClient.subscribe(Subscribe_topic)
    print(f"connected to MQTT Broker:: {MQTT_Broker}")
    while True:
            mqttClient.check_msg()
            global last_publish
            if(time.time() - last_publish) >= publish_interval:
               dataHum = {
                "humidity": sensor.humidity
               }
               dataTemp = {
                "temperature": sensor.temperature,
               }
               payloadHum = json.dumps(dataHum)
               payloadTemp = json.dumps(dataTemp)
               mqttClient.publish(Publish_topic, payloadHum.encode())
               mqttClient.publish(Publish_topic2, payloadTemp.encode())
               if(int(sensor.temperature) >= 25):
                    print("Temperature reached 25°C!")
                    mqttClient.publish(Threshhold_topic, str("thresh hold has been reached 25 degrees").encode())
               time.sleep(1)

if __name__ == "__main__":
     while True:
            try:
               main()
            except OSError as e:
               print("Error: " + str(e))
               reset()
