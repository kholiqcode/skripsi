import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Cleaning


def Cleaning(tweets):
    return [re.sub(r"[()\"#/@;:<>{}*`'+=~|.!?,]", "", tweet)
            for tweet in tweets]


def Casefolding(tweets):
    return [tweet_cleaning.lower()
            for tweet_cleaning in tweets]

# Tokenizing


def Tokenizing(tweets):
    tweets_tokenizing = []
    for tweet_casefolding in tweets:
        tweets_tokenizing.append(tweet_casefolding.split())
    return tweets_tokenizing


# Normalisasi
def Normalization(tweets):
    tweets_normalization = []
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    for tweet_tokenizing in tweets:
        tweet_normalization = [pattern.sub(r"\1", tweet_per_word)
                               for tweet_per_word in tweet_tokenizing]
        tweets_normalization.append(tweet_normalization)
    return tweets_normalization


# Steeming
def Steeming(tweets):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return [stemmer.stem(" ".join(tweet_normalization))
            for tweet_normalization in tweets]


# Remove Stopword
def Stopword(tweets):
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    return [stopword.remove(tweet_steeming)
            for tweet_steeming in tweets]

# Pembobotan Kata


def Pembobotan(tweets):
    return [tweet_stopword.split()
            for tweet_stopword in tweets]
