from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Raiku Fast Tap Game!</h1><p>This is a demo showing Raiku’ s speed.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)