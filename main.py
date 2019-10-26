from parse_json_data import get_tweets
from sentiment import sentiment
import json


def main():
    tweets = []
    list_scores = []

    # get list of tweets
    tweets = get_tweets("adaptive.json")
    for tweet in tweets:
        # make sentiment/magnitude into a tuple
        scores = sentiment(tweet[0])
        scores = scores + (tweet[1],)
        list_scores.append(scores)
        # tweet[0] is actual tweet / tweet[1] is date
        print(tweet[0])
        print(tweet[1])
        print("{}\n".format(scores))

    print(list_scores)

    with open("jetblue.json", "r", encoding="utf-8") as f:
        read = f.read()
        data1 = read.split("]")[0]
        data2 = read.split("]")[1]
    data += "]"
    data = json.loads(data1) + json.loads("[" + data2[1:] + "]")

    print(data)

    return list_scores



if __name__ == "__main__":
    main()
