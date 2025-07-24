from scapy.all import *
import csv

def pcap_to_csv(pcap_file, csv_file):
    packets = rdpcap(pcap_file)

    with open(csv_file, mode='w', newline='') as f:
        writer = csv.writer(f)

        # Header
        writer.writerow([
            "No", "Timestamp", "Source IP", "Destination IP",
            "Source Port", "Destination Port", "Protocol", "Packet Length"
        ])

        for i, pkt in enumerate(packets):
            # Initialize fields
            src_ip = dst_ip = src_port = dst_port = proto = ""

            # Extract IP layer
            if IP in pkt:
                src_ip = pkt[IP].src
                dst_ip = pkt[IP].dst
                proto = pkt[IP].proto

                # Extract TCP/UDP ports
                if TCP in pkt:
                    src_port = pkt[TCP].sport
                    dst_port = pkt[TCP].dport
                    proto = "TCP"
                elif UDP in pkt:
                    src_port = pkt[UDP].sport
                    dst_port = pkt[UDP].dport
                    proto = "UDP"
                else:
                    proto = str(proto)

            # Write row
            writer.writerow([
                i + 1,
                pkt.time,
                src_ip,
                dst_ip,
                src_port,
                dst_port,
                proto,
                len(pkt)
            ])

    print(f"[+] Conversion complete: {csv_file}")

# Example usage:
pcap_to_csv("logs_generated.pcap", "logs_converted.csv")
