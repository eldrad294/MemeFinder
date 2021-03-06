#
# Module imports
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
from src.Meme_Object import Meme_Object
import os
#
# Path variables
URL_CONFIG = os.path.dirname(os.path.realpath(__file__)) + "/URL_CONFIG.txt"
URL_RESULTS = os.path.dirname(os.path.realpath(__file__)) + "/URL_RESULTS.txt"
#
# Read from URL_CONFIG file and retrieve html elements, attribute values and URLs
try:
    with open(URL_CONFIG, 'r') as f:
        file = f.read().splitlines()
    print("Urls extracted from file. Preparing for dank meme extraction")
except FileNotFoundError:
    print("URL_CONFIG.txt was not found")
    exit(1)
#
# Iterate over items retrieved from URL_CONFIG
url_results = ''
for line in file:
    #
    obj = Meme_Object(line)
    #
    # Ignore commented lines
    if obj.element[0] == "#":
        continue
    #
    try:
        page = urlopen(obj.url).read()
    except urllib.error.URLError as e:
        print(e)
        print("["+obj.url+"] did not give me any memes!")
        continue
    soup = BeautifulSoup(page, 'html.parser')
    soup = soup.find_all(obj.element)
    print("Extracting dank memes from [" + obj.url + "]")
    #
    for link in soup:
        meme_pic = link.get(obj.value)
        if meme_pic is not None:
            url_results += meme_pic + '\n'
#
# Write results to file
try:
    f = open(URL_RESULTS, 'w')
    f.write(url_results)
except FileNotFoundError:
    print("URL_RESULTS.txt was not found")
    exit(1)
else:
    print("Enough memes have been collected for a while, I need some rest for now.")


