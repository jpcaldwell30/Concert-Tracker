#!/usr/bin/env python 
import requests
import json

#API key: REDACTED  
# api-endpoint 
URL = "https://api.songkick.com/api/3.0/users/jp-caldwell/events.json?"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS1 = {
	'apikey':'REDACTED',
	'attendance':'all',
	'per_page':50
}

PARAMS2 = {
	'apikey':'REDACTED',
	'attendance':'im_going',
	'per_page':50
}

PARAMS3 = {
	'apikey':'REDACTED',
	'attendance':'i_might_go',
	'per_page':50
}

allRequest = requests.get(url = URL, params = PARAMS1)
goingRequest = requests.get(url = URL, params = PARAMS2)
interestedRequest = requests.get(url = URL, params = PARAMS3)
 
# request json 
json_data1 = allRequest.json()
json_data2 = goingRequest.json()
json_data3 = interestedRequest.json()
#end request json

#file part
#with open ('songkick.txt') as json_file:
#	json_data = json.load(json_file)
#end file part
print ('User: jp-caldwell  \n')
print ('Total number of events: ' + str(json_data1['resultsPage']['totalEntries']) + '\n')
print ("Events I'm going to: " + str(json_data2['resultsPage']['totalEntries'])+ '\n\n')
for event in json_data2['resultsPage']['results']['event']:
	selected_data = event
	json_formatted_str = json.dumps(selected_data, indent=2)
	displayName = event['displayName']
	popularity = str(round((event['popularity'] * 1000),1))
	print (displayName.encode("utf-8") + ' Popularity: ' + popularity+ '\n\n')
print ('=====================\n\n')
print ("Events I'm interested in: " + str(json_data3['resultsPage']['totalEntries'])+ '\n')
for event in json_data3['resultsPage']['results']['event']:
	selected_data = event
	json_formatted_str = json.dumps(selected_data, indent=2)
	displayName = event['displayName']
	popularity = str(round((event['popularity'] * 1000),1))
	print (displayName.encode("utf-8") + ' Popularity: ' + popularity+ '\n\n')
	
