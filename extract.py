import sys
import urllib
from bs4 import BeautifulSoup

def extract(url):
	pass

urls = []

for arg in sys.argv[1:]:
	urls.append(arg)

for url in urls:
	print("URL: " + url)
