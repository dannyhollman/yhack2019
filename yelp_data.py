from sentiment import sentiment
from yelp_scrape_to_csv import to_json_string
import json

def yelp_data_to_json():
       airline = "american"

       with open(f"{airline}_yelp.json", "r", encoding="utf-8") as f:
              load = f.read()
       dataset = json.loads(load)
       list_dicts = []
       count = 0
       for data in dataset:
              sent_mag = sentiment(data["review"])
              list_dicts.append({
                            "date" : data["date"],
                            "sentiment" : sent_mag[0],
                            "magnitude" : sent_mag[1]
                            })
              count = len(list_dicts)
              if count % 20 == 0:
                     print(f"collected {count} reviews!")
       with open(f"{airline}_yelp_sent.json", "w", encoding="utf-8") as f:
              f.write(to_json_string(list_dicts))

       print(list_dicts)
yelp_data_to_json()
