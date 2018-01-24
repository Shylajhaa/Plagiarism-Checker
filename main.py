from ReadDocument import ReadDocument
from WebSearch import WebSearch
#import WebSearch
class GetDocument():
	fileName1 = 'holography.txt'
	readDoc = ReadDocument()
	keywords = readDoc.printFile(fileName1)
	#print(keywords)
	#print(len(keywords))
	webSearch = WebSearch()
	results = []
	for word in keywords:
		results.append(webSearch.findPages(word))