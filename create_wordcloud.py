from wordcloud import WordCloud

def create_wordcloud(text,tweet_id):
    wordcloud=WordCloud().generate(text)
    wordcloud_img=wordcloud.to_image()
    wordcloud_img.save(f"Images/{tweet_id}.jpg")