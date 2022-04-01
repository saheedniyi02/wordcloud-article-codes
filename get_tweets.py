import re
from tweepy import Client

ACCESS_TOKEN="##########"
ACCESS_TOKEN_SECRET="##########"
API_KEY="##########"
API_SECRET_KEY="##########"


client = Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)



def get_user_text(user_id):
    user_tweets = client.get_users_tweets(id=user_id, max_results=100)[0]
    total_texts = ""
    for tweet in user_tweets:
        tweet_text = tweet.text
        total_texts = total_texts + tweet_text
    total_texts = total_texts.lower()
    total_texts = re.sub(
        r"(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b",
        "",
        total_texts,
        flags=re.MULTILINE,
    )
    return total_texts
