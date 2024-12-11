from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app) # allow all origin
# CORS(app, resources={r"/api/*": {"origins": ["http://127.0.0.1:5500", "http://another.com"]}})


# GET Method
@app.route('/api/greet', methods=['GET'])
def greet_get():
    name = request.args.get('name', 'World')  # Get the 'name' parameter from the URL
    return jsonify({'message': f"Hello, {name}!"})


# # POST Method
# @app.route('/api/greet', methods=['POST'])
# def greet_post():
#     data = request.get_json()  # Parse JSON payload from the request
#     name = data.get('name', 'World')  # Get 'name' from the payload
#     return jsonify({'message': f"Hello, {name}!"})

app.run()