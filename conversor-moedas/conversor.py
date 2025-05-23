from flask import Flask
import utils

app = Flask(__name__)
utils.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)