from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify
from datetime import datetime

app = Flask(__name__)
app.secret_key = "tural123"

# Store messages in memory (for demo purposes)
messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        if username:
            session["username"] = username
            return redirect(url_for("chat"))
    return render_template("index2.html")

@app.route("/chat")
def chat():
    if "username" not in session:
        return redirect(url_for("index2"))
    return render_template("chat.html", username=session["username"])

@app.route("/send", methods=["POST"])
def send():
    msg = request.form.get("message")
    user = session.get("username")
    if msg and user:
        messages.append({"user": user, "text": msg, "time": datetime.now().strftime("%H:%M:%S")})
    return ("", 204)

@app.route("/get_messages")
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(debug=True)
