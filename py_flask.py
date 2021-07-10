from flask import Flask, request
import random

data = {
    "life": [
             "Life is a joke",
             "It's good sometimes"
    ],
    "love": [
             "It's meaningless",
             "The word 'Love' is used so casually"
    ]
}

app = Flask("App")

@app.route("/")
def hello():
    if request.args.get("topic"):
        li = data.get(request.args.get("topic"))
        if li:
            return random.choice(li)
        else:
            return "Choose topic from : " + ", ".join(list(data.keys())) 
    else:
        return "Please provide a topic in query"

app.run()