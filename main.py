from flask import Flask,render_template

flask_application = Flask(__name__)

@flask_application.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    flask_application.run(debug=True)

