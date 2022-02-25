import json
from json.encoder import JSONEncoder
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import pandas as pd
import numpy as np

from sentiment import clean_text
from sentiment.apps import SentimentConfig
from sentiment.grab import Grab
# Create your views here.

def dashboard(request):
     konteks = {
          'title' : 'Judul'
     }
     return render(request, 'dashboard.html', konteks)

def users(request):
     context = {
          'title' : 'Profil',
          'users' : [
               {
                    'username' : 'jokowi',
                    'screen_name' : 'Joko Widodo'
               },
               {
                    'username' : 'prabowo',
                    'screen_name' : 'Prabowo Subianto'
               },
               {
                    'username' : 'andhiyat',
                    'screen_name' : 'Andi Hidayat'
               },
               {
                    'username' : 'fiersabesari',
                    'screen_name' : 'Fiersa Besari'
               },
               {
                    'username' : 'sandiuno',
                    'screen_name' : 'Sandiaga Salahudin Uno'
               },
               {
                    'username' : 'bayu_yoo',
                    'screen_name' : 'Bayu Joo'
               },
               {
                    'username' : 'dsuperboy',
                    'screen_name' : 'Boy Candra'
               },
               {
                    'username' : 'radenrauf',
                    'screen_name' : 'Raden Rauf'
               },
               {
                    'username' : 'jayakabajay',
                    'screen_name' : 'Fajar R'
               },
          ]
     }
     return render(request, 'users.html', context)

def profil(request):
     context = {
          'title' : 'Profil'
     }

     if request.method == "GET":
          username = request.GET.get("username")  # get text from the parameter

          user = Grab.getUserByUsername(username)
          context['user'] = user
          tweetList = Grab.getTweetByUsername(username)
          process = clean_text.TextPreprocess()
          for index,tweet in enumerate(tweetList):
               cleaned_text = process.normalizer(tweet['text'])
               # vectorizing the given text
               vector_text = SentimentConfig.vectorizer_general.transform([cleaned_text])
               # Predict sentiment based on vector
               _predicted_data = SentimentConfig.model_general.predict(vector_text)
               _predicted_proba = SentimentConfig.model_general.predict_proba(vector_text)
               prob = np.max(_predicted_proba[0])

               if (_predicted_data == "positive"):
                    if prob >= 0.9:
                         result = 1
                    else:
                         result = 0
               elif (_predicted_data == "negative"):
                    if prob >= 0.9:
                         result = -1
                    else:
                         result = 0
               else:
                    result = 0
               tweetList[index]['label'] = result
          context['tweetList'] = tweetList
     
     return render(request, 'profil.html', context)

def tag(request):
     context = {
          'title' : 'Tags'
     }

     if request.method == "GET":
          tag = request.GET.get("tag")  # get text from the parameter

          tweetList = Grab.getTweetByTag()
          process = clean_text.TextPreprocess()
          for index,tweet in enumerate(tweetList):
               cleaned_text = process.normalizer(tweet['text'])
               # vectorizing the given text
               vector_text = SentimentConfig.vectorizer_general.transform([cleaned_text])
               # Predict sentiment based on vector
               _predicted_data = SentimentConfig.model_general.predict(vector_text)
               _predicted_proba = SentimentConfig.model_general.predict_proba(vector_text)
               prob = np.max(_predicted_proba[0])

               if (_predicted_data == "positive"):
                    if prob >= 0.9:
                         result = 0
                    else:
                         result = 1
               elif (_predicted_data == "negative"):
                    if prob >= 0.9:
                         result = -1
                    else:
                         result = 0
               else:
                    result = 0
               tweetList[index]['label'] = result
          context['tweetList'] = tweetList
     
     return render(request, 'tag.html', context)

def sentiment(request):
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
     konteks = {
          'title' : 'Sentiment',
          'tweetList' : tweetList
     }

     return render(request, 'sentiment.html', konteks)

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

          return JsonResponse(tweetList,safe=False)

@api_view(['GET'])
def user(request):
     if request.method == "GET":
          username = request.GET.get("username")  # get text from the parameter

          user = Grab.getUserByUsername(username)

          return HttpResponse(user)