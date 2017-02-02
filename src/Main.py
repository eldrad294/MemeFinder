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
except FileNotFoundError:
    print("URL_CONFIG.txt was not found")
    exit()
#
# Iterate over items retrieved from URL_CONFIG
url_results = ''
for line in file:
    #
    obj = Meme_Object(line)
    try:
        page = urlopen(obj.get_url()).read()
    except urllib.error.URLError as e:
        print(e)
        print("Url does not exist: ["+obj.get_url()+"]")
        continue
    soup = BeautifulSoup(page, 'html.parser')
    soup = soup.find_all(obj.get_element())
    #
    for link in soup:
        meme_pic = link.get(obj.get_value())
        if meme_pic is not None:
            url_results += meme_pic + '\n'
#
# Write results to file
try:
    f = open(URL_RESULTS, 'w')
    f.write(url_results)
except FileNotFoundError:
    print("URL_RESULTS.txt was not found")
    exit()


