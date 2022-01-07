import json
from json.encoder import JSONEncoder
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import pandas as pd

from sentiment import clean_text
from sentiment.apps import SentimentConfig
from sentiment.grab import Grab
# Create your views here.

def dashboard(request):
     konteks = {
          'title' : 'Judul'
     }
     return render(request, 'dashboard.html', konteks)

def profils(request):
     konteks = {
          'title' : 'Profil'
     }
     return render(request, 'profils.html', konteks)

@api_view(['GET'])
def cyberbullying(request):
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

          return JsonResponse(tweetList,safe=False)

@api_view(['GET'])
def emotion(request):
     if request.method == "GET":
          username = request.GET.get("username")  # get text from the parameter
          jumlah = request.GET.get("jumlah")  # get text from the parameter

          tweetList = Grab.getTweetByUsername(username,jumlah)
          #Cleaning the received text
          process = clean_text.TextPreprocess()
          cleanedText = [process.normalizer(tweet['text']) for tweet in tweetList]

          # vectorizing the given text
          vector_text = SentimentConfig.vectorizer_emosi.transform(cleanedText)
          
          # Predict sentiment based on vector
          _predicted_data = SentimentConfig.model_emosi.predict(vector_text)
          
          for index, w in enumerate(_predicted_data):
               tweetList[index]['sentiment'] = w

          return JsonResponse(tweetList,safe=False)

@api_view(['GET'])
def general(request):
     if request.method == "GET":
          username = request.GET.get("username")  # get text from the parameter
          jumlah = request.GET.get("jumlah")  # get text from the parameter

          tweetList = Grab.getTweetByUsername(username,jumlah)
          #Cleaning the received text
          process = clean_text.TextPreprocess()
          cleanedText = [process.normalizer(tweet['text']) for tweet in tweetList]

          # vectorizing the given text
          vector_text = SentimentConfig.vectorizer_general.transform(cleanedText)
          
          # Predict sentiment based on vector
          _predicted_data = SentimentConfig.model_general.predict(vector_text)
          
          for index, w in enumerate(_predicted_data):
               tweetList[index]['sentiment'] = w

          return JsonResponse(tweetList)

@api_view(['GET'])
def user(request):
     if request.method == "GET":
          username = request.GET.get("username")  # get text from the parameter

          user = Grab.getUserByUsername(username)

          return HttpResponse(user)