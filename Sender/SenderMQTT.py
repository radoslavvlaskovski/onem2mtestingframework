import paho.mqtt.client as mqtt

class SenderMQTT:

    def __init__(self, url, port):

        self.url = url
        self.port = port

        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect()
        self.client.on_message = self.on_message

        self.connect(url, port)

    def on_connect(self,client):

        print("Connected with result code: ")

    def on_disconnect(self):
        print("\nFAILED\n")


    def on_message(self):

        return

    def connect(self,url,port1):

        self.client.connect("iot.eclipse.org",1883)

    def send_request(self, subscription, request):

        self.client.publish(subscription,request)