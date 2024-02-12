## Requirements

```bash
python -m pip install --user paho-mqtt
# python -m pip install --user hbmqtt
# python -m pip install --upgrade --user websockets
brew install mosquitto
# python -m pip install  --user keyboard
# python -m pip install  --user pynput
python -m pip  install  --user flask  
python -m pip  install  --user jsonify 
```

## Usage

## Run the MQTT broker
```bash
mosquitto -c ./mosquitto.conf
```

## Run the HTTP Server
```bash
python ./http-server.py
```

## Make Mosquitto broker run on Inet4 IP 
Change configuration,
```
# /opt/homebrew/etc/mosquitto/mosquitto.conf or ./mosquitto.conf
listener 1883 192.168.68.127
allow_anonymous true
```

## Run the MQTT client

```bash
python ./mqtt_client.py
```
