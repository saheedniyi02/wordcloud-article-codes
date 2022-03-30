import re
from tweepy import Client



client=Client(bearer_token="###############", consumer_key="###############",consumer_secret="###############",access_token="###############",access_token_secret="###############")
def get_user_text(user_id):
    user_tweets=client.get_users_tweets(id=user_id,max_results=100)[0]
    total_texts=""
    for tweet in user_tweets:
        tweet_text=tweet.text
        total_texts=total_texts+tweet_text
    total_texts=total_texts.lower()
    total_texts=re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '',   total_texts, flags=re.MULTILINE)
    return total_texts 