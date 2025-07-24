# CSV-to-Pcap-Log-convertor
Hello Gentlemen, I am give this tool for generation of pcap file that are saved in excel. Hopw it is helpful.
# 📦 PCAP to CSV Converter

This Python script converts a `.pcap` (Packet Capture) file into a structured `.csv` file, making it easier to analyze network traffic using spreadsheet tools or data processing libraries like `pandas`.

---

## 🧰 Features

- Extracts key network fields:
  - Packet number
  - Timestamp
  - Source and destination IP addresses
  - Source and destination ports
  - Protocol (TCP/UDP)
  - Packet size
- Handles any number of packets efficiently
- Gracefully skips non-IP packets
- Easy to modify for deeper protocol inspection (e.g., HTTP, DNS)

---

## 🔧 Requirements

- Python 3.6+
- [`scapy`](https://pypi.org/project/scapy/)

Install dependencies:

```bash
pip install scapy
