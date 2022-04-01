from wordcloud import WordCloud


def create_wordcloud(text, tweet_id):
    wordcloud = WordCloud(
        background_color="white",
        colormap="spring",
        width=1600,
        height=800,
    ).generate(text)
    wordcloud_img = wordcloud.to_image()
    wordcloud_img.save(f"static/{tweet_id}.jpg")
