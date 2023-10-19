x = 25

def printer():
    x = 50 
    return x

print(x)
#GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
    #ENCLOSING
    name = "Sammy"

    def hello():
        #LOCAL
        name = "IM A LOCAL"
        print("Hello "+name)
    
    hello()
greet()

x =50

def func():
    global x
    print(f'X is {x}')
    #local reassignment on a global variable!
    x = "NEW VALUE"
    print(f'I JUSR LOCALLY CHANGED X TO {x}')

func()

print("HOMEWORK")
print("HOMEWORK 1")

def vol(rad):
   return (4/3)*(3.14)*(rad**3)

result = vol(2)
print(result)

print("HOMEWORK 2")

def ran_check(num, low, high):
    return num <= high and num >= low

result1 = ran_check(5,2,7)
print(result1)

print("HOMEWORK 3")
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s) 

def up_low(s):
    d={"upper":0, "lower":0}
    for char in s:
        if char.isupper():
            d["upper"]+=1
        elif char.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)