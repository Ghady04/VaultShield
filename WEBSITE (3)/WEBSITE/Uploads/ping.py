from scapy.all import *

# Define the target IP address
ip = IP(dst="192.168.1.1")  # Google's public DNS server

# Create an ICMP packet
icmp = ICMP()

# Stack the layers (IP/ICMP)
pkt = ip/icmp

# Send the packet and wait for the first response
reply = sr1(pkt, timeout=2)  # Timeout is 2 seconds

# Check if a reply was received
if reply:
    print("ICMP reply ........")
    print("Source IP: ", reply[IP].src)
    print("Destination IP:", reply[IP].dst)
else:
    print("No reply received!")
