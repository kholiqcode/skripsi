import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
import pandas as pd

from sentiment import clean_text
from sentiment.apps import SentimentConfig
from sentiment.grab import Grab
# Create your views here.
class call_model(APIView):

     def get(Self, request):
          if request.method == "GET":
               username = request.GET.get("username")  # get text from the parameter
               jumlah = request.GET.get("jumlah")  # get text from the parameter
               
               tweetList = Grab.getTweetByUsername(username,jumlah)
               #Cleaning the received text
               process = clean_text.TextPreprocess()
               cleanedText = [process.normalizer(tweet['text']) for tweet in tweetList]

               # vectorizing the given text
               vector_text = SentimentConfig.vectorizer.transform(cleanedText)

               # Predict sentiment based on vector
               _predicted_data = SentimentConfig.model.predict(vector_text)
               
               for index, w in enumerate(_predicted_data):
                   tweetList[index]['sentiment'] = w
            #    prediction = _predicted_data

               # build json response
               response = {'result': json.dumps(tweetList, indent=4, sort_keys=True, default=str)}

               return JsonResponse(response)