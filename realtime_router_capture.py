############ The purpose of this file is real-time packets capturing from the router #####################

import pyshark
import csv

# the interface for Wi-Fi capture
wifi_interface = "en0"

# packets saved in a .pcap file (Live capture)
capture = pyshark.LiveCapture(interface=wifi_interface, output_file="captured_packets.pcap")

# boolean variable for ending the live capture
end_capture = False

# creating a csv file for writing
csv_file = "captured_packets.csv"

with open(csv_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['No.', 'Time', 'Source', 'Destination', 'Protocol', 'Length'])  # the first row will be populated with columns headers

    # create a loop for packets capturing
    for i, packet in enumerate(capture.sniff_continuously()):
        if end_capture:
            break
        try:
            # extracting the relevant info from the packet
            time = packet.sniff_time.strftime('%Y-%m-%d %H:%M:%S')
            source = packet.ip.src
            destination = packet.ip.dst
            protocol = packet.transport_layer
            length = packet.length
            csvwriter.writerow([i + 1, time, source, destination, protocol, length])  # write packet details into the csv file starting with the second row
        except AttributeError:
            pass  # skip if the packet's information is not relevant

        print(packet)

capture.close()