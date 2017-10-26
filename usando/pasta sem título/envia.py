# -*- coding: utf-8 -*-
__author__ = ''
import pyDes
import sys
import time
import paho.mqtt.client as mqtt
from collections import namedtuple

Auth = namedtuple('Auth', ['user', 'pwd'])
MQTT_ADDRESS = '127.0.0.1'
#MQTT_ADDRESS = '127.0.0.1'
# descomente esta linha para usar o servidor da Fundação Eclipse.
#MQTT_ADDRESS = 'iot.eclipse.org'
MQTT_PORT = 1883
# descomente esta linha caso seu servidor possua autenticação.
# MQTT_AUTH = Auth('login', 'senha')
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
    # descomente esta linha caso seu servidor possua autenticação.
    # client.username_pw_set(MQTT_AUTH.user, MQTT_AUTH.pwd)
    client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)
    client.loop_forever()


def send_message(topico,msg):
    client = mqtt.Client()
    # descomente esta linha caso seu servidor possua autenticação.
    # client.username_pw_set(MQTT_AUTH.user, MQTT_AUTH.pwd)
    client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)
    result, mid = client.publish(topico, msg)
    print('Mensagem enviada ao canal: %d' % mid)










# This is the Publisher
for i in range(20):
    client = mqtt.Client()
    client.connect(MQTT_ADDRESS,1883,60)

    data = str.encode("Hello world!")
    k = pyDes.triple_des(b"CHAVE001CHAVE002CHAVE003", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(data)

    print ("\nDecrypted: %r" % k.decrypt(d))


    #d pra str tes
    tes="".join(map(chr, d))

    #tes pra byte final
    final = str.encode(tes)

    client.publish("mensagens", data);
    client.disconnect();
    time.sleep(10)




#  resposta da funcao       bytes.fromhex('').join(result)


   


#    print ("Decrypted: %r" % k.decrypt(final))   
'''
    #d pra str tes
    tes="".join(map(chr, d))
    #tes pra byte final
    final=tes.encode('utf-16')

    client.publish("mensagens", tes);
    client.disconnect();
    time.sleep(10)
'''

    

     
 #   print(data)
#    print("\ndecodificado\n")
  #  print(data.decode('utf-8'))


'''


client2 = mqtt.Client()
client2.connect(MQTT_ADDRESS,1883,60)

client2.on_connect = on_connect
client2.on_message = on_message
    
client2.loop_forever()




# For Python3, you'll need to use bytes, i.e.:
s=input("digite um texto para criptografar\n")
data = str.encode(s)
k = pyDes.triple_des(b"CHAVE001CHAVE002CHAVE003", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

d = k.encrypt(data)
print ("Encrypted: %r" % d)
print ("Decrypted: %r" % k.decrypt(d))
assert k.decrypt(d) == data
        	


mqtt_envia("mensagens",d)

loop()'''















