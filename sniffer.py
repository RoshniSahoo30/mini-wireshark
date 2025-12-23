from scapy.all import sniff

def start_sniffing(handler):
    sniff(prn=handler, store=False)
