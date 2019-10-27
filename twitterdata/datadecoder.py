#!/usr/bin/python3
"""decode the har data"""
from sys import argv
import json
import re

def filter_good(truples):
    """filter out bad arrays"""
    def filter_one(trup):
        """filter one truple"""
        if re.compile("\d\d/\d\d/\d\d\d\d").findall(trup[0]) == []:
            return False
        if trup[1] == '':
            return False
        if trup[2] == '' or trup[2] == "6449282": ### !--filter out jetblue userid of 6449282
            return False
        if len(trup) != 3:
            return False

        return True

    return [x for x in truples if filter_one(x)]

def decode_date(datestr):
    """decode the twitter date into a dd/mm/yyyy form"""
    mo = -1
    if 'Jan' in datestr:
        mo = 1
    if 'Feb' in datestr:
        mo = 2
    if 'Mar' in datestr:
        mo = 3
    if 'Apr' in datestr:
        mo = 4
    if 'May' in datestr:
        mo = 5
    if 'Jun' in datestr:
        mo = 6
    if 'Jul' in datestr:
        mo = 7
    if 'Aug' in datestr:
        mo = 8
    if 'Sep' in datestr:
        mo = 9
    if 'Oct' in datestr:
        mo = 10
    if 'Nov' in datestr:
        mo = 11
    if 'Dec' in datestr:
        mo = 12

    day = datestr.split(' ')[2]
    year = datestr.split(' ')[-1]

    return("{:02d}/{}/{}".format(mo, day, year))

def get_all_matches(thing):
    """match the twitter post regex against raw har text"""
    spl = thing.split('\\"')

    full = []
    temp = []
    for i in range(0, len(spl)):
        if spl[i] == "created_at":
            temp.append(decode_date(spl[i + 2]))
        if spl[i] == "full_text":
            temp.append(spl[i + 2])
        if spl[i] == "user_id" and (spl[i + 1])[0] == ':':
            temp.append((spl[i + 1])[1:-1])
            full.append(temp)
            temp = []


    full = filter_good(full)

    return full

def jsonify(l):
    """make all data into dict form"""

    newl = [{"date": x[0], "review": x[1], "user": x[2]} for x in l]
    
    return json.dumps(newl)

lol = []
for a in argv[1:]:
    print(a)
    with open(a, "r") as f:
        for l in f:
            lol.extend(get_all_matches(str(l)))

j = jsonify(lol)
with open("jetblue_twitter.json", "w+") as f2:
    f2.write(j)
print("done")
