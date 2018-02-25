from ReadDocument import ReadDocument
from WebSearch import WebSearch
from Similarity import Similarity

fileName1 = 'holography.txt'
fileName2 = 'RaspberryPiabsoly.txt'
fileName3 = 'virtualMouse.txt'
fileName4 = 'nanorobots.txt'
fileName5 = 'miniSearchEngine.txt'
fileName6 = 'password.txt'
fileName7 = 'harrypotter.txt'
fileName8 = 'department_auto.txt'

responseDoc = 'result.txt'

#responseDoc = fileName5;

#requestDoc = 'abstract.txt'
requestDoc = fileName5

readDoc = ReadDocument()
print("Reading input document")
fileContent = readDoc.readFile(requestDoc)
keywords = readDoc.getKeywords(fileContent)


#print(keywords)
#print(len(keywords))


webSearch = WebSearch()
print("crawling the web")
webSearch.google_search(keywords)
#webSearch.trialSearch()	

checkSimilarity = Similarity()
print("checking similarity")
value = checkSimilarity.similarValue(requestDoc,responseDoc)
f = open(responseDoc, 'r+')
f.truncate()
print("----------SIMILARITY-----------")
#print(value)
resultValue = str(round((value*100),2))+"%"
#print(str(round((value*100),2))+"%")
print(resultValue);
file = open('similarityValue.txt','w',encoding='utf-8')
file.write(str(resultValue))
print("-------------------------------")