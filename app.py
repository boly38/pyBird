# bootstrap : https://github.com/docker/python-docker
from flask import Flask, request, jsonify
from PredictService import PredictService

app = Flask(__name__)
svc = PredictService()

@app.route('/')
def health():
    return 'My health is ok, thank you so much !'

@app.route('/bioclip/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'URL manquante'}), 400

    url = data['url']
    predictions = svc.predict(url)
    json_result = jsonify(predictions)
    print(json_result)
    return json_result

