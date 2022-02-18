import tweepy
import json
import requests
import logging

import wallpaper as wp


def get_quote():
    url = "https://api.quotable.io/random"

    try:
        response = requests.get(url)
    except:
        logger.info("Error while calling API...")
    res = json.loads(response.text)
    print(res)
    return res["content"] + "-" + res["author"]


def get_last_tweet(file):
    f = open(file, "r")
    lastId = int(f.read().strip())
    f.close()
    return lastId


def put_last_tweet(logger, file, Id):
    f = open(file, "w")
    f.write(str(Id))
    f.close()
    logger.info("Updated the file with the latest tweet Id")
    return


# For adding logs in application
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)


with open(".\\credentials.json") as cred_file:
    credentials = json.load(cred_file)[0]

consumer_key = credentials["consumer_key"]
consumer_secret_key = credentials["consumer_secret"]
access_token = credentials["access_token"]
access_token_secret = credentials["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# api = tweepy.Client(**credentials)


def reply_to_tweet(file="tweet_ID.txt"):
    last_id = get_last_tweet(file)
    # mentions = api.get_users_mentions(api.get_me().data['id'], user_auth=True).data
    # mentions = filter(lambda tw: tw.id > last_id, mentions)
    mentions = api.mentions_timeline(since_id=last_id, tweet_mode="extended")
    if len(mentions) == 0:
        return

    new_id = 0
    logger.info("someone mentioned me...")

    for mention in reversed(mentions):
        logger.info(str(mention.id) + "-" + mention.full_text)
        new_id = mention.id

        if True:  # "#bqod" in mention.full_text.lower():
            logger.info("Responding back with QOD to -{}".format(mention.id))
            try:
                tweet = get_quote()
                wp.get_wallpaper(tweet)

                media = api.media_upload("created_image.png")

                logger.info("liking and replying to tweet")

                api.update_status(
                    "@" + mention.user.screen_name + " Here's your Quote",
                    in_reply_to_status_id=mention.id,
                    media_ids=[media.media_id],
                )
            except:
                logger.info("Already replied to {}".format(mention.id))

    put_last_tweet(logger, file, new_id)


if __name__ == "__main__":
    reply_to_tweet()
