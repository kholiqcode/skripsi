from django.apps import AppConfig
from django.conf import settings

import os
import pickle


class SentimentConfig(AppConfig):
    name = 'sentiment'
    path = os.path.join(settings.MODELS, 'models.p')
    path_emosi = os.path.join(settings.MODELS, 'models_emotion.p')
    path_general = os.path.join(settings.MODELS, 'models_general.p')

    # separation of data packed in the model pickle

    with open(path, 'rb') as pickledFile:
        data = pickle.load(pickledFile)
    
    with open(path_emosi, 'rb') as pickledFile:
        data_emosi = pickle.load(pickledFile)

    with open(path_general, 'rb') as pickledFile:
        data_general = pickle.load(pickledFile)

    model = data['classifier']
    vectorizer = data['vectorizer']

    model_emosi = data_emosi['classifier']
    vectorizer_emosi = data_emosi['vectorizer']

    model_general = data_general['classifier']
    vectorizer_general = data_general['vectorizer']
