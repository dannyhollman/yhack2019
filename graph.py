import matplotlib.pyplot as plt
import json
from datetime import datetime

def graph_jetblue():
	t_satisfaction = []
	y_satisfaction = []
	t_emotion = []
	y_emotion = []
	dates = []
	dates2 = []
	t_e_total = 0
	y_e_total = 0
	t_s_total = 0
	y_s_total = 0
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
					y_s_total += dic["sentiment"]
					y_e_total += dic["magnitude"]
			y_satisfaction.append(y_s_total / count)
			y_emotion.append(y_e_total / count)
			count = 0
			y_s_total = 0
			y_e_total = 0
		f.close()

	with open("more_twitter_data.json", "r") as f:
		count = 0
		data_list = json.load(f)
		sorted_list = sorted(data_list, key=lambda x: datetime.strptime(x["date"], "%m/%d/%Y"))
		for dic in sorted_list:
			print(dic["date"])
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
	plt.plot(dates2, t_satisfaction) #, dates2, t_satisfaction)
	plt.xlabel("Date")
	plt.ylabel("Satisfation")
	plt.xticks(rotation=90)
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
	graph_spirit()
if __name__ == "__main__":
	main()
