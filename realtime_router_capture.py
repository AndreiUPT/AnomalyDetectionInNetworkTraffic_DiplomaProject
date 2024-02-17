############ The purpose of this file is real-time packets capturing from the router #####################

import pyshark
import csv

# the interface for Wi-Fi capture
wifi_interface = "en0"

# packets saved in a .pcap file (Live capture)
capture = pyshark.LiveCapture(interface=wifi_interface, output_file="captured_packets.pcap")

# create a loop for packets capturing
end_capture = False  # boolean variable for ending the live capture
for i, packet in enumerate(capture.sniff_continuously()):
    if end_capture:
        break