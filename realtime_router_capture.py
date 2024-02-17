############ The purpose of this file is real-time packets capturing from the router #####################

import pyshark
import csv

# the interface for Wi-Fi capture
wifi_interface = "en0"

# packets saved in a .pcap file (Live capture)
capture = pyshark.LiveCapture(interface=wifi_interface, output_file="captured_packets.pcap")
