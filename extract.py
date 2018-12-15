import sys
import urllib.request
from bs4 import BeautifulSoup

def extract(url):
	pass

urls = []

for arg in sys.argv[1:]:
	urls.append(arg)

for url in urls:
	print("Downloading " + url)
	with urllib.request.urlopen(url) as response:
		html = response.read()
	page = BeautifulSoup(html, features="html.parser")
	titles = page.body.findAll('span', attrs={'class' : 'tracklist-item__text__headline'})
	for title in titles:
		print(title.text)
