from flask import Flask, request
from pymessenger.bot import Bot

app = Flask("App")

VERIFY_TOKEN = "0123456789"
ACCESS_TOKEN = "EAAHFEVSax4IBANQOfdDSAuJ6AUErJ0LIllLJ4KB6Qe2wotZA8MFZAURznqCkUWz4HiRhYWMZA43tRw8CAoHMiHbxIFRDHZBYgJtxtxyCtKZBRPF44YJD6A4qa9uaHUr94vrbL2CXhPAx77hahbVvKGOWI7ZASKcZByZB5GgQW8dxsbXr1tx711p9b0r2IzNVZC3EZD"

pybot = Bot(ACCESS_TOKEN)

@app.route("/", methods=["GET"])
def home():
    return "Working..."

@app.route("/check/", methods=["GET"])
def sayhi():
    print("Got a ping request!")
    return "Working..."

@app.route("/callback/", methods=["GET"])
def get_callback():
    if VERIFY_TOKEN == request.args.get("hub.verify_token"):
        return request.args.get("hub.challenge")
    else:
        return "Not working."

@app.route("/callback/", methods=["POST"])
def post_callback():
    output = request.get_json()

    for entry in output.get("entry"):
        if "messaging" in entry:
            for messaging in entry.get("messaging"):
                sender = messaging.get("sender").get("id")
                recipient = messaging.get("recipient").get("id")

                text = "You sent an attachment"

                if "text" in messaging.get("message"):
                    text = messaging.get("message").get("text")

                print(sender, recipient, text)

                pybot.send_text_message(sender, text)

    return "Done!"

app.run()