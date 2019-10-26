from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

def sentiment(tweet):

    # The text to analyze
    text = tweet
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Sentiment: {}, {}\n---------'.format(sentiment.score, sentiment.magnitude))

    return ((round(sentiment.score, 2), round(sentiment.magnitude, 2)))
