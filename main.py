from parse_json_data import get_tweets
from sentiment import sentiment
import json

def to_json_string(list_dictionaries):
    """ converts dict to json """
    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)

def twitter_data_to_json():
    tweets = []
    list_dicts = []

    with open("twitterdata/jetblue_twitter.json", "r", encoding="utf-8") as f:
        load = f.read()

    tweets = json.loads(load)
    # get list of tweets
    for tweet in tweets:
        sent_mag = sentiment(tweet["review"])
        # make sentiment/magnitude into a tuple
        list_dicts.append({
                "date" : tweet["date"],
                "sentiment" : sent_mag[0],
                "magnitude" : sent_mag[1]
                })
        count = len(list_dicts)
        if count % 20 == 0:
            print(f"collected {count} reviews!")
        # tweet[0] is actual tweet / tweet[1] is date

    with open("jetblue_twitter_sent.json", "a", encoding="utf-8") as f:
              f.write(to_json_string(list_dicts))

    print(list_dicts)
    return list_dicts

twitter_data_to_json()
