from flask import Flask, jsonify

app = Flask(__name__)
votes = {}
voter_list = [
    "Praveen", "Ravi", "Suresh", "Naresh", "Kiran", "Vamsi",  # unique
    "Praveen", "Ravi", "Praveen", "Kiran"
]
def process_votes():
    for name in voter_list:
        votes[name] = votes.get(name, 0) + 1

process_votes()

# @app.route("/")
# def home():

#     return "Welcome to the App"
@app.route("/health")
def health():
    return "App is running"

@app.route("/")
def home():
    return "Voting App Running"

@app.route("/results")
def results():
    return jsonify(votes)

#version-2
@app.route("/reset")
def reset():
    votes.clear()
    return jsonify({"message": "All votes have been reset"})

if __name__ == "__main__":

    app.run(debug=True)