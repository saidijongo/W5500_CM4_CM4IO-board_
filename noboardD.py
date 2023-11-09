import board
import busio
import digitalio
import adafruit_wiznet5k.adafruit_wiznet5k_socket as socket
import adafruit_wiznet5k.adafruit_wiznet5k as wiznet
import time

# Define the SPI configuration for W5500 using GPIO pin assignments
SCK = board.D23  #  SCK pin (GPIO23)
MOSI = board.D19  #  MOSI pin (GPIO19)
MISO = board.D21  #  MISO pin (GPIO21)

spi_bus = busio.SPI(SCK, MOSI=MOSI, MISO=MISO)

# Define the CS and RST pins
cs = digitalio.DigitalInOut(board.D8)  # (GPIO8)
rst = digitalio.DigitalInOut(board.D7)  # (GPIO7)

# Initialize the W5500 Ethernet controller
ethernet = wiznet.WIZNET5K(spi_bus, cs, rst)

mac_address = (0xE4, 0x5F, 0x01, 0xEC, 0x28, 0xB4)
ip_address = "172.16.100.171"
subnet_mask = socket.parse_ipv4("255.255.255.0")
gateway_ip = socket.parse_ipv4("192.168.1.1")

# Initialize Ethernet with the provided configuration
ethernet.init()
ethernet.ifconfig(mac=mac_address, ip=ip_address, subnet=subnet_mask, gateway=gateway_ip)

while not ethernet.status.link:
    print("Waiting for Ethernet connection...")
    time.sleep(1)

print("Ethernet connection is established.")
