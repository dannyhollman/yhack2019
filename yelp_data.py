from sentiment import sentiment
from yelp_scrape_to_csv import to_json_string
import json

def yelp_data_to_json():

       with open("jetblue_yelp.json", "r", encoding="utf-8") as f:
              load = f.read()
       dataset = json.loads(load)
       list_dicts = []
       for data in dataset:
              sent_mag = sentiment(data["review"])
              list_dicts.append({
                            "date" : data["date"],
                            "sentiment" : sent_mag[0],
                            "magnitude" : sent_mag[1]
                            })
       with open("jetblue_yelp_sent.json", "w", encoding="utf-8") as f:
              f.write(to_json_string(list_dicts))

       print(list_dicts)
yelp_data_to_json()
