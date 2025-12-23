from sniffer import start_sniffing
from parser import parse_packet
from tcp_tracker import track_tcp

def handler(packet):
    parsed = parse_packet(packet)
    if not parsed:
        return

    proto, src, dst, layer = parsed

    if proto == "ICMP":
        print(f"[ICMP] {src} → {dst}")

    elif proto == "UDP":
        print(f"[UDP ] {src}:{layer.sport} → {dst}:{layer.dport}")

    elif proto == "TCP":
        state = track_tcp(src, dst, layer)
        suffix = f" | {state}" if state else ""
        print(f"[TCP ] {src}:{layer.sport} → {dst}:{layer.dport}{suffix}")

if __name__ == "__main__":
    print("📡 Mini Wireshark started")
    start_sniffing(handler)
