from flask import Flask, jsonify, request
import paho.mqtt.publish as publish

app = Flask(__name__)

# Initialize a variable to store the JSON response
stored_response = {}

# MQTT broker details
mqtt_broker_host = "192.168.68.120"
mqtt_broker_port = 1883

# Function to send MQTT notification
def send_mqtt_notification(topic, message):
    publish.single(topic, message, hostname=mqtt_broker_host, port=mqtt_broker_port, retain=True)

# API to set a JSON response
@app.route('/setUserProfile', methods=['POST'])
def set_response():
    global stored_response
    data = request.get_json()
    stored_response = data
    # Send MQTT notification
    send_mqtt_notification("topic/input", "personal data updated")
    return jsonify({"message": "Response set successfully"})

# API to get the stored JSON response
@app.route('/userProfile', methods=['GET'])
def get_response():
    return jsonify(stored_response)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.68.120', port=5000)
