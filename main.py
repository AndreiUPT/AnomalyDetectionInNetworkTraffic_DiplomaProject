from flask import Flask, render_template
from ml.random_forest import RandomForest
from realtime_router_capture import PacketsCapture
import threading

flask_application = Flask(__name__)

# Instantiate Random Forest
random_forest_instance = RandomForest();

@flask_application.route("/")
def index():
    # Call the training method to compute metrics
    accuracy, conf_matrix, class_report = random_forest_instance.training()

    # Render an HTML template
    return render_template("index.html", accuracy=accuracy,
                           conf_matrix=conf_matrix,
                           class_report=class_report)


if __name__ == "__main__":
    flask_application.run(debug=True)
