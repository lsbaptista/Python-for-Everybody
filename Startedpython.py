from _typeshed import IdentityFunction
import sys
print(sys.version)

# %%
x=20
print(x)

if x < 5:
    print("Smaller")
if x > 20:
    print("Bigger")

#%%
def sum():
    x=1+1
    print(x)

    # %%

sum()

# %%
name=input('What is your name?\n')
print(name)

# %%
int(98.6)
# %%
name = input("Enter your name:\n")
# %%
print("Hello", name)

#%%
# My paychech

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

print("Pay:", float(hrs)*float(rate))

# %%
# Conditional execution
x=1
if x == True:
    print("True")
# %%
if x < 0 :
    pass # need to handle negative values!
# %%
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')
# %%
# Chained conditionals
y=4
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
# %%
# Nested conditionals

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
# %%
if 0 < x and x < 10:
    print('x is a positive single-digit number.')
# %%
# Catching exceptions using try and except

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
# %%
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')
# %%
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1

print(istr)
# %%
astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)
# %%
# Teste
print("monica")
#%%
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.

hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

print(h,r)
if h <=40:
    print(h*r)
else:
    hmore= h-40
    hmore=hmore*r*1.5
    print(40*r + hmore)

# %%
# Write a program to prompt for a score between 0.0 and 1.0
score = input("Enter Score: ")

score = float(score)
if score >=0 and score<=1:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("number must be between 0 and 1")

    
# %%
# FUNCTIONS
max("whatisyourname")
len("what in the hell ")

import random

for i in range(10):
    x=random.random()
    print(x)

# %%
t=[1,2,3]
random.choice(t)

# %%
import math

degree=45
radians=degree/360*2*math.pi
math.sin(radians)
# %%
# Adding new functions
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print(print_lyrics)
print(type(print_lyrics))
print_lyrics()
# %%
# REPEAT FUNCTION
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
# %%
# Parameters and arguments
def print_twice(bruce):
    print(bruce)
    print(bruce)

import math

print_twice(math.pi)
print_twice("spam"*4)

mick="What"
print_twice(mick)

# %%
# Fruitful functions and void functions
def addtwo(a,b):
    added=a+b
    return added

x=addtwo(4,4)
print(x)

# %%
def stuff():
    print('Hello')
    return
    print('World')

stuff()
# %%
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay

def computepay(h, r):
    if h <=40:
        w=h*r
        return  w
    else:
        hmore= h-40
        hmore=hmore*r*1.5
        w=40*r + hmore
        return w

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

p = computepay(h, r)

print("Pay", p)


# %%
# ITERATION
# The while statement - loop
n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff')

# %%
# Infinite loops and break

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# %%
# Finishing iterations with continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue # it ignores and continue executing the code
    if line == 'done':
        break
    print(line)
print('Done!')
# %%
# Definite loops using for
friends = ['Joseph','Glenn','Sally']

for friend in friends:
    print('Happy new year:', friend)
print('Done!')
# %%
# Loop patterns
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar #accumulator
print('Total: ', total)

# %%
# Maximun and smallest value
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)


# %%
num = 0
tot = 0.0

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('invalid error')
        continue
    print(fval)
    num = num +1
    tot = tot + fval

print('All done')
print(tot,num,tot/num)
# %%
l = None
s = None

while True:
    sval = input('Enter a number: ')
    if sval == 'done': 
        break
    try:
        sval = int(sval)
    except:
        print('Invalid input')
        continue
    if l is None or sval>l:
        l=sval 
    elif s is None or sval<s:
        s=sval

print('Maximum is',l)
print('Minimum is',s)

# %%

