from parse_json_data import get_tweets
from sentiment import sentiment

def main():

    tweets = []
    list_scores = []

    tweets = get_tweets("adaptive.json")
    for tweet in tweets:
        print(tweet[1])
        print(tweet[0])
        scores = sentiment(tweet)
        list_scores.append(scores)
        print("{}\n".format(scores))
    print(list_scores)
    return list_scores
    
if __name__ == "__main__":
    main()
