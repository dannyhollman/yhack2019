from parse_json_data import get_tweets
from sentiment import sentiment

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
    return list_scores
    
if __name__ == "__main__":
    main()
