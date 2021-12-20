#/mnt/d/lsbap/Documents/GitHub/Python-for-Everybody
#CHAPTER 6
for letter in 'banana' :
    print(letter)

## First week
#Strings
# %%
'a' in 'banana'
# %%
stuff='Hello World'
dir(stuff)
# %%
word='banana'
word.upper()
# %%
#Format operators
camels=42
'I have spotted %d camels.' % camels
# %%
'In %d years i have spotted %g %s.' % (3,0.1,'camels')
# %%
#CHAPTER 7
##reading from txt
xfile=open('text.txt','r')
for line in xfile:
    line=line.rstrip()
    print(line)
# %%
xfile=open('text.txt','r')
count=0
for line in xfile:
    count=count+1
print('line count:', count)
# %%
xfile=open('text.txt','r')
inp=xfile.read()
print(len(inp))
# %%
xfile=open('text.txt','r')
for line in xfile:
    line=line.rstrip()
    if line.startswith('F'):
        print(line)
# %%
xfile=open('text.txt','r')
for line in xfile:
    line=line.rstrip()
    if not line.startswith('F'):
        continue # Do not print and restart
    print(line)
# %%
xfile=open('text.txt','r')
for line in xfile:
    line=line.rstrip()
    if not 'is all my' in line:
        continue # Do not print and restart
    print(line)
# %%
fname=input('Name of the file:  ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
for line in fhand:
    line=line.rstrip()
    if not 'is all my' in line:
        continue # Do not print and restart
    print(line)
# %%
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line=line.rstrip().upper()
    print(line)

    
# %%
# Use the file name mbox-short.txt as the file name
# Write a program that prompts for a file name, then opens that file and reads through the file,
#  looking for lines of the form:
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos=line.find('0')
    value=float(line[pos:])
    total=value + total
    count=count+1
print('Average spam confidence:',total/count)


# %%
fname = input("Enter file name: ")
fh = open(fname)
fh=fh.read()
fh=list(fh.split())
fh.sort()

rom=list()
for word in fh:
    if word not in rom:
        rom.append(word)

print(rom)
# %%
fname = input("Enter file name: ")
#guardian in a component statement
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    words=line.split()
    print(words[1])
    count=count + 1
    
    
print("There were", count, "lines in the file with From as the first word")


# %%
stuff = dict()
print(stuff['candy'])
# %%
stuff = dict()
print(stuff.get('candy',-1))
# %%

# DICTIONARY COUNT HISTOGRAM

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count=0
_name=[]

for line in handle:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    words=line.split()
    name=words[1]
    _name.append(name)
  
d = dict()
for name in _name:
    d[name] = d.get(name,0) + 1
    
maximum = 0
max_key = None
for k in d:
    if d[k] > maximum:
        maximum = d[k]
        max_key = k

print(max_key, maximum)

