#!/usr/bin/env python3
import requests
import json

# pass a dictionary to the data argument
shaidata = {"email": "sjwilson2@usfca.edu", "github": "https://github.com/shaiwilson/CODE2040.git"}
headers = {'content-type': 'application/json', "Accept": 'application/json'}
resp = requests.post('http://challenge.code2040.org/api/register', json = shaidata, headers = headers)
mytoken = resp.text
print(mytoken)

#{"result":"N1uMLlRYMt"}