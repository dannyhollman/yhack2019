from urllib.request import urlopen
from bs4 import BeautifulSoup
from csv import DictWriter
import time


def scrape_yelp(start):
    """ scrape craigsliest """ 

    # pause before calling request
    time.sleep(.25)
    response = urlopen(f'https://www.yelp.com/biz/jetblue-airways-new-york?start={start}')
    # parse response
    html = BeautifulSoup(response.read(), 'html.parser')
    review_content = html.find_all(class_="review-content")
    return review_content


def append_data(review):
    """ create list of dicts """

    data = {
        "date": get_date(review),
        "rating": get_rating(review),
        "review": get_review(review)
    }
    return data


def collect_data(review_content):
    """ returns list of dictionaries """

    review_data = []
    for review in review_content:
        review_data.append(append_data(review))
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


def main():
    """ collect reviews in a csv file """

    t0 = time.time()
    start = 0
    while (1):
        try:
            review_content = scrape_yelp(start)

            write_apts(collect_data(review_content))
            print(start)
            print(collect_data(review_content)[0]["date"] != None)
        except:
            break

        start += 20
    t = time.time()
    print(f"Program took {t - t0} seconds!")
main()
