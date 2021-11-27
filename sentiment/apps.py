from django.apps import AppConfig
from django.conf import settings

import os
import pickle


class SentimentConfig(AppConfig):
    name = 'sentiment'
    path = os.path.join(settings.MODELS, 'models.p')

    # separation of data packed in the model pickle

    with open(path, 'rb') as pickledFile:
        data = pickle.load(pickledFile)

    model = data['classifier']
    vectorizer = data['vectorizer']
