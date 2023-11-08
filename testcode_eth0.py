import RPi.GPIO as GPIO
import time

# W5500 Reset Pin
W5500_RST_PIN = 20

# Initialize the W5500 Ethernet
GPIO.setmode(GPIO.BCM)
GPIO.setup(W5500_RST_PIN, GPIO.OUT)

GPIO.output(W5500_RST_PIN, GPIO.LOW)
time.sleep(1)
GPIO.output(W5500_RST_PIN, GPIO.HIGH)
time.sleep(1)

# Wait for an Ethernet cable to be connected
while True:
    try:
        with open("/sys/class/net/eth0/carrier", "r") as carrier_file:
            carrier_status = carrier_file.read().strip()
            if carrier_status == "1":
                print("Ethernet cable connected. Internet is available.")
                break
            else:
                print("Waiting for Ethernet cable to be connected...")
    except FileNotFoundError:
        print("Ethernet interface not found. Make sure it's configured as 'eth0'.")

    time.sleep(2)

# At this point, the internet connection is available, and you can proceed with network operations as needed.
