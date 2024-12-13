from flask import Flask, request, jsonify
from twilio.rest import Client
import json

app = Flask(__name__)

# Twilio credentials
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Load absentees from JSON file
def load_absentees():
    with open("absentees.json", "r") as file:
        return json.load(file)

# Notify absent students
@app.route("/notify", methods=["POST"])
def notify_absentees():
    absentees = load_absentees()

    for student in absentees:
        message = f"Hello {student['name']}, you were marked absent today."
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=student["phone"]
        )

    return jsonify({"status": "Notifications sent successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
