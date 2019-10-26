from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

def sentiment(tweet):

    # The text to analyze
    text = tweet[0]
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Sentiment: {}, {}\n'.format(sentiment.score, sentiment.magnitude))
    t1 = tweet[1]
    return ((t1, round(sentiment.score, 2), round(sentiment.magnitude, 2)))
