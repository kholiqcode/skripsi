from django.apps import AppConfig
from django.conf import settings

import os
import joblib


class SentimentConfig(AppConfig):
    name = 'sentiment'
    path = os.path.join(settings.MODELS, 'models.p')
    path_emosi = os.path.join(settings.MODELS, 'models_emotion.p')
    path_general = os.path.join(settings.MODELS, 'models_general.p')

    # separation of data packed in the model joblib
    with open(path, 'rb') as joblibFile:
        data = joblib.load(joblibFile)
    
    with open(path_emosi, 'rb') as joblibFile:
        data_emosi = joblib.load(joblibFile)

    with open(path_general, 'rb') as joblibFile:
        data_general = joblib.load(joblibFile)

    model = data['classifier']
    vectorizer = data['vectorizer']

    model_emosi = data_emosi['classifier']
    vectorizer_emosi = data_emosi['vectorizer']

    model_general = data_general['classifier']
    vectorizer_general = data_general['vectorizer']
