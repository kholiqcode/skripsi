# 1 Cari Data
# 2 Menghapus Special Character
# 3 Convert case to lower case
# 4 Tokenizing / Pemisahan menjadi kata-kta
# 5 Normalisasi => tai menjadi tahi
# 6 Steeming
# 7 Remove Stopword
# 8 Pembobotan Kata (TF/IDF)

import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# static data
g1 = "saaaarapan roti biar kamu kaya bule"
g2 = "pelit kayaaaaa Orangggg cina anjing"
g3 = "dia pantes lelet kamu Kaya orang jawa"
g4 = "negro"
g5 = "kamu orang timur biasanya yg rusuh"
g6 = "orang-orang banyuwangi suka nyantet"
g7 = "semoga keturunan A'r*ab muka teroris"
tweets = [g1, g2, g3, g4, g5, g6, g7]

# Cleaning
tweets_cleaning = [re.sub(r"[()\"#/@;:<>{}*`'+=~|.!?,]", "", tweet)
                   for tweet in tweets]

# Casefolding
tweets_casefolding = [tweet_cleaning.lower()
                      for tweet_cleaning in tweets_cleaning]

# Tokenizing
tweets_tokenizing = []
for tweet_casefolding in tweets_casefolding:
    tweets_tokenizing.append(tweet_casefolding.split())

# Normalisasi
tweets_normalization = []
pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
for tweet_tokenizing in tweets_tokenizing:
    tweet_normalization = [pattern.sub(r"\1", tweet_per_word)
                           for tweet_per_word in tweet_tokenizing]
    tweets_normalization.append(tweet_normalization)

# Steeming
factory = StemmerFactory()
stemmer = factory.create_stemmer()
tweets_steeming = [stemmer.stem(" ".join(tweet_normalization))
                   for tweet_normalization in tweets_normalization]

# Remove Stopword
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
tweets_stopword = [stopword.remove(tweet_steeming)
                   for tweet_steeming in tweets_steeming]

# Pembobotan Kata
tweets_stopword = [tweet_stopword.split()
                   for tweet_stopword in tweets_stopword]
TF_dict = {}
DF_dict = {}
twets = []
for tweet_stopword in tweets_stopword:
    twets = twets+tweet_stopword
for index, tweet_stopword in enumerate(tweets_stopword):
    WD_dict = {}
    DF = 0
    for word_twet in twets:
        if word_twet in WD_dict and word_twet in tweet_stopword:
            WD_dict[word_twet] += 1
            DF += 1
        elif word_twet not in WD_dict and word_twet in tweet_stopword:
            WD_dict[word_twet] = 1
            DF += 1
        else:
            WD_dict[word_twet] = 0
    for word_tweet in tweet_stopword:
        if word_tweet in DF_dict:
            DF_dict[word_tweet] += 1
        else:
            DF_dict[word_tweet] = 1
    TF_dict[index] = WD_dict
TF_dict["DF"] = DF_dict
TF_dict["IDF"] = [DF_dict[twet]/len(tweets_stopword)
                  for twet in twets]
print(TF_dict)