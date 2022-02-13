## REGULAR EXPRESSIONS
# %%
import re

hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^X.*:', line): # . is any character and * means zero or more times
        print(line)
# %%
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^X-\S+:', line):# \S match any non-whitespace character + one or more times
        print(line)

##EXTRACTING DATA
# %%
x="My 2 favorite numbersx are 19 and 42"
y=re.findall('[0-9]+',x) # one or more digits + one or more digits
print(y)
# %%
y=re.findall('[AEIOU]+',x) # one or more digits + one or more digits
print(y)
# %%
y=re.findall('[aeiou]+',x) # one or more digits + one or more digits
print(y)
# %%
x="From: Using the : character"
y=re.findall('^F.+:',x) #greedy algorithm it do not stop at the first :
print(y)
# %%
x="From: Using the : character"
y=re.findall('^F.+?:',x) # ? do not be greedy 
print(y)
# %%
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    y=re.findall('\S+@\S+', line)
    print(y)
# %%
x="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y=re.findall('\S+@\S+', x)
print(y)
# %%
y=re.findall('^From (\S+@\S+)', x) # parentesis start extracting only inside them
print(y)
# %%
y=re.findall('^From \S+@\S+', x)
print(y)
# %%
y=re.findall('@([^ ]*)', x) # extract only after@, match non.blanck character, math many of them
print(y)
# %%
y=re.findall('From .*@([^ ]*)', x) # extract only after@, match non.blanck character, math many of them
print(y)
# %%
hand=open('mbox-short.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line) # . is for float
    #print(stuff)
    #print(len(stuff))
    if len(stuff) != 1 : continue
    num=float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
# %%
x="We just receive $100 for cookies"
y=re.findall('\$[0-9.]+', x)# \ excape
print(y)
# %%
import pandas as pd
hand=open('sample.txt')
text=hand.read()
y=re.findall('[0-9]+',text) # one or more digits + one or more digits
y=[int(i)for i in y]
sum(y)
# %%
hand=open('actualData.txt')
text=hand.read()
y=re.findall('[0-9]+',text) # one or more digits + one or more digits
y=[int(i)for i in y]
sum(y)
# %%
## NETWORKED TECHNOLOGY
# Sockets in Python  (comunication)

# %%
import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # Host and port 80

cmd= 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()

# %%
## Programs that Surf the Web
print(ord('H'))

# %%
# Using urllib in Python

import urllib.request, urllib.parse,urllib.error

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
# %%
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts=dict()
for line in fhand:
    words=line.decode().strip()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)

## Parsing Web Pages
# %%
import urllib.request, urllib.parse,urllib.error
import bs4 as bs

# %%
url=input('Enter -')
html=urllib.request.urlopen(url).read()
soup=bs(html,'html.parser')

# Retrive all off the anchor tags
tags=soup('a')
for tag in tags:
    print(tag.get('href', None))
# %%
import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup as bs
import ssl

# Ignore ssl.create_default_context()
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter -')
html=urllib.request.urlopen(url,context=ctx).read()
soup=bs(html,'html.parser')

# Retrive all off the anchor tags
tags=soup('a')
for tag in tags:
    print(tag.get('href', None))


# %%
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum=0
for tag in tags:
    sum=sum+ int(tag.contents[0])
print(sum)


# %%
##Scraping HTML Data with BeautifulSoup

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)


# %%

## Assignment: Following Links in HTML Using BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
n=0
while n<7:
    tags = soup('a')
    url = tags[17].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    n=n+1

mytag=tags[17]
print('Contents:', mytag.contents)
    

# %%

## WEEK 5 - Web Services and XML

import xml.etree.ElementTree as ET 
data = '''
<person>
    <name>Chuck</name> 
    <phone type="intl">
        +1 734 303 4456 
    </phone>
    <email hide="yes"/> 
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text) 
print('Attr:', tree.find('email').get('hide'))

# %%

## Multiple child tags

import xml.etree.ElementTree as ET 
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name> 
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name> 
        </user>
    </users> 
</stuff>'''

stuff = ET.fromstring(input) 
lst = stuff.findall('users/user') 

print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))

# %%

## Extracting Data from XML - Assignment
## Example

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)

# %%

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://py4e-data.dr-chuck.net/comments_1403950.xml"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print('Comment count:', len(results))
sum=0
for item in results:
    print('Count:', item.find('count').text)
    sum=sum+int(item.find('count').text)
print(sum)
 








# %%
