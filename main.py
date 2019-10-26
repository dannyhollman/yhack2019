from parse_json_data import get_tweets
from sentiment import sentiment

def main():

    tweets = []

    tweets = get_tweets("adaptive.json")
    for tweet in tweets:
        print(tweet[1])
        print(tweet[0])
        scores = sentiment(tweet)
        print("{}\n".format(scores))
    return(scores)
    
if __name__ == "__main__":
    main()
