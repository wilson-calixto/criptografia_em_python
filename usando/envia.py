# -*- coding: utf-8 -*-
__author__ = ''
import pyDes
import sys
import time
import paho.mqtt.client as mqtt
from collections import namedtuple

Auth = namedtuple('Auth', ['user', 'pwd'])
MQTT_ADDRESS = '127.0.0.1'

MQTT_PORT = 1883

MQTT_TIMEOUT = 60
TOPICO_RESPOSTA="mensagens"

def on_message(client, userdata, msg):
	print("\nchegou")
	print(msg.topic+" "+str(msg.payload))
	print("\nchegou")

def on_subscribe(client, userdata, mid, granted_qos):
    print('Inscrito no tópico: %d' % mid)

def loop():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
  
    client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)
    client.loop_forever()

def send_message(topico,msg):
    client = mqtt.Client()
    
    client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)
    result, mid = client.publish(topico, msg)
    print('Mensagem enviada ao canal: %d' % mid)


for i in range(20):
    client = mqtt.Client()
    client.connect(MQTT_ADDRESS,1883,60)

    data = str.encode(str(input("\nDigite uma mensagem\n")))
    k = pyDes.triple_des(b"CHAVE001CHAVE002CHAVE003", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(data)

    mensagem_envida=d.hex()

    client.publish("mensagens", mensagem_envida);
    client.disconnect();
    time.sleep(10)
