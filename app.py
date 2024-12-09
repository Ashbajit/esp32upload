from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.data  # Get raw binary data
    size = len(data) / (1024 * 1024)  # Convert size to MB
    return f"Received {size:.2f} MB of data.", 200
