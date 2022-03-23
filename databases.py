# %%
## Using Databases with Python

## EmailDB
  
import sqlite3

conn = sqlite3.connect('emaildb.sqlite') # Creates a file .sqlite that will be the DB file.
# we can open with SQLite Manager
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

# %%

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    print(email)
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, )) # question mark is a placeholder and is a way to make sure that we dont allow SQL injection
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) 
                VALUES ( ?, 1 )''', ( email, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', 
            (email, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# %%
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])

cur.close()


# %%
## ASSIGNEMENT COUNTING ORGANIZATIONS
  
import sqlite3

conn = sqlite3.connect('orgdb.sqlite') # Creates a file .sqlite that will be the DB file.
# we can open with SQLite Manager
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# %%

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')
    org=org[1]
    print(org)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, )) # question mark is a placeholder and is a way to make sure that we dont allow SQL injection
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# %%
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])

cur.close()
# %%

## TWITER SPIDER EXAMPLE

from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, friends INTEGER)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # Debugging
    # print json.dumps(js, indent=4)

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
                        (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
                        VALUES (?, 0, 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()

cur.close()

# %%
## 15.4 - Designing a Data Model

