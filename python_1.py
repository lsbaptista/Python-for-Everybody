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

# %%
