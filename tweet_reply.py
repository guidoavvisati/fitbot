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


def load_credentials():
    try:
        with open(".\\credentials.json") as cred_file:
            credentials = json.load(cred_file)[0]

        c_key = credentials["consumer_key"]
        cs_key = credentials["consumer_secret"]
        a_token = credentials["access_token"]
        as_token = credentials["access_token_secret"]
    except FileNotFoundError:
        import os

        c_key = os.getenv("CONSUMER_KEY")
        cs_key = os.getenv("CONSUMER_SECRET")
        a_token = os.getenv("ACCESS_TOKEN")
        as_token = os.getenv("ACCESS_TOKEN_SECRET")

    return c_key, cs_key, a_token, as_token


# For adding logs in application
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

creds = load_credentials()

auth = tweepy.OAuthHandler(*creds[:2])
auth.set_access_token(*creds[2:])
api = tweepy.API(auth)
# api = tweepy.Client(**credentials)


def reply_to_tweet(file="tweet_ID.txt"):
    last_id = get_last_tweet(file)
    # mentions = api.get_users_mentions(api.get_me().data['id'], user_auth=True).data
    # mentions = filter(lambda tw: tw.id > last_id, mentions)
    mentions = api.mentions_timeline(since_id=last_id, tweet_mode="extended")
    if len(mentions) == 0:
        return
    mentions = list(filter(lambda tw: tw.id_str == "1494631949599752192", mentions))

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

    # put_last_tweet(logger, file, new_id)


if __name__ == "__main__":
    reply_to_tweet()
