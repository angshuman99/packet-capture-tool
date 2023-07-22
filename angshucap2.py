from scapy.all import *
from scapy.layers.tls.all import TLS
from tabulate import tabulate

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        if TCP in packet and TLS in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            flags = packet[TCP].flags
            tls_version = packet[TLS].version
            data = [protocol, src_ip, src_port, dst_ip, dst_port, flags, f"TLSv{tls_version}"]
            table.append(data)
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            data = [protocol, src_ip, src_port, dst_ip, dst_port, "N/A", "N/A"]
            table.append(data)

interface = input("Enter the interface to capture packets (e.g., eth0, wlan0): ")
table = []

try:
    print("Starting packet capture... Press Ctrl+C to stop.")
    sniff(iface=interface, prn=packet_handler, store=0)
    headers = ["Protocol", "Source IP", "Source Port", "Destination IP", "Destination Port", "TCP Flags", "TLS Version"]
    print(tabulate(table, headers=headers, tablefmt="grid"))
except KeyboardInterrupt:
    print("Packet capture stopped.")
