from flask import Flask

flask_application = Flask(__name__)

if __name__ == "__main__":
    flask_application.run(debug=True)

