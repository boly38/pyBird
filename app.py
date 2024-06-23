# bootstrap : https://github.com/docker/python-docker
from flask import Flask, request, jsonify
from PredictService import PredictService
import os

app = Flask(__name__)
svc = PredictService()

# Retrieve the expected private key from environment variable
# when missing, the app is free to use without security
EXPECTED_PRIVATE_KEY = os.getenv('PYBIRD_PRIVATE_KEY')


def require_private_key(func):
    """
    Decorator to check for the presence and validity of the 'PRIVATE-KEY' header.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapped function if the 'PRIVATE-KEY' is valid; otherwise, a 403 response.
    """
    def wrapper(*args, **kwargs):
        private_key = request.headers.get('PRIVATE-KEY')
        if private_key and private_key != EXPECTED_PRIVATE_KEY:
            return jsonify({'error': 'Forbidden: Missing or incorrect private key'}), 403
        return func(*args, **kwargs)
    return wrapper

@app.route('/')
def health():
    return 'My health is ok, thank you so much !'


@app.route('/bioclip/predict', methods=['POST'])
@require_private_key
def predict():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'URL manquante'}), 400

    url = data['url']
    predictions = svc.predict(url)
    json_result = jsonify(predictions)
    print(json_result)
    return json_result

