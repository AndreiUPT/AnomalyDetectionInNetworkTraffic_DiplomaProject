from flask import Flask, render_template
from ml.random_forest import RandomForest

flask_application = Flask(__name__)

# Instantiate Random Forest
random_forest_instance = RandomForest();

@flask_application.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    flask_application.run(debug=True)
