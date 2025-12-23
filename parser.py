from scapy.layers.inet import IP, TCP, UDP, ICMP

def parse_packet(packet):
    if IP not in packet:
        return None

    src = packet[IP].src
    dst = packet[IP].dst

    if ICMP in packet:
        return ("ICMP", src, dst, None)

    if UDP in packet:
        return ("UDP", src, dst, packet[UDP])

    if TCP in packet:
        return ("TCP", src, dst, packet[TCP])

    return None
