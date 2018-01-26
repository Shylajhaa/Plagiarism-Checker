from ReadDocument import ReadDocument
from WebSearch import WebSearch

my_api_key = "AIzaSyAl0NqvVvge5td_pAlLqSRgVcULEuqmw1M"
my_cse_id = "015309536654007099184:olg4fuwb_vy"
fileName1 = 'holography.txt'
readDoc = ReadDocument()
keywords = readDoc.printFile(fileName1)
#print(keywords)
'''print(len(keywords))
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']'''
webSearch = WebSearch()
for word in keywords:
	results = webSearch.google_search(word, my_api_key, my_cse_id, num=1)
	for result in results:
		title = result['title']
		link = result['formattedUrl']
		dis = result['snippet']
		print (title)
		#results.append(result['title'])
		print (link)
		print (dis)
		print("......")
#result = google_search(keywords[-1], my_api_key, my_cse_id, num=1)
#print(result)