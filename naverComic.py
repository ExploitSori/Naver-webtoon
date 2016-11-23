from requests import *
from bs4 import *

class naverComic:
	def __init__(self):
		self.url = "http://comic.naver.com/webtoon/detail.nhn?titleId=626907&no=123&weekday=000"
		self.getHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"}
		self.author = "antiweb <admin@hepstar.kr>"
		self.parseComic()
	def parseComic(self):
		readURL = get(self.url, headers=self.getHeader)
		setParse = BeautifulSoup(readURL.text, "html.parser")
		getURL = setParse.findAll('img', attrs={'alt':'comic content'})
		for i in range(len(getURL)):
			self.getImage(getURL[i]['src'], str(i))
	def getImage(self, url, filename):
		getImageURL = get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36", "Referer":self.url, "If-None-Match":repr("00000-0000000000000")}, stream=True)
		if getImageURL.status_code != 403:
			with open(filename+".jpg", 'wb') as f:
				for chunk in getImageURL:
					f.write(chunk)
if __name__ == '__main__':
	naverComic = naverComic()
