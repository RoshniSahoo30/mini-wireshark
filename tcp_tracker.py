tcp_states = {}

def track_tcp(src, dst, tcp):
    key = (src, tcp.sport, dst, tcp.dport)
    flags = tcp.flags

    if flags == "S":
        tcp_states[key] = "SYN"
        return "SYN"

    if flags == "SA":
        tcp_states[key] = "SYN-ACK"
        return "SYN-ACK"

    if flags == "A" and key in tcp_states:
        tcp_states[key] = "ESTABLISHED"
        return "ESTABLISHED"

    return None
