from api_key import *
from helper import *

import csv
import requests
import time





with open('log.csv', 'w', newline='') as csvfile:
    log = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    write_row(log, ["id", 'creator_id', 'person_ids', 'organization_ids', 'opertunity_ids', 'parent_id', 'is meeting', 'timestamp', 'content'])
    write_row(log,['Spam'] * 5 + ['Baked Beans'])


    response = get_all_notes(api_key)
    row_data = []

    # If this is the last page, do this
    if is_token(response) is False:
    	print("Last Page, no token")
    	# print(conv(response.json()['next_page_token']))
    	additonal_pages = False
    elif is_token(response) is True:
    	print("Token found")
    	# print(conv(response.json()['next_page_token']))
    else:
    	print("Neither")
    	pass
    



