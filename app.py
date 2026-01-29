from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    version = os.environ.get("APP_VERSION", "v1")  # GitHub Action se env variable bhi bhej sakte ho
    return f"Flask app deployed via GitHub Actions, version: {version}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
