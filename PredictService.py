import tempfile
import requests
from bioclip import TreeOfLifeClassifier, Rank


class PredictService:

    def __init__(self):
        self.classifier = TreeOfLifeClassifier()

    def download_image(self, url):
        response = requests.get(url)

        # Vérifier si la requête a réussi
        if response.status_code == 200:
            # Créer un fichier temporaire
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')

            # Écrire le contenu de l'image dans le fichier temporaire
            temp_file.write(response.content)
            temp_file.close()

            # Retourner le chemin du fichier temporaire
            return temp_file.name
        else:
            raise Exception("Error while downloading image. Status: {}".format(response.status_code))

    def predict(self, image_url=None):
        if image_url is None:
            raise Exception("expect image url")
        image_path = self.download_image(image_url)
        predictions = self.classifier.predict(image_path, Rank.SPECIES)
        for prediction in predictions:
            if 'file_name' in prediction:
                del prediction['file_name']
        return predictions
