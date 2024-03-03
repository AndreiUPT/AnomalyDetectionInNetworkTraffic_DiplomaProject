from flask import Flask, render_template
from ml.random_forest import RandomForest
from realtime_router_capture import PacketsCapture
import threading

flask_application = Flask(__name__)

# Instantiate Random Forest
random_forest_instance = RandomForest()

# Instantiate capturing
'''
wifi_interface = "en0"
output_file = "captured_packets.pcap"
csv_file = "captured_packets.csv"
'''
capture_instance = PacketsCapture()

# thread creation for packets capturing
packetsCapturing_thread =  threading.Thread(target=capture_instance.capture_packets)

@flask_application.route("/")
def index():
    # Call the training method to compute metrics
    accuracy, conf_matrix, class_report = random_forest_instance.training()

    # start the packets capturing thread if not already running
    if not packetsCapturing_thread.is_alive():
        packetsCapturing_thread.start()

    # Render an HTML template
    return render_template("index.html", accuracy=accuracy,
                           conf_matrix=conf_matrix,
                           class_report=class_report)


if __name__ == "__main__":
    flask_application.run(debug=True)
