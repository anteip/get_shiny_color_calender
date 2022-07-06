import tweepy
from config import CONFIG
import urllib.request
import re
import json
import datetime
import getpass

CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

#取得したURLを使って画像を保存
def save_image(url):
    count = 1
    user = getpass.getuser()
    dir = "/home/" + user + "/gscc/"

    for image_url in url:
        image_url = image_url + ":orig"
        date = datetime.date.today()
        file_path = dir + date.strftime('%Y-%m') + "-01_imassc_calender_" + str(count) + ".jpeg"
        data = urllib.request.urlopen(image_url).read()
        with open(file_path, mode="wb") as f:
            f.write(data)
        count += 1

#画像URLを取得
def get_image():
    result_url = []
    for tweet in tweepy.Cursor(api.user_timeline, id="imassc_official").items(20):
        if (list(tweet.text)[:2]!=['R', 'T']) & (list(tweet.text)[0]!='@'):
            if "#シャニマスカレンダー" in tweet.text:
                for media in tweet.extended_entities['media']:
                    result_url.append(media['media_url'])
    return result_url

def start():
    url = get_image()
    save_image(url)

if __name__ == "__main__":
    start()
