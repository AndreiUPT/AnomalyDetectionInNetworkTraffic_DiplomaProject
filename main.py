from flask import Flask, render_template, request, jsonify
from ml.random_forest import RandomForest
import pickle

flask_application = Flask(__name__)

# Instantiate Random Forest
random_forest_instance = RandomForest()
random_forest_instance.training()

with open('random_forest_model.pkl', 'wb') as f:   # Saving the trained model into a pickle file
    pickle.dump(random_forest_instance, f)


@flask_application.route("/")
def index():
    # Render HTML template
    return render_template("index.html")


@flask_application.route("/predict", methods=["POST", "GET"])
def predict():
    source = request.form.get('Source')
    destination = request.form.get('Destination')
    protocol = request.form.get('Protocol')
    length = request.form.get('Length')

    # model = pickle.load(open("random_forest_model.pkl", "rb"))

    # Predictions:
    packet_info = {'Source': source, 'Destination': destination, 'Protocol': protocol, 'Length': length, }

    try:
        prediction = random_forest_instance.predict_packet_category(packet_info)

        return render_template("index.html", result=prediction)
    except ValueError as e:
        message = "Source, Destination or Protocol are not found. Please use the tool https://www.virustotal.com/gui/home/upload for in-depth IP investigation."
        return render_template("index.html", result=message)


@flask_application.route("/favicon.ico")  # Handling 404 error
def favicon():
    return "", 404


if __name__ == "__main__":
    flask_application.run(debug=True)
