import json
import requests

def reversed_string(data, token):
	string - json.loads(data)['results']
	reverseS = string[::-1]
	print(string)
	print(reverseS)

def reversed_string():

def prefix():

def datingGame():

def findNeedle():


def main():
	
	mydata = "N1uMLlRYMt"

	def challenge(stageNumber):
		data_url = {
		0:['http://challenge.code2040.org/api/getstring', 'http://challenge.code2040.org/api/validatestring'],
		1:['http://challenge.code2040.org/api/haystack', 'http://challenge.code2040.org/api/validateneedle'],
		2:['http://challenge.code2040.org/api/prefix', 'http://challenge.code2040.org/api/validateprefix'],
		3:['http://challenge.code2040.org/api/time', 'http://challenge.code2040.org/api/validatetime']}


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

        
main()