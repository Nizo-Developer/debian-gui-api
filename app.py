from flask import Flask, Blueprint
from flask_cors import CORS
from api.browse_routes import browseBp


app = Flask(__name__)
CORS(app)

app.register_blueprint(browseBp, url_prefix="/api")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
