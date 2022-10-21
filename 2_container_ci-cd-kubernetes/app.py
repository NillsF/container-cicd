from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This speaker room is actually kind of fun. Great people here!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
