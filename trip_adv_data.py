from sentiment import sentiment
import json

def to_json_string(list_dictionaries):
    """ converts dict to json """
    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)

def trip_advisor_data():

    list_dicts = []

    with open("trip_advisor_reviews_JBLU.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)

    for data in dataset:
        sent_mag = sentiment(data["review"])
        list_dicts.append({
                "date" : data["date"],
                "sentiment" : sent_mag[0],
                "magnitude" : sent_mag[1],
                })

    with open("jetblue_tripadvisor_sent.json", "w", encoding="utf-8") as f:
        f.write(to_json_string(list_dicts))

    print(list_dicts)

trip_advisor_data()

