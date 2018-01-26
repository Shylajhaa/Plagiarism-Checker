from googleapiclient.discovery import build

class WebSearch():
	def google_search(self,search_term, api_key, cse_id, **kwargs):
	    service = build("customsearch", "v1", developerKey=api_key)
	    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
	    return res['items']
