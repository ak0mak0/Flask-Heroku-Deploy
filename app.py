from flask import Flask, jsonify

app = Flask("__name__")

@app.route("/ping")
def ping():
    return "lol"

if __name__ == "__main__":
    app.run(debug=True, port=4000)