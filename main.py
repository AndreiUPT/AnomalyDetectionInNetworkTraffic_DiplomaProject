from flask import Flask, render_template, request, jsonify
from sklearn.preprocessing import LabelEncoder

from ml.random_forest import RandomForest
import pickle
import pandas as pd

flask_application = Flask(__name__)

# Instantiate Random Forest
random_forest_instance = RandomForest()
random_forest_instance.training()

with open('random_forest_model.pkl', 'wb') as f:
    pickle.dump(random_forest_instance, f)

#Define label encoders
label_encoders = {}

# Method for preprocessing packet data
def preprocess_packet(packet_info):
    # Create a DataFrame from packet info
    packet_df = pd.DataFrame(packet_info, index=[0])

    # Label encoding for categorical columns
    for column, encoder in label_encoders.items():
        if column in packet_df.columns:
            packet_df[column] = encoder.transform(packet_df[column])

    return packet_df


@flask_application.route("/")
def index():
    # Render an HTML template
    return render_template("index.html")

@flask_application.route("/predict", methods=["POST"])
def predict():
 try:
    # Get packet data from the request
    packet_data = {
        "Source": request.form.get("source"),
        "Destination": request.form.get("destination"),
        "Protocol": request.form.get("protocol"),
        "Length": int(request.form.get("length"))
    }

    # Preprocess packet data
    packet_df = preprocess_packet(packet_data)

    # Predict packet category using the loaded model
    prediction = random_forest_instance.predict(packet_df)

    # Map prediction to labels
    if prediction[0] == 1:
        prediction_label = "Normal"
    else:
        prediction_label = "Anomaly"
    return jsonify(prediction=prediction)

 except Exception as e:
     return jsonify(error=str(e)), 500

@flask_application.route("/favicon.ico")
def favicon():
    return "", 404

if __name__ == "__main__":
    flask_application.run(debug=True)
