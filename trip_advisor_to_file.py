import json
from csv import DictWriter


def upload_file(json_file):
    """ upload a file and return list of dicts """

    with open(json_file, "r", encoding="utf-8") as f:
        data = f.read()

    data = json.loads(data)
    return data

def clean_trip_advisor(data):
    """ clean trip advisor data """


    review_data = []

    for review in data["reviews"]:
        dr = review["title"][1]
        date = dr["date"]
        review_text = dr["review_text"]
        review_data.append({"date": date, "review": review_text})
    
    return review_data


def write_apts(review_data):
    """ create/append to a csv file"""

    file_name = "trip_advisor_reviews_JBLU"
    with open(f"{file_name}.csv", "a", encoding='utf-8') as file:
        headers = ["date", "review"]
        # posible peek function to not repeat headers peek(0)
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for review in review_data:
            csv_writer.writerow(review)
    return print(f"apts added to {file_name}.csv.")


def to_json_string(list_dictionaries):
    """ converts dict to json """

    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)


def save_to_file(LO_dict):
    """ write into a .json file """

    filename = "trip_advisor_reviews_JBLU.json"

    with open(filename, "a") as f:
        f.write(to_json_string(LO_dict))
    print(f"Appended to {filename}.json")

def __main__():

    json_file = "trip_adv_JBLU_reviews.json"

    clean_data = clean_trip_advisor(upload_file(json_file))

    save_to_file(clean_data)


__main__()
