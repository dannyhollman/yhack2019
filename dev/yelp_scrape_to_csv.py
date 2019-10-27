from urllib.request import urlopen
from bs4 import BeautifulSoup
from csv import DictWriter
import time
import json


def scrape_yelp(start, airline):
    """ scrape yelp """

    #different airlines to get their sentiments
    BaseURL = "https://www.yelp.com/biz/"
    airlines ={
    "delta" : "delta-air-lines-los-angeles-3",
    "spirit" : "spirit-airlines-los-angeles",
    "american" : "american-airlines-los-angeles-5",
    "jetblue" : "jetblue-airways-new-york"
    }
    # pause before calling request
    time.sleep(.25)

    response = urlopen(f"{BaseURL}{airlines[airline]}?start={start}")
    # parse response
    html = BeautifulSoup(response.read(), "html.parser")
    review_content = html.find_all(class_="review-content")
    return review_content


def append_data(review, count):
    """ create list of dicts """

    data = {
        "count": count,
        "date": get_date(review),
        "rating": get_rating(review),
        "review": get_review(review)
    }
    return data


def collect_data(airline):
    """ returns list of dictionaries """

    count = 0
    start = 0
    size = 0
    last_size = -1
    review_data = []

    while (1):
        try:
            review_content = scrape_yelp(start, airline.lower())
            
            for review in review_content:
                data = append_data(review, (start + count))
                count += 1
                review_data.append(data)
            size = len(review_data)
            print(f"in collect data {size}")
            # break when no new data is collected
            if size ==last_size:
                break
            last_size = size
        except Exception as e:
            print(e)
            break
        start +=20
    return review_data


def get_date(review):
    """ get date """

    try:
        date_str = review.find_all(
            class_="rating-qualifier")[0].get_text().split(" ")
        for date in date_str:
            try:
                if date[0].isdigit():
                    date = date.split("\n")[0]
                    break
            except:
                continue
    except:
        date = "None"
    return date


def get_review(review):
    """ get review """

    try:
        review_text = review.find_all("p")[0].get_text()
    except:
        review_text = "None"
    return review_text


def get_rating(review):
    """ get rating """

    try:
        rating = review.find_all(
            class_="biz-rating__stars")[0].find("div").get("title")
    except:
        rating = "None"
    return rating


def write_apts(review_data):
    """ create/append to a csv file"""

    file_name = "yelp_reviews"
    with open(f"{file_name}.csv", "a", encoding='utf-8') as file:
        headers = ["date", "rating", "review"]
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


def save_to_file(LO_dict, airline):
    """ write into a .json file """

    with open(airline + "_yelp.json", "a") as f:
        f.write(to_json_string(LO_dict))
    print(f"Appended to {airline}_yelp.json")

def main():
    """ collect reviews in a csv file """

    t0 = time.time()
    airline = "american"
        
    try:
        
        data = collect_data(airline)
        print(f"data = {len(data)}")

    except Exception as e:
        print(e)

    save_to_file(data, airline)
    t = time.time()
    print(f"Program took {t - t0} seconds!")

main()