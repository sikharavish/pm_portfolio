from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(message="✅ Flask is up and running!", status="OK")

if __name__ == "__main__":
    app.run(debug=True)