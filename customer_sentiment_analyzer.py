#!/usr/bin/python3
import matplotlib.pyplot as plt
import json
from datetime import datetime
from PyQt5.QtWidgets import *


def graph_jetblue_twitter():
    t_satisfaction = []
    t_emotion = []
    dates2 = []
    t_e_total = 0
    t_s_total = 0
    count = 0

    with open("more_twitter_data.json", "r") as f:
        count = 0
        data_list = json.load(f)
        sorted_list = sorted(data_list, key=lambda x: datetime.strptime(x["date"], "%m/%d/%Y"))
        for dic in sorted_list:
            temp = dic["date"].split("/")
            dic["date"] = temp[0] + "/" + temp[2]
            if dic["date"] not in dates2:
                dates2.append(dic["date"])
        for date in dates2:
            for dic in sorted_list:
                if dic["date"] == date:
                    count += 1
                    t_s_total += dic["sentiment"]
                    t_e_total += dic["magnitude"]
            t_satisfaction.append(t_s_total / count)
            t_emotion.append(t_e_total / count)
            count = 0
            t_s_total = 0
            t_e_total = 0
        f.close()
    plt.plot(dates2, t_satisfaction)
    plt.title("jetBlue Customer Sentiment (Twitter)")
    plt.xlabel("Date")
    plt.ylabel("Satisfation")
    plt.xticks(range(0, len(dates2), 2), rotation=90)
    plt.axhline(y= 0, color='r', linestyle='-')
    plt.show()

def graph_jetblue_yelp():
    t_satisfaction = []
    t_emotion = []
    dates2 = []
    t_e_total = 0
    t_s_total = 0
    count = 0

    with open("dev/jetblue_yelp_sent.json", "r") as f:
        count = 0
        data_list = json.load(f)
        sorted_list = sorted(data_list, key=lambda x: datetime.strptime(x["date"], "%m/%d/%Y"))
        for dic in sorted_list:
            temp = dic["date"].split("/")
            dic["date"] = temp[0] + "/" + temp[2]
            if dic["date"] not in dates2:
                dates2.append(dic["date"])
        for date in dates2:
            for dic in sorted_list:
                if dic["date"] == date:
                    count += 1
                    t_s_total += dic["sentiment"]
                    t_e_total += dic["magnitude"]
            t_satisfaction.append(t_s_total / count)
            t_emotion.append(t_e_total / count)
            count = 0
            t_s_total = 0
            t_e_total = 0
        f.close()
    plt.plot(dates2, t_satisfaction)
    plt.title("jetBlue Customer Sentiment (Yelp)")
    plt.xlabel("Date")
    plt.ylabel("Satisfation")
    plt.xticks(range(0, len(dates2), 2), rotation=90)
    plt.axhline(y= 0, color='r', linestyle='-')
    plt.show()

def graph_american():
    satisfaction = []
    emotion = []
    dates = []
    e_total = 0
    s_total = 0
    count = 0
    with open("american_yelp_sent.json", "r") as f:
        data_list = json.load(f)
        sorted_list = sorted(data_list, key=lambda x: datetime.strptime(x["date"], "%m/%d/%Y"))
        for dic in sorted_list:
            temp = dic["date"].split("/")
            dic["date"] = temp[0] + "/" + temp[2]
            if dic["date"] not in dates:
                dates.append(dic["date"])
        for date in dates:
            for dic in sorted_list:
                if dic["date"] == date:
                    count += 1
                    s_total += dic["sentiment"]
                    e_total += dic["magnitude"]
            satisfaction.append(s_total / count)
            emotion.append(e_total / count)
            count = 0
            s_total = 0
            e_total = 0
        f.close()
    plt.plot(dates, satisfaction)
    plt.title("American Airlines Customer Sentiment (Yelp)")
    plt.xlabel("Date")
    plt.ylabel("Satisfation")
    plt.xticks(range(0, len(dates), 3), rotation=90)
    plt.axhline(y= 0, color='r', linestyle='-')
    plt.show()


def graph_spirit():
    satisfaction = []
    emotion = []
    dates = []
    e_total = 0
    s_total = 0
    count = 0
    with open("spirit_yelp_sent.json", "r") as f:
        data_list = json.load(f)
        sorted_list = sorted(data_list, key=lambda x: datetime.strptime(x["date"], "%m/%d/%Y"))
        for dic in sorted_list:
            temp = dic["date"].split("/")
            dic["date"] = temp[0] + "/" + temp[2]
            if dic["date"] not in dates:
                dates.append(dic["date"])
        for date in dates:
            for dic in sorted_list:
                if dic["date"] == date:
                    count += 1
                    s_total += dic["sentiment"]
                    e_total += dic["magnitude"]
            satisfaction.append(s_total / count)
            emotion.append(e_total / count)
            count = 0
            s_total = 0
            e_total = 0
        f.close()
    plt.plot(dates, satisfaction)
    plt.title("Spirit Customer Sentiment (Yelp)")
    plt.xlabel("Date")
    plt.ylabel("Satisfation")
    plt.xticks(range(0, len(dates), 3), rotation=90)
    plt.axhline(y= 0, color='r', linestyle='-')
    plt.show()

def graph_delta():
    satisfaction = []
    emotion = []
    dates = []
    e_total = 0
    s_total = 0
    count = 0
    with open("delta_yelp_sent.json", "r") as f:
        data_list = json.load(f)
        sorted_list = sorted(data_list, key=lambda x: datetime.strptime(x["date"], "%m/%d/%Y"))
        for dic in sorted_list:
            temp = dic["date"].split("/")
            dic["date"] = temp[0] + "/" + temp[2]
            if dic["date"] not in dates:
                dates.append(dic["date"])
        for date in dates:
            for dic in sorted_list:
                if dic["date"] == date:
                    count += 1
                    s_total += dic["sentiment"]
                    e_total += dic["magnitude"]
            satisfaction.append(s_total / count)
            emotion.append(e_total / count)
            count = 0
            s_total = 0
            e_total = 0
        f.close()
    plt.plot(dates, satisfaction)
    plt.title("Delta Customer Sentiment (Yelp)")
    plt.xlabel("Date")
    plt.ylabel("Satisfation")
    plt.xticks(range(0, len(dates), 3), rotation=90)
    plt.axhline(y= 0, color='r', linestyle='-')
    plt.show()



app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
quest = QLabel('Which graph would you like to see?')

delta = QPushButton('Delta (Yelp)')
american = QPushButton('American Airlines (Yelp)')
spirit = QPushButton('Spirit (Yelp)')
jblue = QPushButton('jetBlue (Twitter)')
jblue2 = QPushButton('jetBlue (Yelp)')

jblue2.clicked.connect(graph_jetblue_yelp)
jblue.clicked.connect(graph_jetblue_twitter)
american.clicked.connect(graph_american)
spirit.clicked.connect(graph_spirit)
delta.clicked.connect(graph_delta)


layout.addWidget(quest)
layout.addWidget(jblue)
layout.addWidget(jblue2)
layout.addWidget(delta)
layout.addWidget(american)
layout.addWidget(spirit)
window.setLayout(layout)
window.show()

app.exec_()
