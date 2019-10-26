import json

def get_tweets(json_file):

    list = []

    with open(json_file, "r") as file:
        dict = json.load(file)

    tweets = dict["globalObjects"]["tweets"]


    for value in tweets.values():
        list.append((value["full_text"], value["created_at"]))

    return list
