from googlesearch import search
import requests
from bs4 import BeautifulSoup


class WebSearch(): 	
	def google_search(self,keywords):
		for word in keywords:
			for link in search(word, tld="co.in", num=10, stop=1, pause=1):
				#print(link)
				if 'wikipedia' in link:
					content = ""
					f = requests.get(link)
					page = f.text
					soup = BeautifulSoup(page, 'html.parser')
					para = soup.find_all('p')
					for element in para:
						content = content + element.get_text()	
					file = open('result.txt','a',encoding='utf-8')
					file.write(str(content))

	
	'''def trialSearch(self):
		link = 'https://en.wikipedia.org/wiki/Holographic_data_storage'
		f = requests.get(link)
		page = f.text
		soup = BeautifulSoup(page, 'html.parser')
		content = soup.get_text()
		file = open('result.txt','a',encoding='utf-8')
		file.write(content)'''