from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    # Get raw binary data
    data = request.get_data()
    size = len(data) / (1024 * 1024)  # Convert size to MB
    print(f"Received {len(data)} bytes ({size:.2f} MB).")
    return f"Received {size:.2f} MB of data.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
