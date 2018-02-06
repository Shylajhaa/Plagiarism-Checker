from ReadDocument import ReadDocument
from WebSearch import WebSearch
from Similarity import Similarity

fileName1 = 'holography.txt'
fileName2 = 'RaspberryPiabsoly.txt'
fileName3 = 'virtualMouse.txt'
fileName4 = 'nanorobots.txt'
fileName5 = 'miniSearchEngine.txt'
fileName6 = 'password.txt'
responseDoc = 'result.txt'

requestDoc = fileName1

readDoc = ReadDocument()
fileContent = readDoc.readFile(requestDoc)
keywords = readDoc.getKeywords(fileContent)


#print(keywords)
#print(len(keywords))


webSearch = WebSearch()
webSearch.google_search(keywords)
#webSearch.trialSearch()	

checkSimilarity = Similarity()
value = checkSimilarity.similarValue(requestDoc,responseDoc)
print(value)