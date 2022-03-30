from tweepy import Client
from get_tweets import get_user_text
from create_wordcloud import create_wordcloud
BEARER_TOKEN="##########"
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

my_id=client.get_me()[0].id
my_username=client.get_me()[0].username




import os



def reply_tweets():
    mentioned_tweets=client.get_users_mentions(id=my_id,max_results=50,expansions="author_id")
    print(mentioned_tweets[0])
    for tweet in reversed(mentioned_tweets[0]):
        request=tweet.text
        tweet_id=tweet.id

        if ("#createmywordcloud" in request.lower()) and (f"{tweet_id}.jpg" not in os.listdir("Images")):
            try:
                author_id=tweet.author_id
                text=get_user_text(author_id)
                create_wordcloud(text,tweet_id)
                client.create_tweet(text=f"Your word cloud can be found here http://127.0.0.1:5000/{tweet_id}",
                in_reply_to_tweets=tweet_id)
                print("hi2")
                client.like(tweet_id)
                client.retweet(tweet_id)
            except:
                print("error occurred")
        else:
            print("invalid request")

