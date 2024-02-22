############ The purpose of this file is real-time packets capturing from the router #####################

import pyshark
import csv

class PacketsCapture:

    def __init__(self, wifi_interface, output_file, csv_file, capture, end_capture):
        self.interface = wifi_interface
        self.output_file = output_file
        self.csv_file = csv_file
        self.capture = None
        self.end_capture = False


    def start_capture(self):     # method for packets capturing
        # packets saved in a .pcap file (Live capture)
        self.capture = pyshark.LiveCapture(interface=self.interface, output_file=self.output_file)

    def stop_capture(self):     # method to stop the capture
        # boolean variable for ending the live capture
        self.end_capture = True  # stop -> end_capture's value True

    def create_csv(self):        # method to created a csv file in which the capture will be stored
        # creating a csv file for writing
        self.csv_file = "captured_packets.csv"

        with open(self.csv_file, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['No.', 'Time', 'Source', 'Destination', 'Protocol', 'Length'])  # the first row will be populated with columns headers

        # create a loop for packets capturing
        for i, packet in enumerate(self.capture.sniff_continuously()):
            if self.end_capture:
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

    def close_capture(self):      # method to stop the capture
        self.capture.close()