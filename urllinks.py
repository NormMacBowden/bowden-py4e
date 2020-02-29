# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

"""
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
"""

url = 'http://py4e-data.dr-chuck.net/known_by_Maura.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve the anchor tag at pos 17, follow the link and repeat
tags = soup('a')
nextlink = tags[17].get('href', None)
print(nextlink)

counter = 0
while counter <= 5:
    url = nextlink
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    nextlink = tags[17].get('href', None)
    print(nextlink)
    counter = counter + 1
    continue
