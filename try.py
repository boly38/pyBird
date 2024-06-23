from PredictService import PredictService
import json

svc = PredictService()
predictions = svc.predict("https://images.pexels.com/photos/326900/pexels-photo-326900.jpeg?cs=srgb&dl=pexels-pixabay-326900.jpg&fm=jpg")
print(json.dumps(predictions, indent=4))