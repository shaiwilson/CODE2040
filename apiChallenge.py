#!/usr/bin/python
# Author : Shai Wilson
# Email: Sjwilson2@usfca.edu
# This challenge is split into two parts
# Part one: registration -- project.py
# Part two: four challenges

# imports
import json
import requests
from datetime import datetime, timedelta

def validateChallenge(info, url):
    headers = {'content-type': 'application/json', "Accept": 'application/json'}
    resp = requests.post('http://challenge.code2040.org/api/register', json = info, headers = headers)
    output = resp.text
    print(output)

    return json.loads(content)['result']


def getChallenge(token,url):
    info = {'token':token}
    headers = {'content-type': 'application/json', "Accept": 'application/json'}
    resp = requests.post('http://challenge.code2040.org/api/register', json = info, headers = headers)
    output = resp.text
    print(output)
    
    return output


"""
This function expects a string and returns the reversed string
"""
def reversed_string(query, token):
	string = json.loads(query)['results']
	reverseS = string[::-1]

	return {'token': token, 'string': reverseS}

"""
This function expects a dictionary and returns an array of strings that do not contain the prefix
"""

def prefix(query, token):
	array = result['array']
	result = json.loads(query)['result']
	prefix = result['prefix']
	new_array = []
	for index in array:
		if index.startswith(prefix, 0, len(prefix) == False):
			new_array.append(index)
	#return {'token': token, 'array': new_array}

def datingGame(query, token):
	result = json.loads(query)['result']
	datestamp = result['datestamp']
	interval = result['interval']
	new_date = timedelta(0,interval) + date
	date = datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
	new_date_formatted = new_date.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z"

	return {'token':token, 'datestamp':new_date_formatted}

"""
This function expects a dictionary with two values and keys. The first value, a needle and the second a haystack, an array of strings.
First, locate the needle in the 'haystack' (array). Then return the position (count), of the needle. 
"""

def findNeedle(query, token):
	json_data = json.loads(query)
	needle = json_data['result']['needle']
	haystack = json_data['result']['haystack']
	count = 0
	for index in haystack:
			if needle == index:
				return {'token': token,'needle': count}
	count += 1

def main():

	#my token
	mydata = "N1uMLlRYMt"
	state = 1

	challenge_urls = [
	'http://challenge.code2040.org/api/getstring',
	'http://challenge.code2040.org/api/prefix',
	'http://challenge.code2040.org/api/time',
	'http://challenge.code2040.org/api/haystack',
	]

	validation_urls= [
        'http://challenge.code2040.org/api/validatestring',
        'http://challenge.code2040.org/api/validateprefix',
        'http://challenge.code2040.org/api/validatetime',
        'http://challenge.code2040.org/api/validateneedle'
    ]

	if state == 1:
	    query = getChallenge(mydata, challenge_urls[0])
	    result = reversed_string(query, mydata)

	elif state == 2:
	    query = getChallenge(mydata, challenge_urls[1])
	    result = prefix(query, mydata)

	elif state == 3:
	    query = getChallenge(mydata,challenge_urls[2])
	    result = datingGame(query, mydata)

	elif state == 4:
	    query = getChallenge(mydata,challenge_urls[3])
	    result = findNeedle(query, mydata)


if __name__ == "__main__":
    main()
