import requests

url = "https://api.affinity.co"

conv = lambda i : i or 'None'

def get_all_notes(api_key):
	return requests.get(url + "/notes", auth=('', api_key))
	pass

def get_more_notes(api_key, token):
	return requests.get(url + "?page_token=" + str(token), auth=('', api_key))
	pass

def is_token(response):
	if response.json() is None:
		return False
	else:
		return True
	pass

# CSV
def write_row(file, row_array):
	file.writerow(row_array)
	pass

# Test method
# def get_all_notes(apikey):
# 	return requests.get(url + "/notes?page_size=3", auth=('', apikey))
# 	pass
