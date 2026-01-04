from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
messages = []

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/send", methods=["POST"])
def send_message():
    user = request.form["username"]
    message = request.form["message"]
    time = datetime.now().strftime("%H:%M")

    messages.append({
        "user": user,
        "message": message,
        "time": time
    })

    return jsonify(messages)

@app.route("/messages")
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(debug=True)

