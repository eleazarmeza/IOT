import random
import time
import sys
import json

from paho.mqtt import client as mqtt_client

topic = "srv/temperature"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        info = "Help!"
        loc = f"({random.randint(-100, 100)}, {random.randint(-100, 100)})"
        msg = json.dumps({ "msg": info, "loc": loc })
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Sent `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        time.sleep(7)


if __name__ == "__main__":
    broker = sys.argv[1]
    port = int(sys.argv[2])
    client = connect_mqtt()
    client.loop_start()
    publish(client)
