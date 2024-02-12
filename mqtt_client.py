import paho.mqtt.client as mqtt

# MQTT broker settings
broker_address = "192.168.68.120"  # Change this to your broker's address
broker_port = 1883  # Default MQTT port

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to a topic when connected
    client.subscribe("topic/input")

# Callback when the client receives a message from the server
def on_message(client, userdata, msg):
    print("Received message: " + msg.payload.decode())

# Initialize MQTT client
client = mqtt.Client()

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(broker_address, broker_port, 60)

# Loop to process MQTT messages
client.loop_start()

# Loop for command-line input
while True:
    user_input = input("Press 's' to send a message: ")
    if user_input.lower() == 's':
        # Publish message to MQTT topic
        client.publish("topic/input", "Message from server: Hello, world!")
        print("Message sent!")
    elif user_input.lower() == 'q':
        # Quit loop if 'q' is pressed
        break

# Disconnect MQTT client
client.loop_stop()
client.disconnect()
