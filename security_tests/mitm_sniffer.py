from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("Raw"):
        data = packet["Raw"].load
        if b"Authorization" in data or b"password" in data:
            print(f"⚠️ Possible Credentials Leak: {data}")

sniff(filter="tcp port 80", prn=packet_callback, store=0)
