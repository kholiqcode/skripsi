from flask import Flask,render_template, jsonify
import main

app = Flask(__name__)

# Hasil Preprocessng
@app.route("/api/tweet", methods=['GET'])
def api_tweet():
    dict = main._FS
    return jsonify(dict)

# Get Tweet from Twitter
@app.route("/api/tweet/<string:keyword>", methods=['GET'])
def api_tweets(keyword):
    return keyword

if __name__ == "__main__":
    app.run(debug=True)