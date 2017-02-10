#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2017-02-10

import requests, json

# Setup
URL = 'https://www.googleapis.com/customsearch/v1'
APIKEY = open('google_api.token').readline().rstrip()
CXID = open('google_custom_search_engine_id.token').readline().rstrip()
QUERIES = [
    '化粧'
]

payload = {
    'key': APIKEY,
    'cx': CXID,
    'q': ' '.join(QUERIES),
    # 'imageType': 'image',
    'num': 1,
    'start': 1
}

result = requests.get(URL, params=payload)
print('Request URL:', result.url)
print('Result')
print(result)
