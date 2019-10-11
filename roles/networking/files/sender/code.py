import os
import time
import requests

flag = os.environ.get('FLAG')
url = 'http://receiver/flag'

while True:
    requests.post(url, data={'flag': flag})
    time.sleep(30)
