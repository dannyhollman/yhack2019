from sentiment import sentiment
from yelp_scrape_to_csv import to_json_string
import json

def yelp_data_to_json():

       with open("jetblue.json", "r", encoding="utf-8") as f:
              read = f.read()
              data1 = read.split("]")[0]
              data2 = read.split("]")[1]
       data1 += "]"
       dataset = json.loads(data1) + json.loads("[" + data2[1:] + "]")

       list_dicts = []

       for data in dataset:
              sent_mag = sentiment(data["review"])
              list_dicts.append({
                            "date" : data["date"],
                            "sentiment" : sent_mag[0],
                            "magnitude" : sent_mag[1]
                            })
       with open("jetblue_yelp_sent.json", "a", encoding="utf-8") as f:
              f.write(to_json_string(list_dicts))

       print(list_dicts)
yelp_data_to_json()
