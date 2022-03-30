from flask import Flask,render_template,url_for,send_file
from apscheduler.schedulers.background import BackgroundScheduler
from bot import reply_tweets



app=Flask(__name__, template_folder="templates") #initialize the flask app




#create the home route
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/display-word-cloud/<string:tweet_id")
def view_wordcloud(tweet_id):
    image_path=url_for("Images", filename=f"{tweet_id}.jpg")
    return render_template("display_image.html",image_path=image_path,tweet_id=tweet_id)



@app.route("/download/<string:tweet_id>")
def download_image(tweet_id):
    return send_file(f"Images/{tweet_id}.jpg",as_attachment=True)

scheduler = BackgroundScheduler()
scheduler.add_job(func=reply_tweets, trigger="interval", seconds=600)
scheduler.start()

if __name__=="__main__":
    app.run(debug=False)