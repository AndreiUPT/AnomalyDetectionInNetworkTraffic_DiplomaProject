from flask import Flask, render_template, request, jsonify
from ml.random_forest import RandomForest

flask_application = Flask(__name__)

# Instantiate Random Forest
random_forest_instance = RandomForest()

@flask_application.route("/")
def index():
    # Render an HTML template
    return render_template("index.html")

@flask_application.route("/predict", methods=["POST"])
def predict():
    # Get the data submitted by user
    source = request.form.get("source")
    destination = request.form.get("destination")
    protocol = request.form.get("protocol")
    length = request.form.get("length")

    # Put the packet info in a dictionary
    packet_data = {
        "Source": source,
        "Destination": destination,
        "Protocol": protocol,
        "Length": length
    }

    prediction = random_forest_instance.predict(packet_data)
    return jsonify(prediction=prediction)


if __name__ == "__main__":
    flask_application.run(debug=True)
