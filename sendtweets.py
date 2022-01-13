import tweepy, os
from dotenv import load_dotenv

#read in and set env variables
load_dotenv() 
APPKEY = os.environ.get('APPKEY')
APPSECRET = os.environ.get('APPSECRET')
ACCOUNTKEY = os.environ.get('ACCOUNTKEY')
ACCOUNTSECRET = os.environ.get('ACCOUNTSECRET')


f = open("../DownloadTest/info.txt", "r")
lyric, style = f.readline().strip(), f.readline().strip()

# auth setup for 1.1 endpoint
auth = tweepy.OAuthHandler(APPKEY, APPSECRET)
auth.set_access_token(ACCOUNTKEY, ACCOUNTSECRET)
helper=tweepy.API(auth)
img = helper.simple_upload('../DownloadTest/swin/step-024_SwinIR_large.png')
print(img)
art_id = img.media_id_string
vid = helper.media_upload('../DownloadTest/process.mp4', wait_for_async_finalize=True)
print(vid)
vid_id=vid.media_id_string

bot = tweepy.Client(consumer_key = APPKEY, consumer_secret = APPSECRET, 
                    access_token = ACCOUNTKEY, access_token_secret = ACCOUNTSECRET)
art_tweet = bot.create_tweet(text=lyric, media_ids=[art_id])
print(art_tweet)
art_tweet_id = art_tweet.data.get('id')
vid_tweet = bot.create_tweet(media_ids=[vid_id], in_reply_to_tweet_id = art_tweet_id)
print(vid_tweet)

