# Mini-wireshark
# Mini Wireshark – Network Packet Sniffer

A lightweight, system-level network packet sniffer inspired by Wireshark. This tool captures live traffic, parses core protocols, and tracks TCP connection states (like the three-way handshake) in real-time.

Built to demonstrate deep-dives into **TCP/IP stacks**, **OS kernel-user space interaction**, and **stateful packet inspection**.

---

## Features

* **Live Capture:** Real-time sniffing from active network interfaces.
* **Protocol Support:** Deep parsing for **TCP**, **UDP**, and **ICMP**.
* **TCP Handshake Tracking:** Detects `SYN`, `SYN-ACK`, and `ESTABLISHED` sequences.
* **Stateful Monitoring:** Tracks the lifecycle of TCP connections.
* **Clean CLI:** Readable, color-coded terminal output for easy debugging.

---

## Tech Stack

* **Language:** Python 3.9+
* **Library:** [Scapy](https://scapy.net/) (Packet manipulation)
* **OS:** macOS / Linux (Requires root/sudo)
* **Model:** User-space packet sniffing

---

## Getting Started

### Prerequisites
* Python 3.9 or later
* `pip` (Python package manager)
* Administrator/root access (required for raw socket access)

### Installation
1. **Clone the repo**
   ```bash
   git clone [https://github.com/RoshniSahoo30/mini-wireshark.git](https://github.com/RoshniSahoo30/mini-wireshark.git)
   cd mini-wireshark
   ```
2. **Install Scapy**
   ```bash
   pip install scapy
   ```
   **Running the App**
    Since sniffing requires raw socket access, you must run the script with sudo:
      ```bash
      sudo python3 main.py
      ```
      To stop sniffing, press Ctrl + C.

### Sample Output
  ```bash
    [TCP ] 192.168.0.105:60682 → 142.250.182.69:443 | SYN
    [TCP ] 142.250.182.69:443 → 192.168.0.105:60682 | SYN-ACK
    [TCP ] 192.168.0.105:60682 → 142.250.182.69:443 | ESTABLISHED
    [ICMP] 192.168.0.105       → 8.8.8.8
    [UDP ] 192.168.0.105:5353  → 224.0.0.251:5353
 ```
---
### Project Structure
  ```bash
    mini-wireshark/
    ├── main.py          # Entry point
    ├── sniffer.py       # Live capture logic
    ├── parser.py        # Protocol decoding (TCP/UDP/ICMP)
    ├── tcp_tracker.py   # Connection state management
    └── README.md
 ```
---
### Concepts 
* **Networking**
  * TCP/IP Stack: Layer 3 (IP) and Layer 4 (TCP/UDP) analysis.
  * Handshake Mechanics: Understanding the sequence of flags.
  * ICMP: Monitoring echo requests/replies (pings).

* **Operating Systems**
  * User-Space vs. Kernel: How Scapy interacts with the network stack.
  * Privileged Ops: Why raw sockets require elevated permissions.

---
### System Architecture
```bash
┌────────────┐
│  main.py   │  → Application entry point
└─────┬──────┘
      ↓
┌────────────┐
│ sniffer.py │  → Captures packets from the network interface
└─────┬──────┘
      ↓
┌────────────┐
│ parser.py  │  → Parses packets & identifies protocols
└─────┬──────┘
      ↓
┌──────────────┐
│ tcp_tracker  │  → Tracks TCP connection states (handshake)
└──────────────┘
```
