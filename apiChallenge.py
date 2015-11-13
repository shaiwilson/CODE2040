#!/usr/bin/python
# Author : Shai Wilson
# Email: Sjwilson2@usfca.edu
# This challenge is split into two parts
# Part one: registration
# Part two: four challenges

import json
import requests

def validatechallenge(info, url):
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
	string - json.loads(query)['results']
	reverseS = string[::-1]
	print(string)
	print(reverseS)

	#return {'token': token, 'string': reverseS}

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

	print new_array

	#return {'token': token, 'array': new_array}


#def datingGame(query, token):

#def findNeedle(query, token):

def main():

	mydata = "N1uMLlRYMt"

	challenge_urls = [
	'http://challenge.code2040.org/api/getstring',
	'http://challenge.code2040.org/api/prefix',
	'http://challenge.code2040.org/api/time',
	'http://challenge.code2040.org/api/haystack',
	]

	state = raw_input()

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