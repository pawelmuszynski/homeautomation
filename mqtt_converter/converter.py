#!/usr/bin/python3

import socket
import paho.mqtt.client as mqtt
import pyjq
import json

MQTT_HOST = "10.1.1.10"
SUB_TOPIC = "rtl_433/" + socket.gethostname() + "/events"
PUB_TOPIC = "domoticz/in"
LIGHT_JQ_FILTER = "{\"idx\": 25} + {\"Battery\": (.\"battery_ok\" * 100)} + {\"svalue\": .\"light_lux\" | tostring}"
UV_JQ_FILTER = "{\"idx\": 35} + {\"Battery\": (.\"battery_ok\" * 100)} + {\"svalue\": (.\"uvi\" | tostring + \";0\")}"
UV_test_JQ_FILTER = "{\"idx\": 36} + {\"Battery\": (.\"battery_ok\" * 100)} + {\"svalue\": (.\"uv\" | tostring + \";0\")}"

def windDirection(wb):
  if 0 <= wb < 11.5:
    return "N"
  if 11.5 <= wb < 33.75:
    return "NNE"
  if 33.75 <= wb < 56.25:
    return "NE"
  if 56.25 <= wb < 78.75:
    return "ENE"
  if 78.75 <= wb < 101.25:
    return "E"
  if 101.25 <= wb < 123.75:
    return "ESE"
  if 123.75 <= wb < 146.25:
    return "SE"
  if 146.25 <= wb < 168.75:
    return "SSE"
  if 168.75 <= wb < 191.25:
    return "S"
  if 191.25 <= wb < 213.75:
    return "SSW"
  if 213.75 <= wb < 236.25:
    return "SW"
  if 236.25 <= wb < 258.75:
    return "WSW"
  if 258.75 <= wb < 281.25:
    return "W"
  if 281.25 <= wb < 303.75:
    return "WNW"
  if 303.75 <= wb < 326.25:
    return "NW"
  if 326.25 <= wb < 348.75:
    return "NNW"
  if 348.75 <= wb < 360:
    return "N"
  return "ERROR"

def windDomoticz(tin):
  idx = 32
  wb = str(tin['wind_dir_deg'])
  wd = windDirection(tin['wind_dir_deg'])
  ws = str(round(10 * tin['wind_avg_m_s'], 1))
  wg = str(round(10 * tin['wind_max_m_s'], 1))
  t  = "0"
  tc = "0"
  tout = {}
  tout['idx'] = idx
  tout['svalue'] = wb + ";" + wd + ";" + ws + ";" + wg + ";" + t + ";" + tc
  tout['Battery'] = 100 * tin['battery_ok']
  return json.dumps(tout)


def on_connect(client, userdata, flags, rc):
  print("Connected to broker " + MQTT_HOST + " with result code " + str(rc))
  client.subscribe(SUB_TOPIC)
  print("Subscribe topic: " + SUB_TOPIC)

def on_message(client, userdata, msg):
  received_json = json.loads(msg.payload.decode('utf-8'))
  published_json = pyjq.one(LIGHT_JQ_FILTER, received_json)
  client.publish(PUB_TOPIC, json.dumps(published_json))
  #print(json.dumps(published_json))
  client.publish(PUB_TOPIC, windDomoticz(received_json))
  #print(windDomoticz(received_json))
  published_json = pyjq.one(UV_JQ_FILTER, received_json)
  client.publish(PUB_TOPIC, json.dumps(published_json))
  #print(json.dumps(published_json))
  published_json = pyjq.one(UV_test_JQ_FILTER, received_json)
  client.publish(PUB_TOPIC, json.dumps(published_json))
  #print(json.dumps(published_json)

client = mqtt.Client()
client.connect(MQTT_HOST)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
