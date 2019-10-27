import matplotlib.pyplot as plt
import json
from datetime import datetime

def graph_yelp():
	satisfaction = []
	emotion = []
	dates = []
	e_total = 0
	s_total = 0
	count = 0
	with open("jetblue_yelp_sent.json", "r") as f:
		data_list = json.load(f)
		sorted_list = sorted(data_list, key=lambda x: datetime.strptime(x["date"], "%m/%d/%Y"))
		for dic in sorted_list:
			temp = dic["date"].split("/")
			dic["date"] = temp[0] + "/" + temp[2]
			if dic["date"] not in dates and int(dic["date"][-4:]) > 2013:
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

	plt.plot(dates, satisfaction, dates, list(map(lambda x: (x/10), emotion)))
	plt.xlabel("Date")
	plt.ylabel("Satisfaction")
	plt.xticks(rotation=90)
	plt.show()

def graph_twitter():
	satisfaction = []
	emotion = []
	dates = []
	e_total = 0
	s_total = 0
	count = 0
	with open("more_twitter_data.json", "r") as f:
		data_list = json.load(f)
		sorted_list = sorted(data_list, key=lambda x: datetime.strptime(x["date"], "%m/%d/%Y"))
		for dic in sorted_list:
			print(dic["date"])
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
	plt.xlabel("Date")
	plt.ylabel("Satisfation")
	plt.xticks(rotation=90)
	plt.show()



def main():
	graph_twitter()
	graph_yelp()
if __name__ == "__main__":
	main()
