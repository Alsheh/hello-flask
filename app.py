from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'OK', 200


@app.route('/hello', methods=['GET'])
def hello():
    return 'hello', 200


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
