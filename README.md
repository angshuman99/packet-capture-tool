# AngshuCap

AngshuCap is a packet capture tool that allows you to monitor network traffic and analyze packets on your system. It is built using Python and the Scapy library, offering flexibility and ease of use.

## Features

- Capture packets on a specified network interface.
- Display packet information, including source and destination IPs, ports, protocols, TCP flags, and TLS versions.
- Support for both UDP and TCP protocols.
- Easily customizable to suit specific packet capturing needs.

## Requirements

- Python 3.x
- Scapy library

## Usage

1. Clone the repository:

```bash
git clone https://github.com/<your_username>/angshucap.git
cd angshucap

pip install scapy

sudo python angshucap.py

1. Enter the interface name when prompted (e.g., eth0, wlan0).
2. Start capturing packets. Press Ctrl+C to stop the capture.

Example Output
+------------+-----------------+---------------+------------------+--------------------+-------------+---------------+
|   Protocol | Source IP       |   Source Port | Destination IP   |   Destination Port | TCP Flags   | TLS Version   |
+============+=================+===============+==================+====================+=============+===============+
|         17 | 172.16.103.129  |         50014 | 172.16.103.2     |                 53 | N/A         | N/A           |
+------------+-----------------+---------------+------------------+--------------------+-------------+---------------+
|         17 | 172.16.103.129  |         50014 | 172.16.103.2     |                 53 | N/A         | N/A           |
+------------+-----------------+---------------+------------------+--------------------+-------------+---------------+
...


Contribution

Contributions to AngshuCap are welcome! Feel free to open issues, suggest improvements, or submit pull requests.

License

This project is licensed under the MIT License.

Replace `<your_username>` with your actual GitHub username, and feel free to modify the content as needed. This README provides an overview of the tool, its features, how to use it, and the license information. Add more details if necessary or include information about how to set up and run the tool on different systems.
