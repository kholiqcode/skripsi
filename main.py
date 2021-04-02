# 1 Cari Data
# 2 Menghapus Special Character
# 3 Convert case to lower case
# 4 Tokenizing / Pemisahan menjadi kata-kta
# 5 Normalisasi => tai menjadi tahi
# 6 Steeming
# 7 Remove Stopword
# 8 Pembobotan Kata (TF/IDF)

import core
import json

# static data
g1 = "saaaarapan roti biar kamu kaya bule"
g2 = "pelit kayaaaaa saaaarapan Orangggg cina anjing"
g3 = "dia pantes lelet kamu Kaya orang jawa"
g4 = "negro"
g5 = "kamu orang timur biasanya yg rusuh"
g6 = "orang-orang banyuwangi suka nyantet"
g7 = "semoga keturunan A'r*ab muka teroris"
tweets = [g1, g2, g3, g4, g5, g6, g7]

# Cleaning
tweets_cleaning = core.Cleaning(tweets)

# Casefolding
tweets_casefolding = core.Casefolding(tweets_cleaning)

# Tokenizing
tweets_tokenizing = core.Tokenizing(tweets_casefolding)

# Normalisasi
tweets_normalization = core.Normalization(tweets_tokenizing)

# Steeming
tweets_steeming = core.Steeming(tweets_normalization)

# Remove Stopword
tweets_stopword = core.Stopword(tweets_steeming)

# Pembobotan Kata
tweets_stopword = core.Pembobotan(tweets_stopword)


twets = []
for tweet_stopword in tweets_stopword:
    twets = twets+tweet_stopword
TWEETS = {}
for tweet in twets:
    _TF_dict = {}
    _DF = 0
    for index, tweet_stopword in enumerate(tweets_stopword):
        if tweet in tweet_stopword and tweet in _TF_dict:
            _TF_dict["Tweet"+str(index)] += 1
            _DF += 1
        elif tweet in tweet_stopword and tweet not in _TF_dict:
            _TF_dict["Tweet"+str(index)] = 1
            _DF += 1
        else:
            _TF_dict["Tweet"+str(index)] = 0
    _TF_dict["DF"] = _DF
    _TF_dict["IDF"] = _DF/len(tweets_stopword)
    TWEETS[tweet] = _TF_dict

# Hasil Pembobotan
RESULT_TF_IDF = {}
for tweet in twets:
    _TF_IDF_dict = {}
    for index, tweet_stopword in enumerate(tweets_stopword):
        _TF_IDF_dict["Tweet"+str(index)] = TWEETS[tweet]["Tweet" +
                                                         str(index)]*TWEETS[tweet]["IDF"]
    RESULT_TF_IDF[tweet] = _TF_IDF_dict

# print(RESULT_TF_IDF)
# print(json.dumps(TWEETS.keys()))
# key_list = list(TWEETS.keys())
# print(key_list[0])

# Analisa Fitur Selection
_FS = {}
for TWEET in TWEETS:
    _FS[TWEET] = RESULT_TF_IDF[TWEET]
    _FS[TWEET]['DF'] = TWEETS[TWEET]['DF']

print(_FS)
