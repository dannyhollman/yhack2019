#!/usr/bin/python3
""" The scraper module. """
from selenium import webdriver
from time import sleep

opts = webdriver.firefox.options.Options()
#opts.headless = True

drive = webdriver.Firefox(options=opts)
drive.get("https://mobile.twitter.com/search/?q=jetblue&src=typd")
for i in range(0, 10):
    drive.execute_script("window.scrollBy(0, 1000)")
    sleep(1)
print(drive.execute_script("""
var reqs = Array()
page.onResourceRequested = function(req, netReq) {
    reqs.push(req.url)
}
alert(json.stringify(reqs))"""))
    #"return document.documentElement.outerHTML"))
#drive.quit()
print("done")
